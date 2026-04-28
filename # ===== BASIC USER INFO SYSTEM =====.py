# ===== BASIC USER INFO SYSTEM =====
# simple python project using basic concepts

print("---- USER INFORMATION SYSTEM ----\n")

# taking inputs
user_name = input("Enter your full name: ")
user_age = input("Enter your age: ")
user_weight = input("Enter your weight (kg): ")
fav_color = input("Enter your favourite color: ")

# type casting
age = int(user_age)
weight = float(user_weight)

# using string methods
user_name = user_name.strip().upper()
fav_color = fav_color.lower()

print("\nData Saved Successfully!\n")

# displaying collected data
print("Name :", user_name)
print("Age :", age)
print("Weight :", weight, "kg")
print("Favourite Color :", fav_color)

# using operators
next_year_age = age + 1
double_weight = weight * 2

# conditional statements
if age < 18:
    age_group = "Teenager"
elif age >= 18 and age < 60:
    age_group = "Adult"
else:
    age_group = "Senior"

# another condition
if weight > 70:
    health_msg = "You should take care of fitness"
else:
    health_msg = "You are doing good"

# string concatenation
final_msg = "\nHello " + user_name + ", next year you will be " + str(next_year_age)

# output section
print("\n--- RESULT ---")
print("Age Group :", age_group)
print("Double Weight Value :", double_weight)
print(health_msg)
print(final_msg)

# ending message
print("\nProgram Ended Successfully!")
