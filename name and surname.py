#Greet the user:

name = input("What is your name?")
print("Hello" + name)
surname = input("What is your surname?")
print("Hello" + name + " " + surname)


#Getting user weight and height to calculate BMI:
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))

#Getting user age to check if they are an adult:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")  

