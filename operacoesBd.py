import sqlite3


# OPERAÇÕES NA TABELA DE VEÍCULOS

def insereVeiculo(placa, modelo):
    conn = sqlite3.connect("abastece.db")
    conn.execute("insert into Veiculo (placa, modelo) values (?, ?)", (placa, modelo ))
    conn.commit()

def alteraVeiculo(id, placa, modelo):
    conn = sqlite3.connect("abastece.db")
    conn.execute("update Veiculo SET placa = ?, modelo = ? where idVeiculo = ?", (placa, modelo, id))
    conn.commit()

def pesquisaTodosVeiculos():
    listaVeiculo = []
    conn = sqlite3.connect("abastece.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Veiculo")
    rows = cur.fetchall()
    for row in rows:
        listaVeiculo.append(row)
    return listaVeiculo

def pesquisaVeiculoId(id):
    listaVeiculo = []
    conn = sqlite3.connect("abastece.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Veiculo where idVeiculo = ?",(id,))
    rows = cur.fetchall()
    for row in rows:
        listaVeiculo.append(row)
    return listaVeiculo

def pesquisaVeiculoPlaca(placa):
    listaVeiculo = []
    conn = sqlite3.connect("abastece.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Veiculo where placa = ?",(placa,))
    rows = cur.fetchall()
    for row in rows:
        listaVeiculo.append(row)
    return listaVeiculo

def excluiVeiculo(id):
    conn = sqlite3.connect("abastece.db")
    conn.execute("delete from Veiculo where idVeiculo = ?", (id,))
    conn.commit()

# OPERAÇÕES NA TABELA DE ABASTECIMENTOS

