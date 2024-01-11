import functions.otrasFunciones as otf

menus = {
    'principal' : ['Administrador de generos', 'Administrador de actores', 'Administrador de formatos', 'Gestor de informes','Gestor de peliculas','Salir'],
    'generos' : ['Crear generos', 'Listar generos','Ir al menu principal'],
    'actores' : ['Crear actor', 'Listar actor','Ir al menu principal'],
    'formatos' : ['Crear formato', 'Listar formato','Ir al menu principal'],
    'peliculas' : ['Agregar pelicula', 'Editar pelicula','Eliminar pelicula','Eliminar actor','Buscar pelicula','Listar todas las peliculas', 'Menu principal'],
    'informes' : ['Listar pelicula de un genero especifico', 'Listar peliculas donde el protagonista sea Silvester Stallone','Buscar pelicula y mostrar sinopsis y los actores','Menu principal']
}


def mostrarMenu(menu : str):
    otf.bp()
    print('\n'.join (f'{i+1}. {item}' for i,item in enumerate(menus.get(menu))))
    opcion = otf.validDato('Selecciones una opcion: ', int)
    return opcion