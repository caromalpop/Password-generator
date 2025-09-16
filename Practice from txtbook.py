#Examples of in() and float() functiojns

print("Please enter an integer")
a = input()
print("Your input:", a)

b = int(a)
print("As integer:", b)
print("Doubled:", b *2)

print("Please enter a number")
x = input()
print("Your input:", x)

try:
	y = float(x)
	print("As float:", y)
	print("Doubled:", y * 2)
except ValueError:
	print("Invalid input: could not convert to float.")
	

    #exercise
	a = input("Number in inches:")
	b = float(a)
	print("This is the number:",b)
	print("The number doubled:", b*2)
	print(b,"inches are:", b*2.54, "cm")

#exercise 2
s = input("Enter your salary: ")
salary = float(s)
tax = salary * 0.18
after_tax = salary - tax

print("Your salary is: R", round(salary, 2))
print("18% tax is: R", round(tax, 2))
print("Salary after tax: R", round(after_tax, 2))	
   

