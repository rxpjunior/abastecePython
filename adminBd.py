import sqlite3
import os

# Excluindo BD
def excluiBd():
    bd = "abastece.db"
    ## Se existir, delete ##
    if os.path.isfile(bd):
        os.remove(bd)
    else:    ## Se houver erro ##
        print("Erro: %s Banco de Dados não encontrado: " % bd)

# Criando BD 
def criarTabelasBD():
    conn = sqlite3.connect("abastece.db")
    cursor = conn.cursor()
    
    conn.execute("""
        CREATE TABLE veiculo (
            idVeiculo INTEGER PRIMARY KEY AUTOINCREMENT,
            placa     CHAR    NOT NULL,
            modelo            NOT NULL
        )
    """)

    
    conn.execute("""
        CREATE TABLE abastecimento (
            idAbastecimento INTEGER PRIMARY KEY AUTOINCREMENT,
            data            DATE,
            combustivel     CHAR,
            valorLitro      DOUBLE,
            quantLitro      DOUBLE,
            vTotal          DOUBLE,
            kmAbastecimento INT,
            vcl_idVeiculo   INT     REFERENCES veiculo (idVeiculo) 
                                    NOT NULL
        )
    """)
