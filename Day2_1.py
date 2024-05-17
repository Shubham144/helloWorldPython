"""
#LISTS
food = "pizza"
food_items = ["pizza", "burger", "hotdog", "pasta"]
print(food_items)
food_items.append("sushi")
print(food_items)
food_items.pop()
print(food_items)
food_items.remove("burger")
print(food_items)
food_items.insert(2, "TEST")
print(food_items)
food_items.sort()
print(food_items)
food_items.clear()
print(food_items)

#2D List
drinks = ["mocktail", "juice", "coffee"]
dessert = ["ice crean", "cake"]
dinner = ["pizza", "hamburger", "pasta"]
food = [drinks,dessert,dinner]
print(food[1][1])

#Tuple
student_1 = ("Shubham", 25, "male", 150.3)
student_2 = ("sonali", 26, "female", 140.2)
print(student_2.index(26))
print(student_1.count("male"))

#set
utensils = {"fork","spoon","knife", "xyz"}
dished = {"bowl", "plate", "cup", "knife"}
utensils.add("napkin")
utensils.remove("spoon")
#utensils.update(dished)
dinner_table = dished.union(utensils)
print(utensils.difference(dished))
print(utensils.intersection(dished))
for x in dinner_table:
    print(x)
"""

