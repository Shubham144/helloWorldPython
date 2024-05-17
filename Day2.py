
# String slicing

name = "Shubham Patil"
# [start:end:step]
print(name[2-7:12])
print(name[3:1:-1])
print(name[::-1])
slice = slice(0,-3,3) #Sbma
print(name[slice])

# If else and elseif
age = int(input("How old are you boiii?:"))
if age == 20:
    print("You are "+ str(age) + " years old means you're adult")
elif age <20& age>0:
    print("You are just a child.. get lost")
elif age > 20 :
    print("WOW, you can learn Python")
elif age<=0:
    print("what rubbis.. you are not yet born")
else:
    print("You are " + str(age) + " years old means yyou cannot vote today")

# Logical operators
temprature = int(input("What is the temparature today? "))
if temprature>30 or temprature<0:
    print("It's not good for you")
elif temprature<=30 and temprature>=0:
    print("It's suits you")
if not(temprature>30):
    print("it's not more than 30")
else:
    print("It's more than 30")

#While loop
name = None
while not name:
    name = str(input("What is your name?: "))
print("Hello " + name)

#For loop
for i in range(10):
    print(i)
for i in range(20,30):
    print(i)
name = "Shubham Patil of age 26"
for i in name:
    print(i)
import time
for i in range(10, -10, -1):
    print(i)
    if i == 0:
        print("HAPPY 0")
    elif i < 0:
        break
    time.sleep(1)
print("Happppppy NEWW YEAR")

# NESTED LOOP
rows = int(input("Enter rows:"))
cols = int(input("Enter cols:"))
symb = input("Enter symbol:")

for i in range(rows):
    for j in range(cols):
        print(symb, end="@")

phone_number = "123-123-123-23"
print(phone_number.replace("-",""))

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
