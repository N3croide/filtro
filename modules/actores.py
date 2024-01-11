import functions.otrasFunciones as otf, modules.coreFileManager as cfm

DB_ROUTE = 'data/actores.json'

actores = {}
cfm.checkFile(DB=DB_ROUTE, data = actores)

def createAct():
    dbAct = actores
    id = 'A00'
    if len(dbAct) > 0:
        id = list(dbAct.keys())[-1]
    
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
    id = 'A' + str(digitos[0]) + str(digitos[1])

    act = {}
    act.update({id:{'id':id,'nombre':otf.validDato("Ingrese el nombre del genero: ",str)}})
    cfm.addData(DB = DB_ROUTE, data = act)
    cfm.checkFile(DB = DB_ROUTE, data = actores)

def searchAct():
    dbAct = actores
    for key, item in dbAct.items():
        print(" -- ".join(f"{llave.upper()}: {valor}" for llave, valor in item.items()))
    otf.pausa()

def seleccionar() -> dict:
    i = 1
    llaves = []
    for key, item in actores.items():
        for llave, valor in item.items():
            if(llave != 'id'):
                print(i,'. ',valor)
                i += 1
            else:
                llaves.append(valor)
    while (opcion > i or opcion == 0):
        opcion = otf.validDato('Seleccione una opcion valida',int)           
    opcion = otf.validDato('Seleccione un actor: ',int)
    return actores[llaves[opcion-1]]