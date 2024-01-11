import functions.otrasFunciones as otf, modules.coreFileManager as cfm

DB_ROUTE = 'data/formatos.json'

formatos = {}
cfm.checkFile(DB=DB_ROUTE, data = formatos)


def createForm():
    dbForm = formatos
    id = 'F00'
    if len(dbForm) > 0:
        id = list(dbForm.keys())[-1]
    
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
    id = 'F' + str(digitos[0]) + str(digitos[1])

    form = {}
    form.update({id:{'id':id,'nombre':otf.validDato("Ingrese el nombre del formato: ",str)}})
    cfm.addData(DB = DB_ROUTE, data = form)
    cfm.checkFile(DB = DB_ROUTE, data = formatos)

def searchForm():
    dbForm = formatos
    for key, item in dbForm.items():
        print(" -- ".join(f"{llave.upper()}: {valor}" for llave, valor in item.items()))
    otf.pausa()

def seleccionar() -> dict:
    i = 1
    llaves = []
    for key, item in formatos.items():
        for llave, valor in item.items():
            if(llave != 'id'):
                print(i,'. ',valor)
                i += 1
            else:
                llaves.append(valor)
    while (opcion > i or opcion == 0):
        opcion = otf.validDato('Seleccione una opcion valida',int)
    opcion = otf.validDato('Seleccione un formato: ',int)
    return formatos[llaves[opcion-1]]