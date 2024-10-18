#Print "Hello World"
#Write a program that prints "Hello World" on the screen.
#  Schreibe ein Programm, das "Hello world" auf dem Bildschirm ausgibt
print('Hello World')



#Create a program that asks the user for two numbers, adds them, and displays the result on the screen./ 
# Erstelle ein Programm, das den Benutzer nach zwei Zahlen fragt, sie addiert und das Ergebnis auf dem Bildschirm anzeigt.
number1=float(input('Enter the first number: '))
number2=float(input('Enter the second number: '))
result= number1 + number2
print('The result is:',result)



#Ask the user to enter two numbers and perform the following operations: addition, subtraction, multiplication, and division. Display each result separately.
# Fordere den Benutzer auf, zwei Zahlen einzugeben, und führe die folgenden Operationen durch: Addition, Subtraktion, Multiplikation und Division. Zeige jedes Ergebnis separat an.
num1=float(input('nter the first number: '))
num2=float(input('Enter the second number: '))
result1= num1 + num2
result2= num1-num2
result3= num1*num2
result4= num1/num2
print('The result of the addition is:',result1)
print('The result of the subtraction is: ',result2)
print('The result of the multiplication is: ',result3)
print('The result of the division is: ',result4)


#Ask the user for their first name and last name separately, then print their full name on a single line.
# Fordere den Benutzer auf, seinen Vor- und Nachnamen separat einzugeben, und gib dann den vollständigen Namen in einer Zeile aus.
Name=(input(' Enter the user name: '))
Surname=(input('Enter the user surname: '))
print('The User name is: ', Name,Surname)


#Longitud de un string

#Create a program that asks the user for a word or phrase and displays how many characters it has.
#  Erstelle ein Programm, das den Benutzer nach einem Wort oder Satz fragt und anzeigt, wie viele Zeichen er hat.

phrase=(input(' Enter your favorite phrase: '))
print('The phrase has', len(phrase), 'characters.')


