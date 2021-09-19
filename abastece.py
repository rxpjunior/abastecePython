import os 

def menuVeiculo():
    op = ''
    while(op != '0'):
        os.system('cls') or None
        print("VEÍCULOS\n")
        print("DIGITE 1 PARA CADASTRAR UM VEÍCULO")
        print("DIGITE 2 PARA CONSULTAR OS DADOS DE UM VEÍCULO")
        print("DIGITE 3 PARA LISTAR TODOS OS VEÍCULOS")
        print("DIGITE 4 PARA EXCLUIR UM VEÍCULO")
        print("DIGITE 0 PARA SAIR DO MENU")
       
        op = input("Entre com uma das opções: ")
        if op != '1' and op != '2' and op != '3' and op != '4' and op != '0':
            print("\n\n")
            print("OPÇÃO INVÁLIDA\n\n")
            os.system("pause")
        if op == '1':
            ...
        elif op == '2':
            ...
        elif op == '3':
            ...
        elif op == '4':
            ...

def menuAbastecimento():
    op = ''
    while(op != '0'):
        os.system('cls') or None
        print("ABASTECIMENTOS\n")
        print("DIGITE 1 PARA CADASTRAR UM ABASTECIMENTO")
        print("DIGITE 2 PARA CONSULTAR OS DADOS DE UM ABASTECIMENTO")
        print("DIGITE 3 PARA LISTAR TODOS OS ABASTECIMENTOS EM UM PERÍODO")
        print("DIGITE 4 PARA LISTAR TODOS OS ABASTECIMENTOS DE UM VEÍCULO EM UM PERÍODO")
        print("DIGITE 5 PARA APAGAR UM ABASTECIMENTO")
        print("DIGITE 0 PARA SAIR DO MENU")
       
        op = input("Entre com uma das opções: ")
        if op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '0':
            print("\n\n")
            print("OPÇÃO INVÁLIDA\n\n")
            os.system("pause")
        if op == '1':
            ...
        elif op == '2':
            ...
        elif op == '3':
            ...
        elif op == '4':
            ...

# MENU PRINCIPAL
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
        
        menuVeiculo()

    elif op == '2':
        
        menuAbastecimento()

print("Programa encerrado")
os.system("pause")
