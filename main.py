from src.script_gold import run_gold
from src.script_bronze import run_bronze
from src.script_silver import run_silver

def main():
    print("Executando camada BRONZE")
    run_bronze()

    print("Executando camada SILVER")
    run_silver()

    print("Executando camada GOLD")
    run_gold()

if __name__ == "__main__":
    main()