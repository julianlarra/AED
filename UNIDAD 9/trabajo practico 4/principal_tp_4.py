import os
import io
import os.path
import pickle
import random
from modulo_tp_4 import Proyecto
from funciones_tp_4 import *


#m = open("libros.csv", mode="rt", encoding="utf8")
def principal():

    fd = 'libros.csv'
    v1 = []
    fd2= 'popular.dat'
    mas_popular = None
    v2 = []
    #menu
    op = 0
    print('|\/'*20)
    print()
    print('{:^60}'.format('Gestión de Proyectos [v2.0]'))
    print()

    while op != 8:
        mostrar_menu()
        print('-'*60)
        op = int(input(' Ingrese la opcion deseada: '))
        print('-'*60)
        #print('|\/'*20)
        #print()

        print()

        if op == 1:
          v1=crear_vector(v1,fd)

        elif op == 2:
            #mostrar_vector(v1) #para prueba
            #print("Filtrando por tag")
            filtrar_tag(v1)
        elif op == 3:
            # Mostrar l ordenado por lenguaje de mayor a menor
            ordenar_lenguaje(v1)

        elif op == 4:
             mas_popular=popularidad_mes(v1)

        elif op == 5:
             buscar_repo(v1)

        elif op == 6:

            if mas_popular == None:
                print('\n\tDebe generar la matriz en el punto 4.')
            guardar_populares(mas_popular,v1,fd2,v2)

        elif op == 7:
            mostrar_archivo(fd2)

        elif op == 8:
            finalizar()

#principal



if __name__ == '__main__':
    principal()
