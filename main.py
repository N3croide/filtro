import ui.menus as me, functions.otrasFunciones as otf, modules.coreFileManager as cfm, modules.peliculas as pe, modules.generos as gen, modules.actores as ac, modules.formatos as form

peliculas = {}
generos = {}
actores = {}
formatos = {}

cfm.checkFile(DB=pe.DB_ROUTE, data = peliculas)
cfm.checkFile(DB=gen.DB_ROUTE, data = generos)
cfm.checkFile(DB=ac.DB_ROUTE, data = actores)
cfm.checkFile(DB=form.DB_ROUTE, data = formatos)


if __name__ == "__main__":
    while(True):
        opcion = me.mostrarMenu('principal')
        if(opcion == 1):
            opcion = me.mostrarMenu('generos')
            if(opcion == 1):
                gen.createGen(generos)
        elif(opcion == 2):
            opcion = me.mostrarMenu('actores')
        elif(opcion == 3):
            opcion = me.mostrarMenu('formatos')
        elif(opcion == 4):
            opcion = me.mostrarMenu('informes')
        elif(opcion == 5):
           opcion =  me.mostrarMenu('peliculas')
        elif(opcion == 6):
            break
    otf.bp()
    print('Gracias por utilizar nuestro software.')
    otf.pausa()