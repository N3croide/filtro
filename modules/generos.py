import functions.otrasFunciones as otf

DB_ROUTE = 'data/generos.json'

def createGen(dbGEn : str):
    id = 'F00'
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
    id = 'F' + str(digitos[0]) + str(digitos[1])

    gen = {}
    gen.update({id:{'id':id,'nombre':otf.validDato("Ingrese el nombre del genero: ",str)}})
    