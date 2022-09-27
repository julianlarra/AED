'''
1. (Parcial 2019) - Servicios de Limpieza
Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos.
Por cada trabajo se tienen los siguientes datos: el número de identificación del trabajo, la descripción o nombre del
mismo, el tipo de trabajo (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados), el importe a cobrar por
 ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar la información referida a
 los n trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea
positivo y que el importe a cobrar sea mayor a cero. Puede hacer la carga en forma manual, o puede generar los datos en
 forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
 programar.
2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.
3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si
hay varios trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal
 sea máxima).
4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado.
Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con
esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
5- Determinar y mostrar la cantidad de trabajos por tipo.
'''
#Importar

import random
from ej_1_modulo import Trabajo

## funciones
def areglos():
    print('| '*40)
    print(' *'*39)
    print('| '*40)


def mostrar_menu():
    print('\n     Menu de opciones: ')
    print('\n1- Cargar cantidad de trabajos.')
    print('2- Mostrar todos los trabajos ordenados por importe.')
    print('3- Mostrar trabajo con mas personal.')
    print('4- Buscar trabajo por descripcion.')
    print('5- ')
    print('6- Salir.')


def generar_trabajos(trabajos, trabajos_cantidad):
    #generar datos num_trabajo,descripcion,tipo_trabajo,importe,cant_personal)
    num_trabajo = len(trabajos)
    for i in range(trabajos_cantidad):
        num_trabajo += 1
        num_trabajo = validar_trabajos_cantidad(num_trabajo)
        descripcion =random.choice(('Limpiar','Ordenar','Reparar','Mantenimiento','Gestionar stock')).lower()
        tipo_trabajo = random.randint(0,3)
        importe = random.randint(1500,15000)
        while importe <= 0:
            importe= int(input('\n Ingrese un importe mayor a $0.'))
        cant_personal= random.randint(1,20)

        #crear vector
        trabajo = Trabajo(num_trabajo,descripcion,tipo_trabajo,importe,cant_personal)

        #cargar vector
        trabajos.append(trabajo)




def validar_trabajos_cantidad(trabajos_cantidad):
    while trabajos_cantidad < 0:
        trabajos_cantidad = int(input('\nIngrese un numero de trabjos positivo:  '))
    return trabajos_cantidad


def ordenar(trabajos):
    n = len(trabajos)
    for pivot in range(0,n-1):
        for sig in range(pivot+1,n):
            if trabajos[pivot].importe < trabajos[sig].importe:
                trabajos[pivot],trabajos[sig] = trabajos[sig] , trabajos[pivot]
    for i in range(n):
        print(trabajos[i])


def mas_personal(trabajos):
      n = len(trabajos)
      for anterior in range(0,n-1):
          for sig in range(anterior+1,n):
              if trabajos[anterior].cant_personal < trabajos[sig].cant_personal:
                  trabajos[anterior].cant_personal,trabajos[sig].cant_personal= trabajos[sig].cant_personal,trabajos[anterior].cant_personal
      print(trabajos[0])


def buscar_trabajo(trabajos,buscar_des):
    for i in range(len(trabajos)):
        if trabajos[i].descripcion == buscar_des:
            print(trabajos[i])
            break
    else:
        print('\nNo se encuentran trabajos relacionados.')


def principal():
    areglos()
    ## vectores
    trabajos = []
    op = -1
    ## menu de opciones
    while op !=6:

        mostrar_menu()
        op = int(input('\n-Ingrese la opcion deseada: '))
        if op == 1:
            trabajos_cantidad = int(input('\n Ingrese la cantidad de trbajos:'))
            validar_trabajos_cantidad(trabajos_cantidad)
            generar_trabajos(trabajos,trabajos_cantidad)

        elif op == 2:
            ordenar(trabajos)

        elif op == 3:
            mas_personal(trabajos)


        elif op == 4:
            buscar_des = input("\nIngrese descripcion del trabajo: \n'Limpiar','Ordenar','Reparar','Mantenimiento','Gestionar stock': ").lower()
            buscar_trabajo(trabajos,buscar_des)

        elif op == 5:
            pass

        elif op == 6:
            print('\n Fin del proceso.\n')
            areglos()
## ejecucion y control

if __name__ == '__main__':
    principal()
