
# DATA TYPES IN PYTHON

# working with Strings
name = "Bro"
print(type(name))
print("Hello" + name)
first_name = "Shubham"
last_name = "Patil"
full_name = first_name + " " + last_name
print(last_name)

# Working with integers and float
age = 23
age += 1
print("Your age is "+str(age))
print(age)
print(type(age))
height = 150.9
print(type(height))
print("My height is :" + str(height))

#Working with Bool
human = False
print("are you human? " + str(human))
print(type(human))
if(human):
    print("Yes I am human")
else:
    print("No I am not a human")

# Multiple assignments
full_name, age, height, human = "Shubham Patil", 25, 140.4 , True
print(full_name, age, height, human)
luffy = zoro = nami = sanji = 20
print(luffy , str(nami))

# String Methods
name = "Shubham Patil"
print(name)
print(len(name))
print(name.find('l'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isalpha())
print(name.replace("a", "u"))
print(name)
print(name.count("a"))
print(name*5)

# Type casting
a = 1
b = 3.9
c = "4"
#b = int(b)
print(b)
print(str(b)*3)
print(a + float(c))
print(a+b)

# User Inputs
full_name = input("What is your name: ")
age = int(input("What is your age? : "))
print("Hello", full_name)
print("You'll be "+str(age+1)+" in 1 year")
print(input("Enyer your inpur in string 1 :") + "Inline input is: "+ input("Enyer your inpur in string 2 :"))

import math
number = 143.3
num1 = 1.1
num2 = 2.2
num3 = 3.3
print(round(number))
print(math.floor(number))
print(math.ceil(number))
print(pow(number,3))
print(math.sqrt(number))
print(abs(number))
print(max(num1, num2, num3))
print(min(num1, num2, num3))
