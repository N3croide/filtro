import ui.menus as me, functions.otrasFunciones as otf, modules.coreFileManager as cfm, modules.peliculas as pe, modules.generos as gen, modules.actores as ac, modules.formatos as form

if __name__ == "__main__":
    while(True):
        opcion = me.mostrarMenu('principal')
        if(opcion == 1):
            opcion = me.mostrarMenu('generos')
            if(opcion == 1):
                gen.createGen()
            elif(opcion == 2):
                gen.searchGen()
        elif(opcion == 2):
            opcion = me.mostrarMenu('actores')
            if(opcion == 1):
                ac.createAct()
            elif(opcion == 2):
                ac.searchAct()
        elif(opcion == 3):
            opcion = me.mostrarMenu('formatos')
            if(opcion == 1):
                form.createForm()
            elif(opcion == 2):
                form.searchForm()
        elif(opcion == 4):
            opcion = me.mostrarMenu('informes')
            if(opcion == 1):
                pass
            elif(opcion == 2):
                pass
        elif(opcion == 5):
            opcion =  me.mostrarMenu('peliculas')
            if(opcion == 1):
                pe.createPel()
            elif(opcion == 2):
                pe.searchPel()
        elif(opcion == 6):
            break
    otf.bp()
    print('Gracias por utilizar nuestro software.')
    otf.pausa()