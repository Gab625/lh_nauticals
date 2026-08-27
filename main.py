from src.script_bronze import load_bronze
from src.script_silver import run_silver

def main():
    print("Executando camada BRONZE")
    load_bronze()

    print("Executando camada SILVER")
    run_silver()



if __name__ == "__main__":
    main()