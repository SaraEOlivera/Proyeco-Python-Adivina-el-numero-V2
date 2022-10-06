#importar modulo
import random 

#funcion de bienvenida

def bienvenida(titulo, caracter = "*"):
  print(caracter * len(titulo))
  print(titulo)
  print(caracter * len(titulo))

#funcion principal

def adivinar_numero(x):
  print("¡Adiviná el número que genera la computadora! Tenes 3 intentos")

  numero_azar = random.randint(1, x)
  intento_usuario = 0
  jugadas = 3
  contador = 0
  while contador < jugadas:
    
    intento_usuario = int(input(f"Ingresa un número entre 1 y {x}: "))
    contador+=1
    if intento_usuario < numero_azar or intento_usuario > numero_azar:
      print("El numero que ingresaste es incorrecto")
    
    if jugadas == contador:
      print(f"¡Perdiste! El numero era {numero_azar}")
    
      
    if intento_usuario == numero_azar:
      print(f"¡Adivinaste! El numero era {numero_azar}")
      break
  

#Llamar funciones

bienvenida("¡Bienvenidos al juego!")
adivinar_numero(15)
