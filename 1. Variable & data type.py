print("20")
v = 10
type(v)
v='10'
type(v)
v=10.34
type(v)
print("v")

number01=10
number02=5
result=number01+number02
print(result)
number01=16
number02=18
result=number01+number02
print(result)
number01

number01
type(number01)
s=""
print(s)
s=14
print(s)

a=1
b=2.543
c=a+b
print(c)
c="2"
print(b)
a=5/2
print(a)
a=5//2
print(a)
a=5**2
print(a)
a=5 % 2
print(a)

a=3; b=4.5; c="Hello"
print(a, b, c, "world")

c=3
type(c)

name=input("what is your name? ")
print("welcome to python", name, "!")


number01=input("please type a integer and press enter: ")
number02=input("please type a another integer and press enter: ")
print("number01+number02= ",number01+number02 )


number01=input("please type a integer and press enter: ")
number02=input("please type a another integer and press enter: ")
number01=int(number01)
number02=int(number02)
print("number01 + number02=", number01 + number02)

//From cmd
>>> 2 ==3
False
>>> 3>3
False
>>> 3!=3
False
>>> 3<=3
True
>>> "34" == "34"
True
>>> "34" =="23"
False
>>> "bangladesh" =="Bangladesh"
False
>>>

>>> myMoney>=rickshaFare
True
>>> myMoney=rickshaFare
>>> myMoney>=rickshaFare
True
>>> myMoney<=rickshaFare
True
>>> myMoney<=rickshaFare
True
>>> myMoney>=rickshaFare
True
>>> myMoney=<rickshaFare
  File "<stdin>", line 1
    myMoney=<rickshaFare
            ^
SyntaxError: invalid syntax
>>> myMoney<=rickshaFare
True
>>> not True
False
>>> not False
True
>>> not(not False)
False
>>>
//


numbers=[2, 4 ,5 ,6, 7,7,7,8,9,0]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[9])
//
saarc=['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Nepal', 'Bhutan', 'Afghanistan', 'Maldiv' ]
print(saarc)
print(saarc[2])
print(saarc[3])
print(saarc[4])
print(saarc[0])

'Bangladesh' in saarc
'India' in saarc
'Russia' in saarc
//
saarc=['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Nepal', 'Bhutan', 'Afghanistan', 'Maldiv' ]

terminate= False
while not terminate:
    country = input('Please enter a country name: ')
    if country in saarc:
        print(country, 'is in saarc list')
    else:
        print(country, 'is not in saarc list')
        break
    print('program terminated')
//
while True:
    marks =input('please enter your marks(>=100 to exit)')
    marks=int(marks)

    if marks >= 100:
        print('incorrect marks')
        break
    elif marks >= 80:
        print('A+')
    elif marks >= 70:
        print('A')
    elif marks >= 60:
        print('A-')
    elif marks >= 50:
        print('B')
    elif marks >= 40:
        print('C')
    elif marks >= 33:
        print('C')
    else:
        print('Fail')
        break

//
while True:
    numbers =input('please enter a rtional number')
    numbers =int(numbers)


    if numbers >0:
        print(numbers, 'is positive integer')
    elif numbers == 0:
        print(numbers, 'is zero')
        exit(0)
    else:
        print(numbers,"is negetive integers")
//
while True:
    numbers =input('please enter a rtional number')
    numbers =int(numbers)


    if numbers % 2 == 0:
        print(numbers, 'is even')

    else:
        print(numbers,"is odd")
//
while True:
    numbers =input('please enter number ')
    numbers =int(numbers)
    numbers1 = input('please enter number1 ')
    numbers1 = int(numbers1)
    numbers2= input('please enter a number2 ')
    numbers2 = int(numbers2)


    if numbers > numbers1:
        max=numbers
    else:
        max = numbers1
    if numbers2  > max:
        max = numbers2

    print(max, "is the maximum number")
//
while True:
    year = input('please enter a year ')
    year = int(year)
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
                print("Yes")
            else:
                print('No')
        else:
            print('Yes')
    else:
        print("No")

//
while True:
    year = input('please enter a year ')
    year = int(year)
    if year % 4 == 0 and year % 100 !=0:
        print("yes")
    elif year % 100 == 0 and year % 400 ==0:
        print("yes")
    else:
        print("No")
//

import turtle
turtle.shape("turtle")
turtle.speed(2)

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()

//

import turtle
turtle.shape("turtle")
turtle.speed(2)

for _ in range(3):
    turtle.forward(100)
    turtle.right(120)

turtle.exitonclick()

//

result = 0
for i in range(1, 50):
    result += i
print(result)

//

number = [4 ,5,6,7,8,9,12,34,23,65,76,3,7,8,9]
maxNumber = number[0]
for n in number:
    if n>maxNumber:
        maxNumber = n
print(maxNumber)
print(len(number))

//
result=0
for i in range(5,101,5):
    result += i
print(result)
//

saarc=['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Nepal', 'Bhutan', 'Afghanistan', 'Maldiv' ]
for country in saarc:
    print(country, "in the list of saarc")
//
list1 = list(range(20))
print(list1)//

//
i = 0
while i < 10:
    print(i)
    i += 1
//
i = -10
while i <= 0:
    print(i)
    i +=1
    //
n = input("Please insert a number ")
n = int(n)

i = 1
while i<=10:
    print(i,"x",n, "=", i*n  )
    i += 1
//
import turtle

turtle.color("red")
turtle.speed(0)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter +=1

turtle.exitonclick()

//
import turtle

turtle.color("red")
turtle.speed(1)
turtle.penup()

height = 5
width = 5

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()
//
import turtle
turtle.shape("turtle")
turtle.color("red")
turtle.speed(2)
turtle.penup()

row = 7
column = 8
for _ in range(row):
    for _ in range(column):
        turtle.dot()
        turtle.forward(50)
    turtle.backward(50*column)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)

turtle.exitonclick()
//
while True:
    n = input("Please enter a number(0 to exit) ")
    n = int(n)

    if n == 0:
        print("0 is not acceptable ")
        break
    elif n < 0:
        print("Number is negative integer")
        continue
    else:
        print("squre is ", n*n)
//


terminate = False
while not terminate:
    n1=input("Please enter a number ")
    n1=int(n1)
    n2=input("Please enter a another number ")
    n2=int(n2)

    while True:
        operation= input("Please enter add/sub or quit exit to ")

        if operation == "quit":
            print("code exit")
            terminate = True
            break
        if operation == 'add':
            print("add= ", n1+n2)
            break
        if operation == 'sub':
            print("sub= ", n1-n2)
            break
//
