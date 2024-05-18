
#Dictionaries
countries = {'India':'New Delhi',
             'USA':'Washington dc',
             'China':'Beiging'}
print(countries['India'])
print(countries.keys())
print(countries.values())
print(countries.items())
print(countries.get('Germany'))
countries.update({'Germany':'Berlin'})
countries.update({'USA':'LV'})
countries.pop('China')
for i,k in countries.items():
    print(i, k)
countries.clear()
#Indexing
name = "Shubham Patil"
print(name[2:-1])
print(name[-1])

#Functions
def hello(name):
    print("Hello world"+ name)
hello("Shubham")
student_1= ("Shubham", "Patil", 26,  150.3, "male")
student_2= ("Sonali", "Kangralkar", 27,  160.3, "female")
def students(list_values):
    print("First Name:" + list_values[0] + " Last Name: " + list_values[1] )
    print("Age: " + str(list_values[2]) + "yrs Height: " + str(list_values[3]) + "cm")
    print("Student is " + list_values[4])
students(student_1)
students(student_2)

#Return
def multiply(num1, num2, num3):
    return num1 * num2 * num3

print(multiply(2,4,5.2))

#Keyword arguments
def name(f_name, l_name, gender):
    print("Hello " + f_name + " " + l_name + " " + gender)
name(gender="MALE", f_name="Shubham", l_name="Patil")














