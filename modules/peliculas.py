import functions.otrasFunciones as otf, modules.coreFileManager as cfm,modules.generos as gen, modules.formatos as form, modules.actores as act

DB_ROUTE = 'data/peliculas.json'

peliculas = {'blockbuster':{
    'peliculas':{}
}}
cfm.checkFile(DB=DB_ROUTE, data = peliculas)

def createPel():
    dbPel = peliculas
    otf.bp()
    idp = 'P00'
    if len(dbPel.get('blockbuster').get('peliculas')) > 0:
        idp = list(dbPel.get('blockbuster').get('peliculas').keys())[-1]
    
    digitos = []
    for item in idp:
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
    idp = 'P' + str(digitos[0]) + str(digitos[1])

    pel = {}
    nombrePel = otf.validDato("Ingrese el nombre del pelicula: ",str)
    duracion = otf.validDato("Ingrese la duracion de la pelicula: ",float)
    sinopsis = otf.validDato("Ingrese la sinopsis de la pelicula: ", str)
    genero = {}
    actores = {}
    formato = {}

    while(True):
        genero.update(gen.seleccionar())
        if(otf.validDato('Quiere seleccionar otro genero ? S(si) o N(no)', str) in 'Nn'):
            break
    while(True):
        actores.update(act.seleccionar())
        if(otf.validDato('Quiere seleccionar otro Actor ? S(si) o N(no)', str) in 'Nn'):
            break
    while(True):
        formato.update(form.seleccionar())
        if(otf.validDato('Quiere seleccionar otro Formato ? S(si) o N(no)', str) in 'Nn'):
            break
    pel.update({idp:{'id':idp, 'nombre':nombrePel,'duracion':duracion,'sinopsis':sinopsis,'generos':genero,'actores':actores,'formato':formato}})
    print(pel)
    peliculas.get('blockbuster').get('peliculas').update(pel)
    cfm.addData(DB = DB_ROUTE, data = peliculas)

def searchPel(**arg):
    dbPel = peliculas
    if (len(arg) == 0):
        for key, item in dbPel.get('blockbuster').get('peliculas').items():
                for llave, valor in item.items():
                    if (type(valor) != dict):
                        print(f"{llave.upper()}: {valor}")
                    else:
                        print(f"{llave.upper()}: {valor.get('nombre')}")
    else:
        nombre = arg['pel']
        for key, item in dbPel.get('blockbuster').get('peliculas').items():
                if (item.get('nombre') == nombre):
                    for llave, valor in item.items():
                        if (type(valor) != dict):
                            print(f"{llave.upper()}: {valor}")
                        else:
                            print(f"{llave.upper()}: {valor.get('nombre')}")
        
    otf.pausa()

def editPel():
    otf.bp()
    i = 0
    ids = []
    for key, item in peliculas.get('blockbuster').get('peliculas').items():
        i += 1
        print(i,'. ',end='')
        for llaves, valor in item.items():
            if llaves == 'id' or llaves == 'nombre':
                print(f'{llaves}: {valor}',end=' ')
                if key not in ids:
                    ids.append(key)
        print("")

    peliID = otf.validDato('Seleccione una pelicula: ', int)
    while (peliID > i or peliID == 0):
        peliID = otf.validDato('Seleccione una opcion valida: ',int)

    print('\n'.join(f'{key}. {value}' for key, value in peliculas.get('blockbuster').get('peliculas').get(ids[peliID-1]).items()))
    otf.pausa()

    print('Que desea editar ? \n1.Nombre\n2.duracion\n3.sinopsis\n4.generos\n5.actores\n6.formatos')
    opcion = otf.validDato('selecciones una opcion: ',int)

    peliculaEdit = peliculas.get('blockbuster').get('peliculas').get(ids[peliID-1])

    if(opcion == 1):
        peliculaEdit.update({'nombre':otf.validDato('Ingrese el nuevo nombre',str)})
    elif(opcion == 2):
        peliculaEdit.update({'duracion':otf.validDato('Ingrese la nueva duracion',float)})
    elif(opcion == 3):
        peliculaEdit.update({'sinopsis':otf.validDato('Ingrese la nueva sinopsis',str)})
    elif(opcion == 4):
        pass
    elif(opcion == 5):
        pass
    elif(opcion == 6):
        pass

def delPel():
    otf.bp()
    i = 0
    ids = []
    for key, item in peliculas.get('blockbuster').get('peliculas').items():
        i += 1
        print(i,'. ',end='')
        for llaves, valor in item.items():
            if llaves == 'id' or llaves == 'nombre':
                print(f'{llaves}: {valor}',end=' ')
                if key not in ids:
                    ids.append(key)
        print("")

    peliID = otf.validDato('Seleccione una pelicula: ', int)
    while (peliID > i or peliID == 0):
        peliID = otf.validDato('Seleccione una opcion valida: ',int)
    pelDel = peliculas.get('blockbuster').get('peliculas').get(ids[peliID-1])

    cfm.deleteData(DB = DB_ROUTE, delete = pelDel)
    cfm.checkFile(DB= DB_ROUTE, data = peliculas)
    print('Pelicula borrada con exito')
    otf.pausa()

def genero(**arg):
    nombre = arg['gen']
    for key, item in peliculas.get('blockbuster').get('peliculas').items():
            if (item.get('genero') == nombre):
                for llave, valor in item.items():
                    if (type(valor) != dict):
                        print(f"{llave.upper()}: {valor}")
                    else:
                        print(f"{llave.upper()}: {valor.get('nombre')}")
    