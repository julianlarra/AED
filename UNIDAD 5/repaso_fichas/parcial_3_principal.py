'''
Una agencia de viajes necesita un programa para procesar los datos de los paseos que contratan sus clientes. Por
cada Paseo se tienen los siguientes datos: el número de identificación del paseo, el nombre del cliente que
contrata el paseo, el tipo de paseo (un valor del 0 al 19) y el monto total a abonar. Se desea almacenar la
información referida a los n paseos en un arreglo de registros de tipo Paseo (definir el tipo Paseo y cargar n por
teclado, validando que sea mayor a cero). Se pide desarrollar un programa en Python controlado por un menú de
opciones, que permita gestionar las siguientes tareas:
1. Cargar el arreglo pedido con los datos de los n paseos. Valide o asegure que los valores de cada campo sean
correctos. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
aleatorios). Pero al menos una debe programar. Pero si hace carga automática, todos los campos deben ser
cargados así (no combine ambas técnicas en la carga de un registro).
2. Mostrar todos los datos de todos los paseos, a razón de uno por línea, en un listado ordenado de menor a
mayor según el número de identificación del paseo. Al final del listado indique la suma de los montos a pagar
de todos los paseos que se mostraron.
3. Determinar el total que la agencia de viajes recaudó por cada tipo de paseo que fue contratado (20
acumuladores en total en un vector de acumulación). Muestre solo los valores de los acumuladores cuyos
valores finales sean mayores a un valor c que se carga por teclado.
4. Determinar si existe un paseo en el cual el nombre del cliente sea igual nom, siendo nom un valor que se carga
por teclado. Si existe, mostrar solo el número de identificación del paseo y el monto a pagar. Si no existe,
informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe
mostrar sólo el primero que encuentre.
'''

#import


import random
from parcial_3_modulo import Paseo



#funciones

def mostrar_menu():

    print('\n    Menu')
    print('\n1- Cargar datos.')
    print('2-Mostrar paseos ordenados de Men a May ')
    print('3-Recaudacion por tipo de paseo.')
    print('4-Buscar paseo para el cliente nombre "x".')
    print('5-Salir.')
#Punto 1 _______________________________________________________________________________________________________________
def validar_n():
    n=-1
    while n < 0:
        n= int(input('\nIngrese la cantidad de datos a cargar: '))
    return n

def cargar_datos(paseos,n):
    #crear datos num_identificacion,nombre_cliente,tipo_paseo,monto
    num_paseo = len(paseos)
    for i in range(n):
        num_identificacion= num_paseo + i
        nombre_cliente = random.choice(['Juan','Martin','Ana','Carolina'])
        nombre_cliente = nombre_cliente.lower()
        tipo_paseo = random.randint(0,19)
        monto = random.randint(100,2000)

        #cargar

        paseo =Paseo(num_identificacion,nombre_cliente,tipo_paseo,monto)

        #cargar vector
        paseos.append(paseo)

#Punto 2 ---------------------------------------------------------------------------------------------------------------

def mostrar_vectores(paseos):

    cant = len(paseos)
    sumador_monto =0
    #ordenar
    for piv in range(0,cant-1):
        for sig in range(piv+1,cant):
            if paseos[piv].num_identificacion > paseos[sig].num_identificacion:
                paseos[piv], paseos[sig] = paseos[sig] , paseos[piv]

    for i in range(cant):
        sumador_monto += paseos[i].monto
        print(paseos[i])
    print(' \n El monto total de los paseos es : $'+ str(sumador_monto))

#Punto 3----------------------------------------------------------------------------------------------------------------

def mostrar_recaudacion(paseos,bus_paseo):

    recaudacion = [0]*20
    sumador=0
    for i in range(len(paseos)):
        tipo_paseos = paseos[i].tipo_paseo
        recaudacion[tipo_paseos] += paseos[i].monto
    for p in range(len(recaudacion)):

        if recaudacion[p] > bus_paseo:
           print('El monto acumulado para el tipo de paseo '+ str(p)+' es de : $'+ str(recaudacion[p]))

#Punto 4________________________________________________________________________________________________________________
def buscar_nombre(paseos, nombre):
    existe = False
    for i in range(len(paseos)):
        if paseos[i].nombre_cliente == nombre:
            existe =True
            print('Para el nombre: '+str(nombre) +'\nEl numero de identificacion de paseo es: ' +str(paseos[i].num_identificacion) +' Con un importe de: $'+str( paseos[i].monto))
            break
    if existe == False:
        print('No se encontro ningun cliente con el nombre: '+str(nombre))

################# Principal#############################################################################################



def principal():
    #vector
    paseos=[]
    op = 0

    while op != 5:
        mostrar_menu()
        op = int(input('\nIngrese una opcion: '))

        if op == 1:
            n=validar_n()
            cargar_datos(paseos,n)

        elif op == 2:
            mostrar_vectores(paseos)

        elif op == 3:
            bus_paseo = int(input('\n Ingrese el monto minimo por categoria a filtrar: '))
            mostrar_recaudacion(paseos,bus_paseo)

        elif op == 4:
            nombre = input('Ingrese el nombre que desea buscar: ').lower()
            buscar_nombre(paseos,nombre)

        elif op == 5:
            print('\nConsulta finalizada.')



if __name__ == '__main__':
    principal()
