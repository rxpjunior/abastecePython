# MENU DE ABASTECIMENTO
import os
import operacoesBd as opbd

def menuAbastecimento():
    op = ''
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
             print("CADASTRO DE ABASTECIMENTO\n")
             while(aux != '0'):
                 aux = input("ENTRE COM A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
                 if aux == '0':
                     continue
                 else:
                     veiculo = opbd.pesquisaVeiculoPlaca(aux)
                     if len(veiculo) == 0:
                         aux = input("\nVEÍCULO NÃO ENCONTRADO! PRESSIONE QUALQUER TECLA E TENTE NOVAMENTE\n")
                     else:
                         vclidVeiculo = veiculo[0][0]
                         break
             while(aux != '0'):
                 os.system('cls') or None
                 print("ENTRE COM O TIPO DE COMBUSTÍVEL\n")
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
                     else: 
                        print("OPÇÃO INVÁLIDA! SELECIONE UM NÚMERO DE 0 A 4")
             while(aux != '0'):
                 os.system('cls') or None
                 print("DATA DO ABASTECIMENTO\n")
                 aux = input("ENTRE COM A DATA DO ABASTECIMENTO (EX: 01-10-2021) OU 0 PARA SAIR: ")
                 if aux == '0':
                     continue
                 else:
                     data = aux[6:]+'-'+aux[3:5]+'-'+aux[0:2]
                     break
             while(aux != '0'):
                 os.system('cls') or None
                 print("VALOR DO LITRO DO COMBUSTÍVEL\n")
                 aux = input("ENTRE COM O VALOR DO LITRO DE COMBUSTÍVEL (EX: 4.54) OU 0 PARA SAIR: ")
                 if aux == '0':
                     continue
                 else:
                     valorLitro = float(aux)
                     break
             while(aux != '0'):
                 os.system('cls') or None
                 print("LITROS OU METROS CÚBICOS ABASTECIDOS\n")
                 aux = input("ENTRE COM A QUANTIDADE DE LITROS OU METROS CÚBIDOS ABASTECIDOS OU 0 PARA SAIR: ")
                 if aux == '0':
                     continue
                 else:
                     quantLitro = float(aux)
                     break
             while(aux != '0'):
                 vTotal = float(valorLitro) * float(quantLitro)
                 print(f"VALOR TOTAL DO ABASTECIMENTO: R$ {vTotal:.2f}")
                 aux2 = ''
                 while(aux2 != '1' ):
                     aux2 = input("ACEITA O VALOR CALCULADO ? ENTRE 1 PARA SIM E QUALQUER OUTRA TECLA PARA NÃO: ")
                     if aux2 == '1':
                         break
                     else:
                         os.system('cls') or None
                         aux = input("ENTRE COM O VALOR DO ABASTECIMENTO OU 0 PARA SAIR: ")
                         break
                 if aux == '0':
                     continue
                 else:
                     vTotal = float(aux)
                     break
             while(aux != '0'):
                 aux = input("ENTRE COM A KM DO VEÍCULO OU 0 PARA SAIR: ")
                 if aux == '0':
                     continue
                 else:
                     kmAbastecimento = int(aux)
                     break
             if aux != '0':
                 print(opbd.insereAbastecimento(data, combustivel, valorLitro, quantLitro, vTotal, kmAbastecimento, vclidVeiculo))
                 os.system('pause')
             else:
                aux = ''
                 
        elif op == '2':
            ...
        
        elif op == '3':
            os.system('cls') or None
            print("LISTANDO TODOS OS ABASTECIMENTOS POR UM PERÍODO\n")
            aux = input("ENTRE COM A DATA INICIAL (EX: 01-10-2021): ")
            dInicial = aux[6:]+'-'+aux[3:5]+'-'+aux[0:2]
            aux = input("ENTRE COM A DATA FINAL (EX: 01-10-2021): ")
            dFinal = aux[6:]+'-'+aux[3:5]+'-'+aux[0:2]
            abastecimento = opbd.pesquisaTodosAbastecimentosEntreDatas(dInicial, dFinal)
            if len(abastecimento) == 0:
                print("NENHUM ABASTECIMENTO ENCONTRADO\n")
                
            else:
                cont = 0
                for x in abastecimento:
                    veiculo = opbd.pesquisaVeiculoId(abastecimento[cont][7])
                    print("ABASTECIMENTO ID:",abastecimento[cont][0])
                    print("VEÍCULO: ",veiculo)
                    print("DATA:",abastecimento[cont][1])
                    print("COMBUSTÍVEL:",abastecimento[cont][2])
                    print("VALOR DO LITRO: R$ ",abastecimento[cont][3])
                    print("QUANTIDADE ABASTECIDA: ",abastecimento[cont][4])
                    print("VALOR TOTAL DO ABASTECIMENTO: R$ ",abastecimento[cont][5])
                    print("KM DO VEÍCULO: ",abastecimento[cont][6])
                    print("\n")
                    cont += 1
            os.system('pause')

        elif op == '4':
            os.system('cls') or None
            print("LISTANDO TODOS OS ABASTECIMENTOS DE UM VEÍCULO POR UM PERÍODO\n")
            aux = input("ENTRE COM A DATA INICIAL (EX: 01-10-2021): ")
            dInicial = aux[6:]+'-'+aux[3:5]+'-'+aux[0:2]
            aux = input("ENTRE COM A DATA FINAL (EX: 01-10-2021): ")
            dFinal = aux[6:]+'-'+aux[3:5]+'-'+aux[0:2]
            placa = input("ENTRE COM A PLACA DO VEÍCULO OU 0 PARA SAIR: ")
            veiculo = opbd.pesquisaVeiculoPlaca(placa)
            abastecimento = opbd.pesquisaTodosAbastecimentosPorVeiculoEData(placa,dInicial,dFinal)
            if aux == '0':
                op = '0'
            elif len(abastecimento) == 0 or len(veiculo) == 0:
                print("NENHUM ABASTECIMENTO ENCONTRADO\n")
                
            else:
                cont = 0
                for x in abastecimento:
                    veiculo = opbd.pesquisaVeiculoId(abastecimento[cont][7])
                    print("ABASTECIMENTO ID:",abastecimento[cont][0])
                    print("VEÍCULO: ",veiculo)
                    print("DATA:",abastecimento[cont][1])
                    print("COMBUSTÍVEL:",abastecimento[cont][2])
                    print("VALOR DO LITRO: R$ ",abastecimento[cont][3])
                    print("QUANTIDADE ABASTECIDA: ",abastecimento[cont][4])
                    print("VALOR TOTAL DO ABASTECIMENTO: R$ ",abastecimento[cont][5])
                    print("KM DO VEÍCULO: ",abastecimento[cont][6])
                    print("\n")
                    cont += 1
            os.system('pause')