# funciones
import os
import io
import os.path
import pickle
import random
from modulo_tp_4 import Proyecto, Matriz

import datetime
# mostrar menu
########################################################################################################################
def mostrar_menu():
    print('{:^60}'.format('Menu de opciones'))
    print('\n\t1: Cargar el contenido del archivo en un vector.')
    print('\t2: Filtrar por tag.')
    print('\t3: Determinar la cantidad de proyectos por cada lenguaje.')
    print('\t4: Mostrar matriz ordenada por mes/estrella. buscar mes.')
    print('\t5: Buscar por repositorio y actualizar Url.')
    print('\t6: Guardar populares en archivo binario.')
    print('\t7: Mostrar archivo binario.')
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
    m.write(obj.nombre_usuario+'|'+obj.repositorio+'|'+obj.fecha_actualizacion+'|'+obj.lenguaje+'|'+str(obj.likes)+'k'+'|'+','.join(obj.tags)+'|'+obj.url+'\n'    )
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
        print('\n\tEl vector aun no fue creado.\n')


# Punto3
########################################################################################################################




def ordenar_lenguaje(v1):


  #comprobar que el vector este generado

  if not existe_vector(v1):
      print('\n\tEl vector aun no fue creado.\n')
  lenguajes = []
  #recorrer el vector en busca de los lenguajes y los deja en un vector agrupado por lenguajes
  for obj in v1:
      leng=obj.lenguaje

      n = len(lenguajes)
      pos = n
      izq, der = 0, n-1
      while izq <= der:
          c = (izq + der) // 2
          if lenguajes[c] == leng:
              pos = c
              break
          if leng < lenguajes[c]:
             der = c - 1
          else:
             izq = c + 1
          if izq > der:
             pos = izq
      lenguajes[pos:pos] = [leng]


  cant_len = None

  #recorre el vector y se detiene en cada lenguaje
  #for l in range(len(lenguajes)):

      #posicion
  pos = 0
      #si la matriz esta vacia carga el primer elemento
  if cant_len == None:
     cant_len =[]
  sig = pos+1
      #contador de repeticiones iniciado en 1

  while sig < len(lenguajes):
          counter = 1
          #print(pos, sig)
          while lenguajes[pos] == lenguajes[sig] :
              counter +=1
              pos +=1
              sig = pos+1
              if sig == len(lenguajes):
                  break
          cant_len.append([lenguajes[pos],counter])
          #print(cant_len)
          #print('pos',pos,sig)
          pos +=1
          sig =pos+1
  #print(cant_len)


  #ordena y mostrar ordenado


  for i in range(len(cant_len)-1):
      for j in range(i+1,len(cant_len)):
          if cant_len[i][1] < cant_len[j][1]:
                cant_len[i],cant_len[j] = cant_len[j],cant_len[i]

  if existe_vector(v1):
  #mostrar uno por renglon
      print('\n|\tLenguaje      Cantidad|\n')
      for i in cant_len:
          lengu = i[0]
          cantidad = i[1]

          print('|''{:<20}'.format(lengu)+'{:<5}'.format(cantidad)+'|')




#Punto 4
########################################################################################################################


def meses(obj,v1):
    fecha= obj.fecha_actualizacion.split('-')
    mes = int(fecha[1])
    return mes

def popularidad_mes(v1):
   existe=False
   #verificar si se creo el vector
   if  existe_vector(v1):
       existe = True


       #definir matriz filas mes del 1 al 12,
       popular = [[0]*5 for e in range(12)]

       #referencia primer casillero[x] llama fila mes 0 = mes 1 = enero al 11 = 12 = diciembre
       #segundo casillero [y] llama estrellas [0] = 1 estrella al [4] = 5 estrellas.
       #print(popular)
       #print(popular[1])

       #recorrer el vector y completar la matris
       for obj in v1:
           #extrae el mes de cada registro del descuenta 1  y lo disponibiliza como int para buscar por fila  en la matriz
           mes= meses(obj,v1)-1

           #filtramos los likes convertimos a estrellas reutilizando la funcion cant_estrellas()
           # descontamos uno para buscar en el indice de la matriz

           estrellas = cantidad_estrellas(obj)-1
           #print(estrellas)

           #contabilizamos las coincidencias para cada mes segun las estrellas
           popular[mes][estrellas]+=1

       #mostrae matriz como tabla
       print('\n\t Tabla de meses y estrellas, con cantidad de proyectos.')
       primer_vuelta = True
       for i in range(len(popular)):
           if  primer_vuelta:
               print('\n|{:^6}'.format('MES')+'|{:^13}'.format('1 ESTRELLA')+'|{:^13}'.format('2 ESTRELLAS')+'|{:^13}'.format('3 ESTRELLAS')+'|{:^13}'.format('4 ESTRELLAS')+'|{:^13}|'.format('5 ESTRELLAS'))
               primer_vuelta = False
           print('|{:^6}'.format(i+1)+'|{:^13}'.format(popular[i][0])+'|{:^13}'.format(popular[i][1])+'|{:^13}'.format(popular[i][2])+'|{:^13}'.format(popular[i][3])+'|{:^13}|'.format(popular[i][4]))


        #calcular sumatoria de proyectos por mes
       consulta= input('\n\tPara consultar el total de proyectos de un mes ingrese "S" \n\t o ingrese "N" para salir.\n\tInsert:').lower()

       while consulta != 'n':
         if consulta == 's':
             sumar_mes= input('\nIngrese el numero: \n\t1  = Enero \n\t2  = febrero \n\t3  = febrero\n\t4  = Marzo \n\t5  = Abril'
                              ' \n\t6  = Junio \n\t7  = Julio \n\t8  = Agosto \n\t9  = Septiembre \n\t10 = Octubre \n\t11 = Noviembre \n\t12 = Diciembre \n\t Numero:    ')

             #recoremos la fila y sumamos
             sumatoria = 0
             sumar_mes = int(sumar_mes)-1 #adaptamos al indice
             for m in range(5):
                 sumatoria += popular[sumar_mes][m]

             print('En el mes '+str(sumar_mes+1)+', se actualizaron '+str(sumatoria)+' proyectos.')

         consulta= input('\n\t Para realizar otra consulta\n\t Si = "S" / No = "N" \n\t Insert: ').lower()

   if existe == False:
      print('\n\tEl vector aun no fue creado.\n')

   else:
         return popular
