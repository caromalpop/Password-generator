#exercise 2
s = input("Enter your salary: ")
salary = float(s)
tax = salary * 0.18
after_tax = salary - tax

print("Your salary is: R", round(salary, 2))
print("18% tax is: R", round(tax, 2))
print("Salary after tax: R", round(after_tax, 2))