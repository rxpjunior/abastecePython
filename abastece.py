import os 
import operacoesBd as opbd

# MENU DO VEÍCULO
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
        
        # INSERINDO UM VEICULO
        if op == '1':
            os.system('cls') or None
            aux = ''
            placa = ''
            modelo = ''
            while(aux != '0'):
                aux = input("ENTRE COM A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
                if aux == '0':
                    continue
                else:
                    placa = aux
                    break
            while(aux != '0'):
                aux = input("ENTRE COM O MODELO DO VEÍCULO OU 0 PARA SAIR: ")
                if aux == 0:
                    continue
                else:
                    modelo = aux
                    break
            if aux != '0':
                print(opbd.insereVeiculo(placa, modelo))
                os.system('pause')
            
        # CONSULTANDO OS DADOS DE UM VEÍCULO
        elif op == '2':
            os.system('cls') or None
            placa = input("ENTRE COM A PLACA DO VEÍCULO: ")
            veiculo = opbd.pesquisaVeiculoPlaca(placa)
            if len(veiculo) == 0:
                print("NENHUM VEÍCULO ENCONTRADO")
                os.system('pause')
            else:
                print("VEÍCULO ID:",veiculo[0][0])
                print("PLACA:",veiculo[0][1])
                print("MODELO:",veiculo[0][2])
                os.system('pause')
        
        # CONSULTANDO TODOS OS VEÍCULOS
        elif op == '3':
            os.system('cls') or None
            print("LISTANDO TODOS OS VEÍCULOS\n")
            veiculo = opbd.pesquisaTodosVeiculos()
            if len(veiculo) == 0:
                print("NENHUM VEÍCULO ENCONTRADO")
                os.system('pause')
            else:
                cont = 0
                for x in veiculo:
                    print("VEÍCULO ID:",veiculo[cont][0])
                    print("PLACA:",veiculo[cont][1])
                    print("MODELO:",veiculo[cont][2])
                    print("\n")
                    cont += 1
            os.system('pause')
            
        elif op == '4':
            os.system('cls') or None
            placa = ''
            placa = input("INSIRA A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
            if placa != "0":
                veiculo = opbd.pesquisaVeiculoPlaca(placa)
                if len(veiculo) == 0:
                    print("NÃO FOI ENCONTRADO O VEÍCULO")
                else:
                    print(opbd.excluiVeiculo(veiculo[0][0]))
                os.system('pause')

# MENU DE ABASTECIMENTO
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
        
        # INSERINDO UM ABASTECIMENTO
        if op == '1':
             os.system('cls') or None
             aux = ''
             placa = ''
             data = ''
             combustivel = ''
             valorLitro = ''
             quantLitro = ''
             vTotal = ''
             kmAbastecimento = ''
             veiculo = ''
             vclidVeiculo = ''
             while(aux != '0'):
                 aux = input("ENTRE COM A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
                 if aux == 0:
                     continue
                 else:
                     veiculo = opbd.pesquisaVeiculoPlaca(aux)
                     if len(veiculo) == 0:
                         aux = input("\n\PLACA INVÁLIDA. TENTE NOVAMENTE!\n")
                     else:
                         vclidVeiculo = veiculo[0][0]
                     break
             while(aux != '0'):
                 print("ENTRE COM 1 PARA GASOLINA")
                 print("ENTRE COM 2 PARA ALCOOL")
                 print("ENTRE COM 3 PARA DIESEL")
                 print("ENTRE COM 4 GAS NATURAL")
                 print("ENTRE COM 0 PARA SAIR")
                 aux = input("ENTRE COM UMA DAS OPÇÕES ACIMA: ")
                 if aux == '0':
                     continue
                 else:
                     if aux == '1':
                         combustivel = "GASOLINA"
                         break
                     elif aux == '2':
                         combustivel = "ALCOOL"
                         break
                     elif aux == '3':
                         combustivel = "DIESEL"
                         break
                     elif aux == '4':
                         combustivel = "GÁS NATURAL"
                         break
             while(aux != '0'):
                 aux = input("ENTRE COM A DATA DO ABASTECIMENTO (EX: 01-10-2021) OU 0 PARA SAIR: ")
                 if aux == 0:
                     continue
                 else:
                     data = aux[6:]+'-'+aux[3:5]+'-'+aux[0:2]
                     break
             while(aux != '0'):
                 aux = input("ENTRE COM O VALOR DO LITRO DE COMBUSTÍVEL (EX: 4.54) OU 0 PARA SAIR: ")
                 if aux == 0:
                     continue
                 else:
                     valorLitro = float(aux)
                     break
             while(aux != '0'):
                 aux = input("ENTRE COM A QUANTIDADE DE LITROS DE COMBUSTÍVEL OU 0 PARA SAIR: ")
                 if aux == 0:
                     continue
                 else:
                     quantLitro = float(aux)
                     break
             while(aux != '0'):
                 aux = input("ENTRE COM O VALOR TOTAL DO ABASTECIMENTO OU 0 PARA SAIR: ")
                 if aux == 0:
                     continue
                 else:
                     vTotal = float(aux)
                     break
             while(aux != '0'):
                 aux = input("ENTRE COM A KM DO VEÍCULO OU 0 PARA SAIR: ")
                 if aux == 0:
                     continue
                 else:
                     kmAbastecimento = int(aux)
                     break
            
             if aux != '0':
                 print(opbd.insereAbastecimento(data, combustivel, valorLitro, quantLitro, vTotal, kmAbastecimento, vclidVeiculo))
                 os.system('pause')
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
