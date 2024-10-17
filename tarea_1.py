#Imprimir "Hola Mundo"
#Escribe un programa que imprima "Hola Mundo" en la pantalla.
print('Hola Mundo')



#Crea un programa que solicite al usuario dos números, los sume y muestre el resultado en pantalla.
numero1=float(input('Ingrese el primer numero: '))
numero2=float(input('ingrese el segundo numero: '))
resultado= numero1 + numero2
print('el resultado es:',resultado)



#Pide al usuario que ingrese dos números y realiza las siguientes operaciones: suma, resta, multiplicación y división. Muestra cada resultado por separado.
num1=float(input('ingrese el primer valor: '))
num2=float(input('ingrese el segundo valor: '))
resultado1= num1 + num2
resultado2= num1-num2
resultado3= num1*num2
resultado4= num1/num2
print('el resultado de la sumaes:',resultado1)
print('el resuldado de la resta es: ',resultado2)
print('el resultado de la multiplicacion es: ',resultado3)
print('el resultado de division es: ',resultado4)


#Solicita al usuario su nombre y apellido por separado, luego imprime su nombre completo en una sola línea.
nombre=(input('Ingrese nombre del cliente: '))
apellido=(input('Ingrese apellido del cliente: '))
print('El cliente es: ', nombre,apellido)


#Longitud de un string

#Crea un programa que pida una palabra o frase al usuario y muestre cuántos caracteres tiene.

frase=(input('Ingrese su frase favorita: '))
print('La frase tiene', len(frase), 'caracteres.')


