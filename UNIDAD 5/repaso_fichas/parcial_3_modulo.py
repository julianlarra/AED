''' el número de identificación del paseo, el nombre del cliente que
contrata el paseo, el tipo de paseo (un valor del 0 al 19) y el monto total a abonar. Se desea almacenar la
información referida a los n paseos en un arreglo de registros de tipo Paseo (definir el tipo Paseo y cargar n por
teclado, validando que sea mayor a cero).'''

class Paseo():
    #funcion constructora
    def __init__(self,num_identificacion,nombre_cliente,tipo_paseo,monto):


        self.num_identificacion = num_identificacion
        self.nombre_cliente = nombre_cliente
        self.tipo_paseo = tipo_paseo
        self.monto = monto
    def __str__(self):

        res = 'numero identificacion paseo: ' + str(self.num_identificacion)+ ' nombre cliente: '+ str(self.nombre_cliente) \
              +' tipo paseo: ' + str(self.tipo_paseo) + ' monto paseo: ' + str(self.monto)

        return res
