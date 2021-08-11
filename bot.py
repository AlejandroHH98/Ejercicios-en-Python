#Presentacion del bot
print("Hola soy erick y soy tu bot personal")
#Variable que añade el nombre del usuario
users_name= input("Ya que me presenté, ¿Cuál es tu nombre? ")
print("Hola " + users_name)
print("Se hacer diferentes cosas, por ejemplo sumar")
#Se pide los dos numeros necesarios para capturarlos como entrada
input1=input("Dime el primer numero ")
input2=input("Dime tu secundo numero ")
input3=input("Dime el tercer numero ")
#Se añaden dos variables para analizarlos como numeros enteros 
number1 = int(input1) #input1 será el primer numero entero
number2 = int(input2) #input2 seá el segundo numero entero
number3 = int(input3)
#Se realiza la operacion matemática 
suma = number1 + number2 + number3
#Se necesita trasnformar el resultado numero a variable de texto utilizando el comando str
output = str(suma)
#Mostramos el resultado : primero el nombre del usuario luego number1+numer2 = suma 
print(input1 + "+" + input2 + "+" + input3 + "=" + output)
print("También puedo decirte el área de un cuadrado, por ejemplo supondré que un lado el cuadrado mide lo mismo que el primer 1 en centimetros")
#Conseguir el área de un cuadrado como LadoxLado o Lado^2
area_of_square = number1*number1
#output2 se considera como el resultado de la área transformado a string
output2= str(area_of_square)
print("El area del cuadro considerando uno de sus lados como el valor del primer numero en cm es " + output2)
print ("Tambien puedo restar numeros, tomaré el segundo y el tercer numero y los restaré")
#Se realiza la resta
resta = number2 - number3
#output 3 se considera como la resta transfromada en string
output3=str(resta)
print(input2 + "-" + input3 + "="+ output3)
