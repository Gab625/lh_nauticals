from pathlib import Path
from datetime import datetime
from src.config import SILVER_DIR, SCHEMA_SCRIPT

def csv_to_ddl(caminho_csv: Path, arquivo_saida: Path):
    timestamp_formats = [
        "%Y-%m-%d %H:%M:%S",  # 2026-02-06 22:34:19
        "%d/%m/%Y %H:%M:%S",  # 06/02/2026 22:34:19
    ]


    # Validar timestamps
    def is_timestamp(valor):
        for fmt in timestamp_formats:
            try:
                datetime.strptime(valor, fmt)
                return True
            except ValueError:
                pass

        return False

    # Validar e classificar números
    def infer_numeric(valor):
        try:
            number = int(valor)

            if -2147483648 <= number <= 2147483647:
                return "INTEGER"
            else:
                return "NUMERIC"

        except ValueError:
            pass

        try:
            float(valor)
            return "NUMERIC"

        except ValueError:
            return None

    # Validar booleanos
    def is_boolean(valor):
        return valor.lower() in ("true", "false")

    def descobrir_tipo(valores_coluna):
        """
        Recebe todos os valores de uma coluna
        e retorna o tipo SQL mais apropriado.
        """

        valores = []

        for valor in valores_coluna:
            valor = valor.strip()
            if valor != "":
                valores.append(valor)

        if not valores:
            return "TEXT"

        # TIMESTAMP
        if all(is_timestamp(valor) for valor in valores):
            return "TIMESTAMP"

        # BOOL
        if all(is_boolean(valor) for valor in valores):
            return "BOOL"

        # Números
        tipos_numericos = [
            infer_numeric(valor)
            for valor in valores
        ]

        # Todos os valores são numéricos
        if all(tipo is not None for tipo in tipos_numericos):

            if "NUMERIC" in tipos_numericos:
                return "NUMERIC"

            return "INTEGER"

        # Qualquer outro valor
        return "TEXT"

    # varre os arquivos CSV no diretório especificado e gera o SQL correspondente
    for arquivo in caminho_csv.iterdir():
        if arquivo.suffix == ".csv":
            nome_tabela = arquivo.stem 

            with open(arquivo, "r", encoding="utf-8") as f:
                linhas = f.readlines()

            chaves = []
            for c in linhas[0].strip("\n").split(","):
                chaves.append(c.strip())

            dados = {}
            for c in chaves:
                dados[c] = []

            for l in linhas[1:]:
                valores = l.strip("\n").split(",")
                for i in range(len(valores)):
                    if i < len(chaves):
                        dados[chaves[i]].append(valores[i])

            tipos_colunas = {}
            for col, valores_coluna in dados.items():
                tipos_colunas[col] = descobrir_tipo(valores_coluna)

            colunas_sql = [
                f"    {col} {tipo}" for col, tipo in tipos_colunas.items()
            ]
            definicao = ",\n".join(colunas_sql)

            sql_tabela = (
                f"DROP TABLE IF EXISTS {nome_tabela};\n"
                f"CREATE TABLE {nome_tabela} (\n{definicao}\n);\n\n"
            )
            

            with open(arquivo_saida, mode="a", encoding="utf-8") as f:
                f.write(sql_tabela)

            print(f"{nome_tabela} gerada!")

if __name__ == "__main__":
    caminho_csv = SILVER_DIR
    arquivo_saida = Path("schema.sql")
    csv_to_ddl(caminho_csv, arquivo_saida)