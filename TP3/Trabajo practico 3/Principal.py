'''

Una empresa de desarrollo de software de nuestra ciudad nos encarga un sistema para la gestión de Proyectos de Software.
 De cada proyecto se conoce:
*Número de proyecto
*Título
*Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
*Lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
*Cantidad de líneas de código
Se pide desarrollar un programa en dos módulos: uno de ellos debe contener la definición de la clase del regisstro
y las funciones básicas que permitan manejar un registro, y el otro debe contener el programa principal,
que debe estar controlado por un menú de opciones para permitir hacer lo siguiente:

1) Cargar proyectos: La generación de n proyectos de software cargados en un arreglo de registros. Para ello se pueden
generar los datos totalmente aleatorios o bien contar con proyectos completos precargados e ir seleccionando
aleatoriamente entre los mismos. Cada vez que selecciona esta opción durante la ejecución se agregarán datos al arreglo,
 sin eliminar los que ya estaban cargados. El número del proyecto no debe repetirse dentro del arreglo.

2) Listar proyectos: Mostrar todos los proyectos contenidos en el arreglo, pero ordenados alfabéticamente por título.
 Cada proyecto debe ocupar un máximo de dos líneas en pantalla y en lugar de mostrarse el identificador del lenguaje
 se debe mostrar su nombre.

3) Actualizar proyecto: Buscar si existe un proyecto con número x, siendo x un valor que se ingrese por teclado.
Si existe, se debe permitir modificar su cantidad de líneas de código y la fecha de actualización
(recuerde que debe cumplir con el formato dd-mm-yyyy). Si no existe, debe indicar con un mensaje.

4) Resumen por lenguaje: Calcular la cantidad de líneas de código acumuladas por lenguaje. Mostrar los resultados
 teniendo en cuenta que se debe visualizar el nombre del lenguaje en lugar del código.

5) Resumen por año:  Calcular la cantidad de proyectos por año de actualización, considerando los años entre 2000 y 2022
 inlcuidos ambos. Mostrar los resultados sólo de los años que tengan algún proyecto de software.

6) Filtrar lenguaje: Mostrar los proyectos de software ordenados por número de proyecto de manera ascendente,
del lenguaje ln, siendo ln un valor ingresado por teclado.

7) Productividad: A partir del resultado obtenido en el punto 5, determinar el año con mayor cantidad de proyectos
 actualizados, considerando mostrar todos los años si fuera más de uno con dicha cantidad.

'''

#----------------------------------------------------------------------------------------------------------------------
#importar librerias
from modulo_clases import *
import random

#----------------------------------------------------------------------------------------------------------------------
# Definicion de funciones

def mostrar_menu():
    print('| '*22,'\n')
    print('\tMenu:')
    print('1- Cargar proyectos')
    print('2- Listar proyectos')
    print('3- Actualizar proyecto')
    print('4- Resumen por lenguaje')
    print('5- Resumen por año')
    print('6- Filtrar lenguaje')
    print('7- Productividad')
    print('8- Salir del programa')

def validar_n():
    n = 0
    while n <= 0:
      n=int(input('Ingrese el numero de proyectos a gestionar : '))
    return n

# Punto 1_______________________________________________________________________________________________________________
def crear_titulo():
    primer_palabra = ['Medidor','Contador','Seleccionador','Registrador', 'Archivador', 'Calculador']
    segunda_palabra= [ 'unidades', 'autos','personal', 'proyectos', ]
    tercer_palabra = ['beta.', '2.0.', 'pro.', '3.0.', 'secret project.']
    titulo = random.choice(primer_palabra) +' de '+random.choice(segunda_palabra) + ' '+random.choice(tercer_palabra)
    return  titulo


def crear_fecha():
   dia = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
       '23','24','25','26','27','28','29','30','31']
   mes = ['01','02','03','04','05','06','07','08','09','10','11','12']

   anio = str(random.randint(2000,2022))

   fecha = random.choice(dia)+'/'+ random.choice(mes)+'/'+anio
   return fecha


def crear_lenjuaje():
    lenguaje = ['Python','Java','C++','Javascript','Shell','HTML','Ruby','Swift','C#','VB','Go']

    lenguaje_proyecto = random.choice(lenguaje)
    return lenguaje_proyecto


def crear_cant_lineas():
    lineas=str(random.randint(1,250))
    return lineas

def crear_proyectos(n,vec,):
    #generar tantos proyectos como n pide
    numero = len(vec)
    for i in range (n):
       numero +=1
       titulo = crear_titulo()
       fecha  = crear_fecha()
       lenguaje = crear_lenjuaje()
       cant_lineas = crear_cant_lineas()


    #referenciar los atributos

       proyecto = Proyecto(numero,titulo,fecha,lenguaje,cant_lineas)

    #almacenar proyectos
       vec.append(proyecto)

#Punto 2 _______________________________________________________________________________________________________________

def ordenar_proyectos(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i].titulo > vec[j].titulo:
                vec[i],vec[j] = vec[j],vec[i]

def mostrar_proyecto(vec):
    for i in vec:
        print(Proyecto.__str__(i))

# Punto 3 ______________________________________________________________________________________________________________

