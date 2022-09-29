
class Proyecto():

    def __init__(self,nombre_usuario,repositorio,fecha_actualizacion,lenguaje,likes,tags,url):


        self.nombre_usuario = nombre_usuario
        self.repositorio =  repositorio
        self.fecha_actualizacion = fecha_actualizacion
        self.lenguaje =  lenguaje
        self.likes =  likes
        self.tags = tags
        self.url = url

    def to_string(self):
        r= ''
        r += '{:<74}'.format('Repositorio: '+str(self.repositorio))
        r += '{:<44}'.format(' | Nombre de usuario: '+str(self.nombre_usuario))
        #r += '{:<25}'.format('Numero de repositorio: '+str(self.repositorio))
        r += '{:<40}'.format(' | Fecha de actualizacion: '+str(self.fecha_actualizacion))
        r += '{:<30}'.format(' | Lenguaje: '+str(self.lenguaje))
        r += '{:<25}'.format(' | Likes: '+str(self.likes))
        r += '{:<75}'.format(' | Url: '+str(self.url))
        r += '{:<25}'.format(' | Tags: '+str(self.tags))


        return r



#definir funcion  para el punto 6

class Matriz():

    def __init__(self,mes,estrella,cantidad):


        self.mes      = mes
        self.estrella = estrella
        self.cantidad = cantidad

    def __str__(self):
        r= ' Mes: '+str(self.mes)+ ' Estrella: '+str(self.estrella)+ ' Cantidad: ' +str(self.cantidad)

        return r
