import os

def clear():
    os.system("cls")


while  True:
    opcion = int(input("1.farenheint a celsisu\n2.Celsiius a farenheint\n3.Kevin a celsius"
                "\n4.Celsius a kevin\n5.Kevin a farenheint\n6.farenheint a kevin\nIngrese un opcion: "))
    clear()
    medidas = ["Celsius","Farenheint","kevin"]
    if opcion == 0:
        print("Adios")
        break
    if opcion in [1,2,3,4,5,6]:
            valor = float(input("ingrses una cantidad: "))
            clear()

            if opcion == 1: #farenheint a celsius
                p = 0
                t = 1
                formula =(valor - 32)/1.8
                print(f"los {valor} {medidas[t]}  ""son " ,formula,f"{medidas[p]}")
                
            elif opcion == 2:#celsius a farenheirt
                p = 1
                t = 0
                formula = (valor* 1.8)+ 32
                print(f"los {valor} {medidas[t]}  ""son " ,formula,f"{medidas[p]}")

            elif opcion == 3: #kevin a celsius
                p = 2
                t = 0
                formula = valor - 273.15
                print(f"los {valor} {medidas[t]}  ""son " ,formula,f"{medidas[p]}")
            elif opcion == 4: #celsius a kevin
                p = 2
                t = 0
                formula = valor + 273.15
                print(f"los {valor} {medidas[t]}  ""son " ,formula,f"{medidas[p]}")

            elif opcion == 5: #kevin a farenheint
                p = 1
                t = 2
                formula = (valor - 273.15) * 1.8 + 32
                print(f"los {valor} {medidas[t]}  ""son " ,formula,f"{medidas[p]}")

            elif opcion == 6: #farenheint a kevin
                p = 2
                t = 1
                formula = (valor - 32) + 273.15
                print(f"los {valor} {medidas[t]}  ""son " ,formula,f"{medidas[p]}")

            input("Presione para volver")
      

    else:
        print("Elija una opcion valida")
        input("Presione para vorvel")

            
                
