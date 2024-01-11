import functions.otrasFunciones as otf, modules.coreFileManager as cfm

DB_ROUTE = 'data/generos.json'

generos = {}
cfm.checkFile(DB=DB_ROUTE, data = generos)

def createGen():
    dbGEn = generos
    id = 'G00'
    if len(dbGEn) > 0:
        id = list(dbGEn.keys())[-1]
    
    digitos = []
    for item in id:
        try:
            int(item)
        except ValueError:
            pass
        else:
            digitos.append(int(item))
    if digitos[1] == 9:
        digitos[0] += 1
        digitos[1] = 0
    else:
        digitos[1] += 1
    id = 'G' + str(digitos[0]) + str(digitos[1])

    gen = {}
    gen.update({id:{'id':id,'nombre':otf.validDato("Ingrese el nombre del genero: ",str)}})
    cfm.addData(DB = DB_ROUTE,data = gen)
    cfm.checkFile(DB=DB_ROUTE, data = generos)

def searchGen():
    dbGen = generos
    for key, item in dbGen.items():
        print(" -- ".join(f"{llave.upper()}: {valor}" for llave, valor in item.items()))
    otf.pausa()

def seleccionar() -> dict:
    i = 1
    llaves = []
    for key, item in generos.items():
        for llave, valor in item.items():
            if(llave != 'id'):
                print(i,'. ',valor)
            else:
                llaves.append(valor)
            i += 1
    opcion = otf.validDato('Seleccione un genero: ',int)
    return generos[llaves[opcion]]