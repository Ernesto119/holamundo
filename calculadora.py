import os #importacion para limpiar pantalla

def clear(): #Funcion para limpiar la pantalla en la ejecucion
    os.system("cls")

def suma(a, b):
    return a + b

def resta(a,b):
     return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
          return a / b
    else:
           return"No se puede dividir por cero"

def raiz(a):
     if a >= 0:   
        return a ** 0.5
     else:
        return "Error no se puede calcular la raíz cuadrada un numero negativo"


while True:
 
 print("calculadora")
 print("0.salir\n1.Suma\n4.Resta\n3.Multiplicacion\n4.Divison\n5.Raíz cuadrada")

 opcion = int(input("ingrese un numero: "))
 clear()
 
 if opcion == 0:
          print("Adios")
          break

 if opcion in [1,2,3,4]:
           a = float(input("\nPrimwer numero: "))
           b = float(input("Segundo numero: "))
          
           if opcion == 1:
                    oro = suma(a, b)
                    print("\nLa suma es: ", oro)
                    
           elif opcion == 2:
                    plata = resta(a,b)
                    print("\nLa resta es: ", plata)

           elif opcion == 3:
                    bronce = multiplicacion(a,b)
                    print("\nLa multiplicacion es: ", bronce)
               
           elif opcion == 4:        
                    madera = division(a,b)
                    print("\nLa division es: ", madera)

           input("Presioens para volver al menu")
           clear()

 elif opcion == 5:
       
       a = float(input("\nIngrese el numero: "))     
       papel = raiz(a)

       print("\nLa raíz del numero es: ", papel) 

       input("Presioens para volver al menu")
       clear()
 else: 
    print("Opcion invalida")
    input("Presioens para volver al menu")
