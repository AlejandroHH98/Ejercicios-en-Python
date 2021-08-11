#Creacion de lista para la captura de datos
shopping = []  #Creas una lista en blanco
contador = 0  #Variable para contar el numero de articulos o datos
total_item= input("¿Cuantos articulos quieres comprar?: ")
total_item= int(total_item)
for item_number in range(total_item): #Funcion loop para el conteo de articulos
    contador = contador + 1 #Realiza suma del acumulado
    item = input("Ingresa el articulo " + str(contador) + ": ")  #Captura del articulo que quieres comprar
    print("Articulos añadidos " + item) #Imprimte el articulo
    shopping.append(item) #Añade el articulo a la lista con el comando .append
    print(shopping) #Va imprimiento el valor del articulo 
print("Todos los articulos que ingresaste son " + str(shopping)) 
