# funciones
import os
import io
import os.path
import pickle
import random
from modulo_tp_4 import Proyecto
# mostrar menu
########################################################################################################################
def mostrar_menu():
    print('{:^60}'.format('Menu de opciones'))
    print('\n\t1: Cargar el contenido del archivo en un vector.')
    print('\t2: Filtrar por tag.')
    print('\t3:')
    print('\t4:')
    print('\t5:')
    print('\t6:')
    print('\t7:')
    print('\t8: Salir del programa.\n')

#Punto 8
########################################################################################################################
def finalizar():
    print()
    print('{:^60}'.format('Programa finalizado.'))



#Punto 1
########################################################################################################################

# genera un registro por cada linea

def crear_registro(pipe,v,cont_rep):

    nombre_usuario      = str(pipe[0])
    repositorio         = str(pipe[1])
    fecha_actualizacion = str(pipe[3])
    lenguaje            = str(pipe[4])
    pre_like = pipe[5].split('k')
    likes               = float(pre_like[0])
    pre_tags = pipe[6].split(',')
    tags                = pre_tags
    url                 = str(pipe[7])

    proyecto = Proyecto(nombre_usuario,repositorio,fecha_actualizacion,lenguaje,likes,tags,url)

    #prueba de ordenamiento secuencial
    '''
    n = len(v)
    pos = n
    for i in range(n):
        if proyecto.repositorio < v[i].repositorio:
           pos = i
           break
    v[pos:pos] = [proyecto]
'''
    #prueba de ordenamiento binaria

    repetida = False
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
         c = (izq + der) // 2
         #si detecta repositorios iguales, activa la bandera repetida.
         if v[c].repositorio== proyecto.repositorio:
             pos = c
             repetida = True
             #cuenta la cantidad de lineas que se omiten por ser repetidas
             cont_rep +=1
             #print('igual',proyecto.repositorio)

             break
         if proyecto.repositorio < v[c].repositorio:
             der = c - 1
         else:
             izq = c + 1
         if izq > der:
             pos = izq
    # si la bandera es False, significa que el repositorio no esta repetido en el vector y lo agrega
    if repetida == False:
        v[pos:pos] = [proyecto]
    #si la bandera es True significa que el repositorio esta repetido, lo que lo omite y luego reestablece la bandera
    repetida = False

    return v,cont_rep


#crear vector a partir de archivo

def crear_vector(v1,fd):
    v=[]
    omitidos=0 #lineas omitidas por tener el campo lenguaje vacio
    cont_rep = 0 # contador de lineas con repositorio repetido

    #verificar que exista el archivo
    #si no existe informa y sale, para no generar error
    if not os.path.exists(fd):
        print('{:^60}'.format('El archivo '+str( fd) + ' no existe...'))
        print('|\/'*20)
        print()
        return

    #si existe abre el archivo y comienza a procesar la informacion
    print('\n Generando vector...\n')

    m = open("libros.csv", mode="rt", encoding="utf8")

    #omitir la primer linea que contiene el encabezado
    m.readline()


    # lee por lineas eliminando el salto de linea y descartando las lineas cuyo lenguaje este vacio
    for line in m:
        if line[-1] == '\n':
            line = line[:-1]
            pipe= line.split('|')
            if pipe[4] == '':
                #contabiliza la cantidad de lineas sin lenguaje
                omitidos +=1
                continue
            #genera de a un registro por linea
            v,cont_rep= crear_registro(pipe,v,cont_rep)

    #muestra el vector
    '''
    for i in v:
        print(i.to_string())
    '''
    #mostrar la cantidad de registros que se cargaron
    print('Se cargaron '+str(len(v))+' registros en el vector.')
    #mostrar cantidad de registros omitidos
    print('Se omitieron de la carga '+ str(omitidos+cont_rep)+' lineas:')
    print('\t'+str(omitidos)+ ' por tener el campo Lenguaje vacio.')
    print('\t'+str(cont_rep) +' por tener el campo Repositorio repetido.\n')
    print('|\/'*20)
    print()
    return v


    m.close()

       # print(line)


# Punto 2
########################################################################################################################

def  cantidad_estrellas(line):
    estrellas = 0
    if line.likes >= 0 and line.likes <= 10:
        estrellas = 1
    elif line.likes <= 20:
        estrellas = 2
    elif line.likes <= 30:
        estrellas = 3
    elif line.likes <= 40:
        estrellas =4
    elif line.likes > 40:
        estrellas =5
    return estrellas


#previos buscar tags

  #verificar que exista el vector
def existe_vector(v1):
    if len(v1) != 0:
        return True
    return False

#crear archivo y guardar
def guardar_archivo(obj,vacio):
    #Si se carga por primera ves el vector o se vuelve a realizar una nueva busqueda se borra lo anterior y carga encabezado
    if vacio :
        m = open('filtrotags.cvs', mode="wt", encoding="utf8")
        m.write('nombre_usuario|repositorio|fecha_actualizacion|lenguaje|estrellas|tags|url\n')
        m.close()
    #agregar al vector los registros filtrados
    m = open('filtrotags.cvs', mode="at", encoding="utf8")
    m.write(obj.nombre_usuario+'|'+obj.repositorio+'|'+obj.fecha_actualizacion+'|'+obj.lenguaje+'|'+str(obj.likes)+'k'+'|'+str(obj.tags)+'|'+obj.url+'\n'    )
    m.close()


def filtrar_tag(v1):
    coincidencia = False
    #verificar que exista el vector, retorna True si existe
    if existe_vector(v1):

        guardar= False
        #solicita tag a buscar
        tag = input('\nIngrese el Tag que busca:')
        #consulta si quiere guardar la consulta en archivo, True guardar

        vacio = True
        guardar= input('\nPresione "G" para guardar consulta en archivo.\nOtra para no guardar\n\tInsert:').lower()
        if guardar == 'g':
            guardar = True
            #vacio = True
        #recorrer el vector en busca de tag
        for obj in v1:
            if tag in obj.tags:
                coincidencia = True
                #convertir likes en estrellas
                estrella=cantidad_estrellas(obj)
                #mostrar nombre del repositorio, la fecha de actualización y  cantidad de estrellas.
                print('{:<30}'.format(obj.repositorio)+'{:<20}'.format(obj.fecha_actualizacion)+'{:<6}'.format(estrella)  )
                if guardar:
                    #guardar en archivo
                    guardar_archivo(obj,vacio)
                    vacio= False

        if not coincidencia:
            print('\n\tNo se encontraron coincidencias..\n')





    #si el vector no fue creado notifica en pantalla
    if existe_vector(v1) == False:
        print('El vector aun no fue creado.')


#prueba
'''
def mostrar_vector(v1):
   for i in v1:
        print(i.to_string())
'''



