import sqlite3


# OPERAÇÕES NA TABELA DE VEÍCULOS

def insereVeiculo(placa, modelo):
    try:
        conn = sqlite3.connect("abastece.db")
        conn.execute("insert into Veiculo (placa, modelo) values (?, ?)", (placa.upper(), modelo.upper() ))
        conn.commit()
        return "REGISTRO INSERIDO COM SUCESSO"
    except Exception as erro:
        print("Erro: ",erro)
        return "ERRO AO INSERIR O REGISTRO"

def alteraVeiculo(id, placa, modelo):
    try:
        conn = sqlite3.connect("abastece.db")
        conn.execute("update Veiculo SET placa = ?, modelo = ? where idVeiculo = ?", (placa.upper(), modelo.upper(), id))
        conn.commit()
        print("Registro atualizado com sucesso")
    except Exception as erro:
        print("Erro: ",erro)

def pesquisaTodosVeiculos():
    try:
        listaVeiculo = []
        conn = sqlite3.connect("abastece.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Veiculo")
        rows = cur.fetchall()
        for row in rows:
            listaVeiculo.append(row)
        return listaVeiculo
    except Exception as erro:
        print("Erro: ",erro)

def pesquisaVeiculoId(id):
    try:
        listaVeiculo = []
        conn = sqlite3.connect("abastece.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Veiculo where idVeiculo = ?",(id,))
        rows = cur.fetchall()
        for row in rows:
            listaVeiculo.append(row)
        return listaVeiculo
    except Exception as erro:
        print("Erro: ",erro)

def pesquisaVeiculoPlaca(placa):
    try:
        listaVeiculo = []
        conn = sqlite3.connect("abastece.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Veiculo where placa = ?",(placa.upper(),))
        rows = cur.fetchall()
        for row in rows:
            listaVeiculo.append(row)
        return listaVeiculo
    except Exception as erro:
        print("Erro: ",erro)

def excluiVeiculo(id):
    try:
        conn = sqlite3.connect("abastece.db")
        conn.execute("delete from Veiculo where idVeiculo = ?", (id,))
        conn.commit()
        print("Registro apagado com sucesso")
    except Exception as erro:
        print("Erro: ",erro)

# OPERAÇÕES NA TABELA DE ABASTECIMENTOS

def insereAbastecimento(data, combustivel, valorLitro, quantLitro, vtotal, kmAbastecimento, vcl_idVeiculo):
    try:
        conn = sqlite3.connect("abastece.db")
        conn.execute("insert into Abastecimento (data, combustivel, valorLitro, quantLitro, vtotal, kmAbastecimento, vcl_idVeiculo) values (?, ?, ?, ?, ?, ?, ?)", (data, combustivel.upper(), valorLitro, quantLitro, vtotal, kmAbastecimento, vcl_idVeiculo ))
        conn.commit()
        print("Registro inserido com sucesso")
    except Exception as erro:
        print("Erro: ",erro)

def alteraAbastecimento(data, combustivel, valorLitro, quantLitro, vtotal, kmAbastecimento, vcl_idVeiculo, idAbastecimento):
    try:
        conn = sqlite3.connect("abastece.db")
        conn.execute("update Abastecimento SET data = ?, combustivel = ?, valorLitro = ?, quantLitro = ?, vtotal = ?, kmAbastecimento = ?, vcl_idVeiculo = ? where idAbastecimento = ?", (data, combustivel.upper(), valorLitro, quantLitro, vtotal, kmAbastecimento, vcl_idVeiculo, idAbastecimento))
        conn.commit()
        print("Registro atualizado com sucesso")
    except Exception as erro:
        print("Erro: ",erro)

def pesquisaTodosAbastecimentosPorVeiculo(placa):
    try:
        listaAbastecimento = []
        veiculo = pesquisaVeiculoPlaca(placa.upper())
        id = veiculo[0][0]
        conn = sqlite3.connect("abastece.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Abastecimento where vcl_idVeiculo = ?",(id,))
        rows = cur.fetchall()
        for row in rows:
            listaAbastecimento.append(row)
        return listaAbastecimento
    except Exception as erro:
        print("Erro: ",erro)

def pesquisaTodosAbastecimentosEntreDatas(d1, d2):
    try:
        listaAbastecimento = []
        conn = sqlite3.connect("abastece.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Abastecimento where data BETWEEN ? and ?",(d1, d2,))
        rows = cur.fetchall()
        for row in rows:
            listaAbastecimento.append(row)
        return listaAbastecimento
    except Exception as erro:
        print("Erro: ",erro)

def pesquisaTodosAbastecimentosPorVeiculoEData(placa, d1, d2):
    try:
        listaAbastecimento = []
        veiculo = pesquisaVeiculoPlaca(placa.upper())
        id = veiculo[0][0]
        conn = sqlite3.connect("abastece.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Abastecimento where vcl_idVeiculo = ? and data BETWEEN ? and ?",(id, d1, d2,))
        rows = cur.fetchall()
        for row in rows:
            listaAbastecimento.append(row)
        return listaAbastecimento
    except Exception as erro:
        print("Erro: ",erro)

def excluiAbastecimento(id):
    try:
        conn = sqlite3.connect("abastece.db")
        conn.execute("delete from Abastecimento where idAbastecimento = ?",(id,))
        conn.commit()
        print("Registro apagado com sucesso")
    except Exception as erro:
        print("Erro: ",erro)


