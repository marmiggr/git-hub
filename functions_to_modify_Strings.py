age = input("What is your age: ")
first_name = input("What is your name: ")
last_name = input("What is your last name: ")
age = int(input("What is your age: "))

calories_breakfast = float(input("How many calories did you eat for breakfast? "))
calories_lunch = float(input("How many calories did you eat for lunch? "))
calories_dinner = float(input("How many calories did you eat for dinner? "))

calories = calories_breakfast + calories_lunch + calories_dinner

print("Hello " + first_name.capitalize() + " " + last_name.upper()+ " you are " + str(age))
print("You eat this total of calories:", str(calories))