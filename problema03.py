# creamos la clase banco
class Banco:
	# inicializamos
	def _init_(self):
		self.cliente1=Cliente("")
		self.cliente2=Cliente("")
		self.cliente3=Cliente("")
 
	# función para operar
	def operacion(self):
		self.cliente1.depositar(0)
		self.cliente2.depositar(0)
		self.cliente3.depositar(0)
		self.cliente1.extraer(0)
 
	# función para obtener los depósitos totales
	def depositos(self):
		total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
 
 
 
# creamos la clase Cliente
class Cliente:
	# inicializamos
	def _init_(self,nombre):
		self.nombre= input ("digite titular:::>")
		self.cantidad=float (input ("digite cantidad:::>"))
 
	# función para depositar dinero
	def depositar(self,cantidad):
		self.cantidad+=cantidad
 
	# función para extraer dinero
	def extraer(self,cantidad):
		self.cantidad-=cantidad
 
	# función para obtener el total de dinero
	def devolver_cantidad(self):
		return self.cantidad
 
	# función para imprimir los datos del cliente
	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
 
 
# bloque principal
banco1=Banco()
banco1.operacion()
banco1.depositos()