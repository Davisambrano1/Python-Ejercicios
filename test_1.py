# This file contains an exam in which I completed 5 exercises to test what I have learned in the first part of my course.

# Diese Datei enthält eine Prüfung, in der ich 5 Übungen durchgeführt habe, um das zu testen, was ich im ersten Teil meines Kurses gelernt habe.

#Write a program that asks the user for their name and greets them with a message like "Hello, [name]"
# Schreibe ein Programm, das den Benutzer nach seinem Namen fragt und ihn mit einer Nachricht wie "Hallo, [Name]" begrüßt.

Name =input('Please write name: ')
print('Hello,',Name)


# Create a program that asks the user for two integers, then prints their product (multiplication).
# Erstelle ein Programm, das den Benutzer nach zwei Ganzzahlen fragt und dann ihr Produkt (Multiplikation) ausgibt.

num1=int(input('Please write your first number '))
num2=int(input('Please write your second number '))
result= num1*num2
print('The result is:',result)


# Given a number entered by the user, write a program that prints whether the number is even or odd. Use the modulo operator %.
# Gegeben eine vom Benutzer eingegebene Zahl, schreibe ein Programm, das ausgibt, ob die Zahl gerade oder ungerade ist. Verwende den Modulo-Operator %
num=int(input('Write you number: '))
if num %2==0:
    print('The number is EVEN')
else:
    print('The number is ODD')


#Pregunta 4: Write a program that asks the user for a phrase, then prints that phrase in uppercase and lowercase (use the upper() and lower() methods of strings).
#Schreibe ein Programm, das den Benutzer nach einem Satz fragt und dann diesen Satz in Groß- und Kleinbuchstaben ausgibt (verwende die Methoden upper() und lower() von Strings).
phrase=input('Write your phrase: ')

print(phrase.upper()) #upper
print(phrase.lower())# lower
#Optional
print(phrase.capitalize())

#Pregunta 5: Crea un programa que pida al usuario dos palabras y las concatene con un espacio entre ellas. Luego, muestra el resultado en pantalla.
word1=input('write your first word: ')
word2=input('write your second word: ' )
print(word1 , word2)


