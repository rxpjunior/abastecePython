# MENU PRINCIPAL
import os
import menuAbastecimento as abastecimento
import menuVeiculo as veiculo
import adminBd

op = ''
while(op !='0'):
    os.system('cls') or None
    print("SOFTWARE DE CONTROLE DE ABASTECIMENTOS - ABASTECE PYTHON\n")
    print("DIGITE 1 PARA MENU DE VEÍCULOS")
    print("DIGITE 2 PARA MENU DE ABASTECIMENTOS")
    print("DIGITE 0 PARA SAIR")

    op = input("Entre com uma das opções: ")
    if op != '1' and op != '2' and op != '0':
        print("\n\n")
        print("OPÇÃO INVÁLIDA\n\n")
        os.system("pause")
    if op == '1':
        
        veiculo.menuVeiculo()

    elif op == '2':
        
        abastecimento.menuAbastecimento()

print("Programa encerrado")
os.system("pause")