#Punto 5
########################################################################################################################



def buscar_repo(v1):

  #verificar si se genero el vectos
   existe=False

   if  existe_vector(v1):
       existe = True

       encontrado = False
       rep= input('\n\t Ingrese el repositorio que desea actualizar\n\t Rep: ')
       for r in v1:

          if rep == r.repositorio:
              encontrado = True
              print('\n\tSe muestran los datos del repositorio buscado:\n ')
              print(r.to_string())
              r.url = input('\n\tIngrese el nuevo Url: ')
              r.fecha_actualizacion = datetime.datetime.now().strftime('%Y-%m-%d')
              print('\n\tRegistro modificado con exito.\n')
              print(r.to_string())
              break
       if encontrado == False:
           print('\n\tLa busqueda no produjo coincidencias.')
   if not existe:
       print('\n\tEl vector aun no fue creado.\n')

#Punto 6
########################################################################################################################

def guardar_populares(mas_popular,v1,fd2,v2):
     #verificar si se genero el vectos
   existe=False

   if  existe_vector(v1):
       existe = True


       if mas_popular != None:

           #recorrer la matriz
           for fila in range(len(mas_popular)):
               for columna in range(len(mas_popular[fila])):
                   if mas_popular[fila][columna] > 0:
                       mes      = fila
                       estrella = columna
                       cantidad = mas_popular[fila][columna]
                       matriz = Matriz(mes,estrella,cantidad)
                       v2.append(matriz)

       m= open(fd2,'wb')
       for dat in v2:
             pickle.dump(dat,m)

       m.close()
       print('\n\tArchivo guardado.')
   if not existe:
       print('\n\tEl vector aun no fue creado.\n')


#Punto 7
########################################################################################################################

def mostrar_archivo(fd2):
    #crear matriz plantilla
    popular = [[0]*5 for e in range(12)]
    #comprobar que el archivo existe
    if not os.path.exists(fd2):
        print('\n\tEl archivo ',fd2,' no existe.\n')
        return

    #abrir y manejar el archivo
    m= open(fd2,'rb')

    t= os.path.getsize(fd2)
    while m.tell() < t:
        dat = pickle.load(m) #extraer los datos
        popular[dat.mes][dat.estrella] = dat.cantidad
       # print(dat.mes,dat.estrella,dat.cantidad)

    m.close()

    #mostrar matriz como tabla
    print('\n\t Tabla de meses y estrellas, con cantidad de proyectos.')
    primer_vuelta = True
    for i in range(len(popular)):
           if  primer_vuelta:
               print('\n|{:^6}'.format('MES')+'|{:^13}'.format('1 ESTRELLA')+'|{:^13}'.format('2 ESTRELLAS')+'|{:^13}'.format('3 ESTRELLAS')+'|{:^13}'.format('4 ESTRELLAS')+'|{:^13}|'.format('5 ESTRELLAS'))
               primer_vuelta = False
           print('|{:^6}'.format(i+1)+'|{:^13}'.format(popular[i][0])+'|{:^13}'.format(popular[i][1])+'|{:^13}'.format(popular[i][2])+'|{:^13}'.format(popular[i][3])+'|{:^13}|'.format(popular[i][4]))




#prueba
'''
def mostrar_vector(v1):
   for i in v1:
        print(i.to_string())
'''



