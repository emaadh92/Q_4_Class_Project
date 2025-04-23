# Practice 1: List Manipulation

# List in Python

Fruits = ["Apples","Mango","Orange","Cherry","Peach","WaterMelon"]

# Slicing Of python

print(type(Fruits[3]))
print(len(Fruits))
print(Fruits[:4])
Fruits[1] = "Mellon"

print(Fruits)


# Checking MemberShip
Fruits = ["Apples","Mango","Orange","Cherry","Peach","WaterMelon"]

print("Apples" in Fruits)
print("Apples" not in Fruits)

# Adding Removing in python
Fruits = ["Apples","Mango","Orange","Cherry","Peach","WaterMelon"]
Fruits.append("Banana")
Fruits.remove("Orange")
Fruits.clear()
Fruits.pop()

print(Fruits)
Fruits = ["Apples","Mango","Orange","Cherry","Peach","WaterMelon"]
Fruits.insert(2, "Cherry")
Fruits.pop(1)  # Pop use for Remove through index
print(Fruits)


numbers = list(range(1, 11))

numbers = [num for num in numbers if num % 2 != 0]
print("Updated list (odd numbers):", numbers)

#  If-Statement

number = -5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Practice 3: Dictionary Operations

person = {"name": "Alice", "age": 25, "city": "New York"}

person["profession"] = "Engineer"
print("Updated dictionary:", person)

# Practice 4: Loops and Control Flow

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Practice 5: Function

def sum_of_evens(numbers):
    
    return sum(num for num in numbers if num % 2 == 0)


numbers = [1, 2, 3, 4, 5, 6]
print("Sum of even numbers:", sum_of_evens(numbers))



# Projects
# email to customer for Thanks to pusrchase thing from our store

customer = input()

email = f"""
Dear {customer},
   Thank you for your purchase! We appreciate your support and look forward to serving you again.

   Regards
   Support team"""

print(email)

# Rabri Required for treatment in class
# There are 12 faculty member.
# There are 4 Administrative staff member.
# There are 100 student.
# Expacted 15 person will be absent.

# Rabri per person 250g

faculty_member = 12
admin_member = 4
student = 100
expacted_absent = 15

total_members = faculty_member + admin_member + student

present_member = total_members - expacted_absent

rabri_required = present_member * (250/1000)

print(f"There are total {total_members} member")
print(f"There are {present_member} members are present")
print(rabri_required,f"kg Rabri is required for {present_member} peoples.")
print(rabri_required * 1000,"gram")



# Hungary Person

is_hungry =False
burger_lover =True
pizza_lover = False
cheez_lover =True

if (is_hungry and (burger_lover or pizza_lover) or cheez_lover):
  print("Let's Order the food")
elif (is_hungry and (not burger_lover or not pizza_lover)):
  print("See Menu More")
elif (is_hungry or burger_lover):
  print("Let's Order the food")
else:
  print("let's go to the sleep.")


# countdown proect

count_down = 10

while count_down > 0:
  print(f"{count_down}....")
  if count_down == 1:
    print("Happy New Year")
  count_down -= 1