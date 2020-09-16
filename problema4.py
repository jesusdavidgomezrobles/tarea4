from os import system
system('cls')
class Cuenta:
	
	def __init__(self,titular,cantidad):
		self.titular= input ("digite titular:::>")
		self.cantidad=float (input ("digite cantidad:::>"))
 
	
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
 
 

class CajaAhorro(Cuenta):

	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)
 
	
	def imprimir(self):
		print("----Cuenta de caja de ahorros-----")
		super().imprimir()
 

class PlazoFijo(Cuenta):

	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=float (input ("digite plazo:::>"))
		self.interes=float (input ("digite interes:::>"))
 
 

	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)
 
 
	
	def imprimir(self):
		print("-----Cuenta a plazo fijo------")
		super().imprimir()
		print("Plazo disponible : ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()
 
 

caja1=CajaAhorro("nnnn",000)
caja1.imprimir()
 
plazo1=PlazoFijo("nnnn",000,000,0.0)
plazo1.imprimir()