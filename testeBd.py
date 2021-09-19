import operacoesBd, adminBd

# REMOÇÃO E CRIAÇÃO DO BD 
adminBd.excluiBd()
adminBd.criaTabelasBD()

# TESTES NA TABELA VEÍCULO
operacoesBd.insereVeiculo("DDD-4726", "Fiorino")
operacoesBd.insereVeiculo("CCC-3954", "Intruder")
print("Pesquisa todos os veículos")
for x in operacoesBd.pesquisaTodosVeiculos():
    print(x)

operacoesBd.alteraVeiculo(1,"DDD-1111", "Fiorino")
operacoesBd.alteraVeiculo(2,"CCC-2222", "Intruder")
print("Pesquisa todos os veículos depois de alteração")
for x in operacoesBd.pesquisaTodosVeiculos():
    print(x)

operacoesBd.excluiVeiculo(1)
operacoesBd.insereVeiculo("DDD-4726", "Fiorino")

print("Pesquisa todos os veículos depois de exclusão")
for x in operacoesBd.pesquisaTodosVeiculos():
    print(x)

print("Pesquisa Veículo ID 2",operacoesBd.pesquisaVeiculoId(2))

print("Pesquisa Veículo Placa CCC-2222",operacoesBd.pesquisaVeiculoPlaca("CCC-2222"))

# TESTES NA TABELA ABASTECIMENTO
operacoesBd.insereAbastecimento("2021-08-18", "Gasolina", 5.67, 25.3, 143.45, 22547, 2)
operacoesBd.insereAbastecimento("2021-09-30", "Gasolina", 5.67, 30, 170.10, 23000, 2)
operacoesBd.insereAbastecimento("2021-10-15", "Gasolina", 5.67, 40, 226.80, 23500, 2)
operacoesBd.insereAbastecimento("2021-11-10", "Alcool", 4.40, 25.30, 111.32, 125412, 3)
operacoesBd.insereAbastecimento("2021-12-10", "Alcool", 4.40, 30, 132.00, 125682, 3)
operacoesBd.insereAbastecimento("2022-01-10", "Alcool", 4.40, 40, 176.00, 125772, 3)

operacoesBd.alteraAbastecimento("2021-08-01", "Gasolina", 5.67, 25.3, 143.45, 22547, 2, 1)

print("Abastecimentos do Veículo de placa CCC-2222")
for x in operacoesBd.pesquisaTodosAbastecimentosPorVeiculo("CCC-2222"):
    print(x)

print("Abastecimentos de todos os  Veículos entre as datas 01/08/2021 e 01/12/2021")
for x in operacoesBd.pesquisaTodosAbastecimentosEntreDatas("2021-08-01","2021-12-01"):
    print(x)

operacoesBd.excluiAbastecimento(4)

print("Abastecimentos do Veículo de placa CCC-2222 e entre as datas 01/01/2021 e 01/02/2022")
for x in operacoesBd.pesquisaTodosAbastecimentosPorVeiculoEData("CCC-2222","2021-01-01","2022-02-01"):
    print(x)

