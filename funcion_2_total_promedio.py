def total_promedio():
    lista =[]
    contador = 0
    suma = 0
    total_numeros =input("cuantos numeros quieres en la lista :")
    total_numeros=int(total_numeros)
    for pos_num in range(total_numeros):
        contador = contador+1
        num =input("Ingresa el numero en de la posición " +str(contador) + ": ")
        lista.append(num)
        print(lista)
        num=int(num)
        suma = suma + num
    if command == "total":
        print(lista)
        print("EL total de los numeros en la lista es :"+ str(suma))
    elif command == "promedio":
        prom = suma/total_numeros
        print(lista)
        print("Promedio: "+ str(prom))
        
finished = False
while finished == False:
    print("Si lo que deseas es terminar la acción escribre Adios")
    command=input("En una lista de numeros quieres saber su total o el promedio?: ")
    if command == "total":
        total_promedio()
    elif command =="promedio":
        total_promedio()
    elif command == "Adios":
        finished = True
        print("Bye!!")
    else:
        print("Te equivocaste en la sintaxis vuelve a escribirlo")
    