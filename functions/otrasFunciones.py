import os

def pausa():
    input('Presione una tecla para continuar...')

def bp():
    os.system('clear')


def validDato(cadena, tipo):
    dato = ''
    tipoUsuario = ''
    dato.strip()
    if(tipo == int):
        tipoUsuario = 'Entero'
    elif(tipo == str):
        tipoUsuario = 'Cadena o texto'
    while(True):
        try:
            dato = tipo(input(cadena))
        except ValueError:
            print(f'El dato debe ser de tipo {tipoUsuario}')
            pausa()
        else:
            if(tipo == str and dato.strip() == ''):
                print('El dato no puede estar vacio')
            else:
                return dato