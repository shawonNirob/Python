//
saarc = ["Bangladesh", "Nepal", "India", "Pakistan", "Bhutan", "Sri Lanka", ]
print(saarc)
saarc.append("Afganistan")
print(saarc)
//
saarc = ["Bangladesh", "Nepal", "India", "Pakistan", "Bhutan", "Sri Lanka", ]
print(saarc)
saarc.append("Afganistan")
print(saarc)
saarc.sort()
print(saarc)

Number = [1,5,6,4,1,2,3,4,7,8,2,9]
Number.sort()
print(Number)
//
Number = [1,5,6,4,1,2,3,4,7,8,2,9]
Number.sort()
print(Number)
saarc.reverse()
print(saarc)
Number.reverse()
print(Number)
//
Number = [1,5,6,4,1,2,3,4,7,8,2,9]
Number.sort()
print(Number)
Number.reverse()
print(Number)
Number.insert(1, 25)
print(Number)
Number.remove(3)
print(Number)
item = 2589
if item in Number:
    Number.remove(item)
else:
    print(item, "not in list")
//
saarc = ["Bangladesh", "Nepal", "India", "Pakistan", "Bhutan", "Sri Lanka", ]
print(saarc)
item = saarc.pop()
print(item)
print(saarc)
item = saarc.pop(1)
print(item)
print(saarc)
//


saarc = ["Bangladesh", "Nepal", "India", "Pakistan", "Bhutan", "Sri Lanka", ]
print(saarc)
Number = [2,7,8,9,71,23,28,26]
saarc.extend(Number)
Number.extend(saarc)
print(Number)
print(saarc)

//
Number = [2,7,8,9,4,4,5,6,4,7,7,8,4,71,23,28,26]
item = Number.count(4)
item2 = Number.count(7)
print(item2)
//
Number = [2,7,8,9,4,4,5,6,4,7,7,8,4,71,23,28,26]
del(Number[0])
print(Number)
//
Number= []
for x in range(10):
    Number.append(x)
print(Number)

num=[2,3,4]
sum = Number +num
print(sum)
num1 =[3,4,5]
mal = num * 4
print(mal)

//
li =[1,2,3,4]
newli =[]
for i in li:
    newli.append(i*2)
print(newli)

newList = [ 2 * x for x in li]
print(newList)
//
integerList = [1,2,3,4,5,6,7,8,9,10,11]
evenList= []
for i in integerList:
    if i % 2 == 0:
        evenList.append(i)
print(evenList)
evenList= [i for i in integerList if i % 2 == 0]
print(evenList)
//
