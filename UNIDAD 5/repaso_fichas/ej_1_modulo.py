'''
el número de identificación del trabajo, la descripción o nombre del
mismo, el tipo de trabajo (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados), el importe a cobrar por
 ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar la información referida a
 los n trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).
'''

#definir registro

class Trabajo():
    #funcion constructora
    def __init__(self,num_trabajo,descripcion,tipo_trabajo,importe,cant_personal):


        self.num_trabajo = num_trabajo
        self.descripcion = descripcion
        self.tipo_trabajo = tipo_trabajo
        self.importe = importe
        self.cant_personal = cant_personal

    def __str__(self):

        res= 'Numero trabajo ' + str(self.num_trabajo) + ' Descripcion: ' +str(self.descripcion) + \
             ' Tipo de trabajo: ' +str(self.tipo_trabajo) + ' Importe: ' + str(self.importe) + ' Cantidad de personal: ' + str(self.cant_personal)


        return res
