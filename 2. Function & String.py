

import turtle

turtle.shape("turtle")
turtle.speed(0)
turtle.color("green")

def drawCircle(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)

counter = 0
while counter < 90:
    drawCircle(100)
    turtle.right(4)
    counter += 1
turtle.exitonclick()
//
import turtle

turtle.shape("turtle")
turtle.speed(0)
turtle.color("green")

def drawTriangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.right(120)

counter = 0
while counter < 90:
    drawTriangle(100)
    turtle.right(4)
    counter += 1
turtle.exitonclick()
//
def myfuc(y):
    print("y= ",y )
    print("x =", x)

x = 10
myfuc(x)
//

def myfuc(y=20):
    print("y = ",y )
    print("x = ", x)
x = 10
myfuc(x)
myfuc()
//

def myfuc(x, y=0, z=10):
    print("x =",x, "y=",y, "z=",z )
x = 10
y = 15
z = 17
myfuc(x,y,z)
myfuc(x,y)
myfuc(x)
//
def myfuc(x, z, y=10):
    print("x =",x, "y=",y, "z=",z )

myfuc(x=1,y=3,z=9)
a=5
b=8
myfuc(x=a,z=b)
a=23
b=34
c=90
myfuc(x=a, y=b, z=c)
//

def addNumbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

result = addNumbers([1,2,3,4,5,6,7,8,9])
print(result)
//

def list(li):
    li[0] =10
li = [1,2,3,4,5,6,7,8,9]
print("before function call", li)
list(li)
print("after function call", li)
//

list1=[1,2,3,4,5]
list2 = list1
print(list1)
print(list2)
list2[0] = 10
print(list1)
print(list2)
//
list = [1,2,3,4]
result = sum(list)
print(result)
//
country = "BANGLADESH"
for i in country:
    print(i)
    //
c = ['A', 'a', 'b']
print(c)
c[0]="B"
c = "BAngladesh"
print(c)
//
country1 = "BANGLA"
country2 = "desh"
country  = country1 + country2
print(country)
X = "50" + "50"
print(X)

//
country1 = "BANGLA"
country2 = "desh"
country  = country1 + country2
country.find("BANG")
country.find("desh")
country.find("LA")
country.find("Bengal")

//
country = "North Korea"
newCounrty = country.replace("North", "South")
print(country)
print(newCounrty)



title = "this is a test. this is a very important test for Engineering. this is the final test"
newTitle = title.replace("this", "This")
print(title)
print(newTitle)

//

import turtle
name= turtle.textinput("name", "What is your name?")
name= name.lower()
if name.startswith("mr"):
    print("Hello sir, How are you")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello madam, How are you")
else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)

turtle.exitonclick()




//

str = "a quick brown fox jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))


//
str = "Hello Test! 123 123. good"
upperChar = " "
lowerChar = " "
integer = " "
others = " "
for char in str:
    if char.isupper():
      upperChar = upperChar + char
    elif char.islower():
        lowerChar += char
    elif char.isnumeric():
        integer += char
    else:
        others += char
print(upperChar, lowerChar, integer, others)

//
str = input("Please enter a string: ")
upperChar = " "
lowerChar = " "
integer = " "
others = " "
for char in str:
    if char.isupper():
      upperChar = upperChar + char
    elif char.islower():
        lowerChar += char
    elif char.isnumeric():
        integer += char
    else:
        others += char
print(upperChar, lowerChar, integer, others)
//

str = input("Please enter a string: ")
strLength = len(str)
print(strLength)
newstr=" "
for i in range(0,strLength-1,2):
    newstr += str[i+1]
    newstr += str[i]
print(newstr)
//
str = input("Please enter a string: ")
strLength = len(str)
print(strLength)
newstr=" "
for i in range(0,strLength,2):
    newstr += str[i+1]
    newstr += str[i]
print(newstr)
//
while True:
    str = input("Please enter a string: ")
    strLength = len(str)
    print(strLength)
    palindrome = 0
    for i in range(0,strLength-1):
        if str[i] != str[(strLength-1)-i]:
            palindrome = 0
        else:
            palindrome = 1
    if palindrome == 1:
        print("palindrome")
    else:
        print("not palindrome")
//
while True:
    str = input("Please enter a string: ")
    strLength = len(str)
    print(strLength)
    palindrome = 0
    i =0
    while i != (strLength-1)-i:
        if str[i] != str[(strLength-1)-i]:
            palindrome = 0
        else:
            palindrome = 1
        i +=1
    if palindrome == 1:
        print("palindrome")
    else:
        print("not palindrome")
