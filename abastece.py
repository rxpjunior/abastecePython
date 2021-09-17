import operacoesBd, adminBd

#adminBd.excluiBd()
#adminBd.criarTabelasBD()
operacoesBd.inserirVeiculo("DDD-4726", "Fiorino")
operacoesBd.alterarVeiculo(1,"CCC-3954", "Intruder")
print(operacoesBd.pesquisaTodosVeiculos())

operacoesBd.excluiVeiculo(1)

print(operacoesBd.pesquisaTodosVeiculos())
