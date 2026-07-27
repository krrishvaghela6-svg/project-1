Personal-Fitness-Tracker/
│── fitness_tracker.py
│── README.md
print("===================================")
print("   PERSONAL FITNESS TRACKER")
print("===================================")

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
weight = float(input("Enter Your Weight (kg): "))
height = float(input("Enter Your Height (m): "))
steps = int(input("Enter Today's Steps: "))
water = float(input("Enter Water Intake (Liters): "))

# BMI Calculation
bmi = weight / (height * height)

print("\n========== FITNESS DASHBOARD ==========")
print("Name          :", name)
print("Age           :", age)
print("Weight        :", weight, "kg")
print("Height        :", height, "m")
print("BMI           :", round(bmi, 2))
print("Steps Walked  :", steps)
print("Water Intake  :", water, "Liters")

# BMI Status
if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Healthy"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("Health Status :", status)

# Steps Goal
if steps >= 10000:
    print("Steps Goal    : Achieved")
else:
    print("Steps Goal    : Not Achieved")

# Water Goal
if water >= 2:
    print("Water Goal    : Completed")
else:
    print("Water Goal    : Drink More Water")

print("===================================")
print("Stay Healthy! 💪")
print("===================================")
# Personal Fitness Tracker Dashboard

## Features
- BMI Calculator
- Health Status
- Daily Steps Tracking
- Water Intake Tracking
- Fitness Dashboard

## Language
Python 3
===================================
   PERSONAL FITNESS TRACKER
===================================
Enter Your Name: Krishna
Enter Your Age: 28
Enter Your Weight (kg): 70
Enter Your Height (m): 1.75
Enter Today's Steps: 12000
Enter Water Intake (Liters): 2.5

========== FITNESS DASHBOARD ==========
Name          : Krishna
Age           : 28
Weight        : 70.0 kg
Height        : 1.75 m
BMI           : 22.86
Steps Walked  : 12000
Water Intake  : 2.5 Liters
Health Status : Healthy
Steps Goal    : Achieved
Water Goal    : Completed
===================================
Stay Healthy! 💪
===================================