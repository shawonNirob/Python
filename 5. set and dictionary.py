

A = { 1, 2, 5, 7, 8,9,10}
B = { 3, 4, 6, 7, 8}

C = A & B
print(C)
C = A | B
print(C)
C = A - B
print(C)
C = A ^ B
print(C)
C = B - A
print(C)
//
marks= [[40,60,50], [87,95,56],[25,36,58]]
print(marks[2][0])
//
marks= { 1:77, 2:86, 3:98, 4:65, 6:90, 5: 26, 8:98}
print("Marks of roll no 5 is ", marks[5])
//
marks= { "MSE10":77, "MSE11":86, "MAE12":98, "MSE14":65, "MSE13":90, "MSE49": 26, "MSE40":98}
print("Marks of roll no 10 on MSE is ", marks['MSE10'])
print(type(marks))
//
dt = {}
print(dt)
print(type(dt))
dt[1]='One'
dt[2]='two'
dt[3]='three'
print(dt)

//


marks= { "MSE10":77, "MSE11":86, "MAE12":98, "MSE14":65, "MSE13":90, "MSE49": 26, "MSE40":98}
print("Marks of roll no 10 on MSE is ", marks['MSE10'])
print(type(marks))
marks[(1,2,3)]="tuple"
print(marks)
marks[{1,2,3}]="set"
print(marks)
marks[[1,2,3]]="list"
print(marks)



//
marks= { "MSE10":{"Bangla":77, "English":86}, "MSE11": {"Bangla":98, "English":65}, "MSE12": {"Bangla":90, "English": 26}}
print(marks['MSE10']["Bangla"])
print(marks['MSE10'])
marks["MSE14"] = {"Bangla":85, "English":98}
print(marks)

//


bdDivisionInfo = {}
bdDivisionInfo["Barisal"] = {"District": 6, "Upazilla": 39, "Council": 333}
bdDivisionInfo["Chittagong"] = {"District": 11, "Upazilla": 97, "Council": 336}
bdDivisionInfo["Dhaka"] = {"District": 13, "Upazilla": 93, "Council": 1833}
bdDivisionInfo["Khulna"] = {"District": 10, "Upazilla": 59, "Council": 270}
bdDivisionInfo["Mymensingh"] = {"District": 4, "Upazilla": 34, "Council": 350}
bdDivisionInfo["Rajshahi"] = {"District": 8, "Upazilla": 70, "Council": 558}
bdDivisionInfo["Rangpur"] = {"District": 8, "Upazilla": 58, "Council": 536}
bdDivisionInfo["Sylhet"] = {"District": 4, "Upazilla": 38, "Council": 334}
print(bdDivisionInfo)
divisions =bdDivisionInfo.keys()
print(divisions)
for division in divisions:
    print(division, "UpaZilla", bdDivisionInfo[division]["Upazilla"])

//



bdDivisionInfo = {}
bdDivisionInfo["Barisal"] = {"District": 6, "Upazilla": 39, "Council": 333}
bdDivisionInfo["Chittagong"] = {"District": 11, "Upazilla": 97, "Council": 336}
bdDivisionInfo["Dhaka"] = {"District": 13, "Upazilla": 93, "Council": 1833}
bdDivisionInfo["Khulna"] = {"District": 10, "Upazilla": 59, "Council": 270}
bdDivisionInfo["Mymensingh"] = {"District": 4, "Upazilla": 34, "Council": 350}
bdDivisionInfo["Rajshahi"] = {"District": 8, "Upazilla": 70, "Council": 558}
bdDivisionInfo["Rangpur"] = {"District": 8, "Upazilla": 58, "Council": 536}
bdDivisionInfo["Sylhet"] = {"District": 4, "Upazilla": 38, "Council": 334}
print(bdDivisionInfo)
divisions =bdDivisionInfo.keys()
print(divisions)
for division in divisions:
    print(division, "UpaZilla", bdDivisionInfo[division]["Upazilla"])
for item in bdDivisionInfo:
    print(item)
for key in bdDivisionInfo:
    print(key,bdDivisionInfo[key])
for key, value in bdDivisionInfo.items():
    print(key, value)

//
bdDivisionInfo = {}
bdDivisionInfo["Barisal"] = {"District": 6, "Upazilla": 39, "Council": 333}
bdDivisionInfo["Chittagong"] = {"District": 11, "Upazilla": 97, "Council": 336}
bdDivisionInfo["Dhaka"] = {"District": 13, "Upazilla": 93, "Council": 1833}
bdDivisionInfo["Khulna"] = {"District": 10, "Upazilla": 59, "Council": 270}
bdDivisionInfo["Mymensingh"] = {"District": 4, "Upazilla": 34, "Council": 350}
bdDivisionInfo["Rajshahi"] = {"District": 8, "Upazilla": 70, "Council": 558}
bdDivisionInfo["Rangpur"] = {"District": 8, "Upazilla": 58, "Council": 536}
bdDivisionInfo["Sylhet"] = {"District": 4, "Upazilla": 38, "Council": 334}

item = 0
for division in bdDivisionInfo:
    print(division)
    item += bdDivisionInfo[division]["District"]
print(item)
//


bdDivisionInfo = {}
bdDivisionInfo["Barisal"] = {"District": 6, "Upazilla": 39, "Council": 333}
bdDivisionInfo["Chittagong"] = {"District": 11, "Upazilla": 97, "Council": 336}
bdDivisionInfo["Dhaka"] = {"District": 13, "Upazilla": 93, "Council": 1833}
bdDivisionInfo["Khulna"] = {"District": 10, "Upazilla": 59, "Council": 270}
bdDivisionInfo["Mymensingh"] = {"District": 4, "Upazilla": 34, "Council": 350}
bdDivisionInfo["Rajshahi"] = {"District": 8, "Upazilla": 70, "Council": 558}
bdDivisionInfo["Rangpur"] = {"District": 8, "Upazilla": 58, "Council": 536}
bdDivisionInfo["Sylhet"] = {"District": 4, "Upazilla": 38, "Council": 334}

District = 0
SubDistrict = 0
Council = 0
for division in bdDivisionInfo:
    print(division)
    District += bdDivisionInfo[division]["District"]
    SubDistrict += bdDivisionInfo[division]["Upazilla"]
    Council += bdDivisionInfo[division]["Council"]
print("Total", District, "District in Bangladesh")
print("Total", SubDistrict, "Sub District in Bangladesh")
print("Toral", Council, "Council in Bangladesh" )


//


print(bdDivisionInfo["Rangpur"]["Council"])

#

import turtle
import random
turtle.speed(0)
colors=["green","red", "yellow", "orange", "black", "purple", "blue"]
turtle.shape("turtle")

turtle.penup()
for i in range(1000):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtle.setposition(x,y)
    i = random.randint(0, len(colors)-1)
    turtle.dot(colors[i])
turtle.exitonclick()

#
import random
number = random.randint(1,1000)
attempts = 0
while True:
    guessNumber = input("Enter a guess number (between 1 to 1000) ")
    guessNumber = int(guessNumber)
    attempts += 1
    if guessNumber == number:
        print("Yes, your guess is correct")
        print("You tried", attempts, "time to find the correct number. Thank you !")
        break
    if guessNumber > number:
        print("Wrong! Please guess a smaller number")
    else:
        print("wrong! please guess a larger number")

#
