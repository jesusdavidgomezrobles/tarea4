#*********************************************AGENDA*****************************************#
from os import system
system('cls')
print("############### A continuacion encontrara las opciones disponibles de agendamiento ###############")

class Agenda:
	def __init__(self):
		self.contactos=[]
  
	def menu(self):
		print("-------------Bienbenido a su asistente de Agendamiento de contactos---------")
        
		menu=[
            
			['-----------Agenda peprsonal ----------'],
			['1. Añadir Contacto'],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
		]
      
		for x in range(5):
			print(menu[x][0])
            
         
 
		opcion=int(input("Ingrese una opcion:===> "))
		if opcion==1:
			self.añadir()
		if opcion==2:
			self.lista()
		if opcion==3:
			self.buscar()
		if opcion==4:
			self.editar()
		if opcion==5:
			print("........Agendamiento finalizado........")
			exit()
		self.menu()
       
 
	def añadir(self):
		print("--------------------------------------------------")
		print("|              Añadir nuevo contacto             |")
		print("--------------------------------------------------")
		nombre=input("Introduzca el nombre: ===> ")
		telefono=int(input("Introduzca el teléfono: ===> "))
		email=input("Introduzca el email: ===> ")
		self.contactos.append({'nombre':nombre,'telfono':telefono,'email':email})
		
	def lista(self):
		print("--------------------------------------------------")
		print("|                 Lista de contactos             |")
		print("--------------------------------------------------")
		if len(self.contactos) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])
		
 
	def buscar(self):
		print("--------------------------------------------------")
		print("|                Buscar  contactos               |")
		print("--------------------------------------------------")
		nombre=input("Introduzca el nombre del contacto: ===> ")
		for x in range(len(self.contactos)):
			if nombre == self.contactos[x]['nombre']:
				print("|____Datos del contacto____|")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telfono'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
		

	def editar(self):
		print("--------------------------------------------------")
		print("|                Editar contacto                 |")
		print("--------------------------------------------------")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			option=int(input("Introduzca la opción deseada: "))
			if option==1:
				nombre=input("Introduzca el nuevo nombre: ")
				self.contactos[data]['nombre']=nombre
			elif option==2:
				telfono=input("Introduzca el nuevo teléfono: ")
				self.contactos[data]['telfono']=telfono
			elif option==3:
				email=input("Introduzca el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True
 
agenda=Agenda()
agenda.menu()