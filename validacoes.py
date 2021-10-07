
def validaPlaca(placa):
    aux = placa.replace("-","")
    aux = aux.replace(" ","")
    tamanho = True if len(aux) == 7 else False
    if not tamanho:
        return False
    else:
        p1Placa = True if (aux[0].isalpha() and aux[1].isalpha() and aux[2].isalpha) else False
        p2Placa = True if (aux[3].isdigit()) else False
        p3Placa = True if (aux[4].isdigit() or aux[4].isalpha()) else False
        p4Placa = True if (aux[5].isdigit() and aux[6].isdigit()) else False
        return (p1Placa and p2Placa and p3Placa and p4Placa)

def validaData(d):
    if len(d) != 10:
        return False
    elif (d[2] !=  '-' or d[5] != '-'):
        return False
    else:
        p1Data = True if(d[0].isdigit() and d[1].isdigit() and d[3].isdigit() and d[4].isdigit() and d[6].isdigit() and d[7].isdigit() and d[8].isdigit() and d[9].isdigit()) else False
        return p1Data



def converteDataInternacional(data):
    ...

def converteDataNacional(data):
    ...


