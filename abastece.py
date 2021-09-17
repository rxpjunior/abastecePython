import operacoesBd, adminBd

#adminBd.excluiBd()
#adminBd.criarTabelasBD()
#operacoesBd.inserirVeiculo("DDD-4726", "Fiorino")
#operacoesBd.alterarVeiculo(1,"CCC-3954", "Intruder")
#print(operacoesBd.pesquisaTodosVeiculos())
for x in operacoesBd.pesquisaVeiculo(1):
    print(x[0])