def modifica_cant_y_fecha(vec,i):
    vec[i].cant_lineas= input('Ingrese la nueva cantidad de lineas de codigo: ')
    print('Ingrese la fecha de modificacion en formato dd-mm-yyyy: ')
    dia='0'
    while len(dia)!=2 and dia <'1' or dia >'31':
      dia= input('Dia: ' )
    mes='0'
    while len(mes) !=2 and mes < '1' or mes >'12':
      mes=input('Mes: ')
    anio='0'
    while anio < '2000' or anio >'2022':
        anio=input('Año: ')
    fecha_act = dia+'/'+mes+'/'+anio
    vec[i].fecha = fecha_act

# Punto 4 ______________________________________________________________________________________________________________

def agrupar_por_lenguaje(vec,total_lineas_lenguajes):
    #recorrer proyectos y sumar lineas de codigo por lenguaje
    for i in range(len(vec)):
       r=vec[i].lenguaje
       for l in range(len(total_lineas_lenguajes)):
           if total_lineas_lenguajes[l][0] == r :
              total_lineas_lenguajes[l][1]  += int(vec[i].cant_lineas)

    # Imprimir lenguajes con mas de cero lineas de codigo
    for p in range(len(total_lineas_lenguajes)):
        if total_lineas_lenguajes[p][1] != 0:

         print('Lenguaje: '+ str(total_lineas_lenguajes[p][0]) + '. Cantidad de lineas de codigo: '+ str(total_lineas_lenguajes[p][1]) )


    # Poner contadores en cero para que cada vez que se ingresa al menu vuelva a calcular teniendo en cuenta las modificaciones
    for l in range(len(total_lineas_lenguajes)):

              total_lineas_lenguajes[l][1]  = 0

# Punto 5_______________________________________________________________________________________________________________

def resumen_por_anio(vec,proyectos_anios):
    cantidad_proyectos = 0
    ciclo=0
    for a in range(2000,2023):
        proyectos_anios.append([a,0])

        for i in range(len(vec)):

          if a == int(vec[i].fecha[-4:]):
            proyectos_anios[ciclo][1] +=1

        ciclo +=1
    for p in range(len(proyectos_anios)):
            if proyectos_anios[p][1] != 0:
                print('Para el año: ' +str(proyectos_anios[p][0]) + '. Se registran: ' +str(proyectos_anios[p][1]) + ' proyectos.')
    #borrar datos para no pisar futuras consultas
    proyectos_anios.clear()

# Punto 6 ______________________________________________________________________________________________________________
def filtrar_lenguaje(vec):
    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):
            if vec[i].numero > vec[j].numero:
                vec[i], vec[j] = vec[j], vec[i]


def filtrar_lenguajebis(vec):
    print('-Python-', '-Java-', '-C++-', '-Javascript-', '-Shell-', '-HTML-', '-Ruby-', '-Swift-', '-C#-', '-VB-',
          '-Go-')
    ln = str(input('Ingrese el lenguaje del cual quiere consultar los proyectos:'))
    t = 1
    for proyecto in vec:
        if proyecto.lenguaje == ln:
            if t == 1:
                print('Los proyectos correspondientes al lenguaje ', proyecto.lenguaje, 'son: ')
                t = 2
            print(proyecto)
        else:
            return print('No se encontraron proyectos de ese lenguaje')


########################################################################################################################
#                                               Script principal                                                        #
########################################################################################################################




def main():

    vec = []
    total_lineas_lenguaje = [['Python',0],['Java',0],['C++',0],['Javascript',0],['Shell',0],
                             ['HTML',0],['Ruby',0],['Swift',0],['C#',0],['VB',0],['Go',0]]
    proyectos_anios = []
    #titulo
    print('\n----- Gestor de Proyectos Aed 2022 -----  \n')

    #menu de 8 opciones con verificacion
    op = 0

    while op != 8 :
        mostrar_menu()
        #print('| '*22)
        op=int(input('\nIngrese el numero del menu que quiera acceder: \n'))

        #opcion 1 Cargar proyectos
        if op == 1:
            n=validar_n()
            crear_proyectos(n,vec)

        #ordenar proyectos alfabeticamente
        elif op == 2:
            ordenar_proyectos(vec)
            mostrar_proyecto(vec)

        #buscar y editar fecha y codigo
        elif op == 3:
            existe = False
            buscar = int(input('\nIngrese el numero del proyecto que desea consultar: '))
            for i in range(len(vec)):

                if vec[i].numero == buscar:
                    existe = True
                    print('\n El proyecto solicitado es:\n',vec[i])
                    if input('\nPresione "s" para modificar el codigo y la fecha, o cualquier tecla para salir:').lower() == "s":
                        modifica_cant_y_fecha(vec,i)
                        print('Lo cambios fueron modificados con exito, detalle:\n',vec[i])
            if existe == False:
                    print('El proyecto no existe.')
            existe = False

        # sumar cantidad de lineas por lenguaje
        elif op == 4:
            agrupar_por_lenguaje(vec,total_lineas_lenguaje)

        #resumen por anio
        elif op == 5:
            resumen_por_anio(vec,proyectos_anios)


        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            print("Sesion finalizada. ")
        else:
            print('\n\tIngrese una opcion valida, por favor.\n')





#----------------------------------------------------------------------------------------------------------------------
#Invocacion script principal
if __name__ == '__main__':
    main()
