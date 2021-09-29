# MENU DO VEÍCULO
import os
import operacoesBd as opbd

def menuVeiculo():
    op = ''
    aux = ''
    placa = ''
    modelo = ''
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
            print("CADASTRO DE VEÍCULOS\n")
            while(aux != '0'):
                aux = input("ENTRE COM A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
                if aux == '0':
                    continue
                else:
                    placa = aux
                    break
            while(aux != '0'):
                aux = input("ENTRE COM O MODELO DO VEÍCULO OU 0 PARA SAIR: ")
                if aux == '0':
                    continue
                else:
                    modelo = aux
                    break
            if aux != '0':
                print(opbd.insereVeiculo(placa, modelo))
                os.system('pause')
            else:
                aux = ''
            
        # CONSULTANDO OS DADOS DE UM VEÍCULO
        elif op == '2':
            os.system('cls') or None
            print("CONSULTA DE VEÍCULO POR PLACA\n")
            placa = input("ENTRE COM A PLACA DO VEÍCULO: ")
            veiculo = opbd.pesquisaVeiculoPlaca(placa)
            if len(veiculo) == 0:
                print("NENHUM VEÍCULO ENCONTRADO\n")
                os.system('pause')
            else:
                print("VEÍCULO ID:",veiculo[0][0])
                print("PLACA:",veiculo[0][1])
                print("MODELO:",veiculo[0][2])
                print("\n")
                os.system('pause')
        
        # CONSULTANDO TODOS OS VEÍCULOS
        elif op == '3':
            os.system('cls') or None
            print("LISTANDO TODOS OS VEÍCULOS\n")
            veiculo = opbd.pesquisaTodosVeiculos()
            if len(veiculo) == 0:
                print("NENHUM VEÍCULO ENCONTRADO\n")
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
            print("EXCLUSÃO DE VEÍCULO POR PLACA\n")
            placa = input("INSIRA A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
            if placa != "0":
                veiculo = opbd.pesquisaVeiculoPlaca(placa)
                if len(veiculo) == 0:
                    print("VEÍCULO NÃO FOI ENCONTRADO\n")
                else:
                    print(opbd.excluiVeiculo(veiculo[0][0]))
                os.system('pause')