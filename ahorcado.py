 # -*- coding: utf-8 -*-
import time
import sys
nombre=input ("¿Cual es tu nombre?")
print("Hola,"+nombre,"quiero jugar a un juego")
print("")
time.sleep(1)
print("Que empiece el juego")
print("Elige un tema antes de empezar")
print("-Ciudadania")
print("-Ibaiondo")
print("-Animales")
eleccion=input("Escribe tu eleccion ")
eleccion = eleccion.upper()
print("")
print("Has elegido "+eleccion,"Que empieze el juego")
print("")
if eleccion=="CIUDADANIA":
	print("persona que no tiene lo necesario para vivir o que lo tiene con escasez:")
	palabra='pobre'
	
elif eleccion=="IBAIONDO":
    print("Profesora que da programacion en clase:")
    palabra='belen'
elif eleccion=="ANIMALES":
    print("El mejor amigo del hombre es:")
    palabra='asier'
else:
	print("Esa eleccion no es válida")
	sys.exit(0)
	
time.sleep(0.5)
tupalabra= ''
vidas=5

contador= '5'
while vidas >0:
        contador=0
        fallos=0
        for letra in palabra:
                if letra in tupalabra:
                        print(letra,end="")
                        contador=contador+1
                else:
                        print("*",end="")
        tuletra=input("Introduce una letra:")
        tupalabra+=tuletra
        if contador==5:
                print("You win this time")
                time.sleep(50)
        if tuletra not in palabra:
                vidas-=1
                print("You failed")
                print("Tu tienes",+vidas,"vidas")
                fallos+=1
        if vidas ==4:
                        print(" ---------------------")
                        print(" |                     |")
                        print(" |                     |")       
                        print(" |                  -------")
                        print(" |                 | -  -  |")
                        print(" |                 |   o   |")
                        print(" |                  -------")
        if vidas ==3:
                        print(" |                  -------")
                        print(" |                 | -  -  |")
                        print(" |                 |   o   |")
                        print(" |                  -------")
                        print(" |                     |")
                        print(" |                     |")
                        print(" |                     |")
                        print(" |                     |")
        if vidas ==2:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | -  -  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / |   ");
            print(" |                 /   |   ");
            print(" |                /    |   ");
            print(" |                     |   ");
        if vidas ==1:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | -  -  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / | \ ");
            print(" |                  /  |   \ ");
            print(" |                 /   |     \ ")
            print(" |                     |   ");
        if vidas==0:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | X  X  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / | \\ ");
            print(" |                  /  |   \\ ");
            print(" |                 /   |     \\ ");
            print(" |                     |   ");
            print(" |                    / \\");
            print(" |                   /   \\  ");
            print(" |                  /     \\ ");     
        if vidas==0:
            print(" Has perdido");
            print(" Gracias por participar"); 
print("la palabra es : \n" ,palabra)			
for letra in palabra1:
                if letra in tupalabra:
                        print(letra,end="")
                        contador=contador+1
                else:
                        print("*",end="")
tuletra=input("Introduce una letra:")
tupalabra+=tuletra
if contador==5:
                print("You win this time")
                time.sleep(50)
if tuletra not in palabra1:
                vidas-=1
                print("You failed")
                print("Tu tienes",+vidas,"vidas")
                fallos+=1
if vidas ==4:
                        print(" ---------------------")
                        print(" |                     |")
                        print(" |                     |")       
                        print(" |                  -------")
                        print(" |                 | -  -  |")
                        print(" |                 |   o   |")
                        print(" |                  -------")
if vidas ==3:
                        print(" |                  -------")
                        print(" |                 | -  -  |")
                        print(" |                 |   o   |")
                        print(" |                  -------")
                        print(" |                     |")
                        print(" |                     |")
                        print(" |                     |")
                        print(" |                     |")
if vidas ==2:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | -  -  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / |   ");
            print(" |                 /   |   ");
            print(" |                /    |   ");
            print(" |                     |   ");
if vidas ==1:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | -  -  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / | \ ");
            print(" |                  /  |   \ ");
            print(" |                 /   |     \ ")
            print(" |                     |   ");
if vidas==0:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | X  X  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / | \\ ");
            print(" |                  /  |   \\ ");
            print(" |                 /   |     \\ ");
            print(" |                     |   ");
            print(" |                    / \\");
            print(" |                   /   \\  ");
            print(" |                  /     \\ ");     
if vidas==0:
            print(" Has perdido");
            print(" Gracias por participar"); 
print("la palabra es : \n" ,palabra)
for letra in palabra2:
                if letra in tupalabra:
                        print(letra,end="")
                        contador=contador+1
                else:
                        print("*",end="")
tuletra=input("Introduce una letra:")
tupalabra+=tuletra
if contador==5:
                print("You win this time")
                time.sleep(50)
if tuletra not in palabra2:
                vidas-=1
                print("You failed")
                print("Tu tienes",+vidas,"vidas")
                fallos+=1
if vidas ==4:
                        print(" ---------------------")
                        print(" |                     |")
                        print(" |                     |")       
                        print(" |                  -------")
                        print(" |                 | -  -  |")
                        print(" |                 |   o   |")
                        print(" |                  -------")
if vidas ==3:
                        print(" |                  -------")
                        print(" |                 | -  -  |")
                        print(" |                 |   o   |")
                        print(" |                  -------")
                        print(" |                     |")
                        print(" |                     |")
                        print(" |                     |")
                        print(" |                     |")
if vidas ==2:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | -  -  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / |   ");
            print(" |                 /   |   ");
            print(" |                /    |   ");
            print(" |                     |   ");
if vidas ==1:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | -  -  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / | \ ");
            print(" |                  /  |   \ ");
            print(" |                 /   |     \ ")
            print(" |                     |   ");
if vidas==0:
            print(" ---------------------");
            print(" |                     |");
            print(" |                     |");
            print(" |                  -------");
            print(" |                 | X  X  |");
            print(" |                 |   o   |");
            print(" |                  -------");
            print(" |                     |   ");
            print(" |                   / | \\ ");
            print(" |                  /  |   \\ ");
            print(" |                 /   |     \\ ");
            print(" |                     |   ");
            print(" |                    / \\");
            print(" |                   /   \\  ");
            print(" |                  /     \\ ");
print("la palabra es : \n" ,palabra)			
if vidas==0:
            print(" Has perdido");
            print(" Gracias por participar"); 
time.sleep(50)	
