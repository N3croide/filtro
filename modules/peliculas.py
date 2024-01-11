import functions.otrasFunciones as otf, modules.coreFileManager as cfm,modules.generos as gen, modules.formatos as form, modules.actores as act

DB_ROUTE = 'data/peliculas.json'

peliculas = {}
cfm.checkFile(DB=DB_ROUTE, data = peliculas)

def createPel():
    dbPel = peliculas
    id = 'P00'
    if len(dbPel) > 0:
        id = list(dbPel.keys())[-1]
    
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
    id = 'P' + str(digitos[0]) + str(digitos[1])

    pel = {}
    nombrePel = otf.validDato("Ingrese el nombre del pelicula: ",str)
    duracion = otf.validDato("Ingrese la duracion de la pelicula: ",float)
    sinopsis = otf.validDato("Ingrese la sinopsis de la pelicula: ", str)
    genero = {'generos':{}}
    actores = {}
    formato = {}

    while(True):
        genero.get('generos').update(gen.seleccionar())
        if(otf.validDato('Quiere seleccionar otro genero ? S(si) o N(no)') in 'Nn'):
            break
    while(True):
        actores.get('actores').update(gen.seleccionar())
        if(act.validDato('Quiere seleccionar otro Actor ? S(si) o N(no)') in 'Nn'):
            break
    while(True):
        formato.get('formatos').update(gen.seleccionar())
        if(form.validDato('Quiere seleccionar otro Formato ? S(si) o N(no)') in 'Nn'):
            break
    pel.update({'nombre':nombrePel,'duracion':duracion,'sinopsis':sinopsis,'actores':genero,'formato':actores,'genero':formato})
    pel.update({id:pel})
    cfm.addData(DB = DB_ROUTE, data = pel)
    cfm.checkFile(DB=DB_ROUTE, data = peliculas)

def searchPel():
    dbPel = peliculas
    for key, item in dbPel.items():
        print(" -- ".join(f"{llave.upper()}: {valor}" for llave, valor in item.items()))
    otf.pausa()
