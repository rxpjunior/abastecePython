import operacoesBd, adminBd

adminBd.excluiBd()
adminBd.criaTabelasBD()
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

print("Pesquisa todos os veículos depois de exclusão")
for x in operacoesBd.pesquisaTodosVeiculos():
    print(x)

print("Pesquisa Veículo ID 2",operacoesBd.pesquisaVeiculoId(2))

print("Pesquisa Veículo Placa CCC-2222",operacoesBd.pesquisaVeiculoPlaca("CCC-2222"))

