#*******************************ESTUDIANTES*****************************#

from os import system
system('cls')


class Alumno():
    
    nombre = ""
    nota = ""

    def inicializar(self):
        self.nombre = input("digite nombre: => ")
        self.nota = float(input("digite su nota: => "))
    
    def imprimir(self):
        print(f"nombre : {self.nombre}")
        print(f"nombre : {self.nota}")
    
    def resultado(self):
        if self.nota >= 3:
            print("Aprobado")
        else:
            print("reprobado")

def main():
    alumno1=Alumno()
    alumno2=Alumno()
    alumno1.inicializar()
    alumno1.imprimir()
    alumno1.resultado()
    alumno2.inicializar()
    alumno2.imprimir()
    alumno2.resultado()

if __name__ == "_main_":
    pass
main()