#Logical operators
x = 4
y = 6
z = 8
print(f"x: {x}, y: {y}, z: {z}")
if x < y and y < z:
    print("x is less than y AND y is less than z")
if x < y or y > z:
    print("x is less than y OR y is greater than z")
    


#🔧 Logical Operators Activity: Test Instructions
#✅ What to do:

#Create three variables:
#Assign any numbers to x, y, and z.

#Print out the values of x, y, and z so you can see them.

#Write an if statement using the and operator:

#Check if x is smaller than both y and z.
#If True, print: "x is the smallest number"
#Else, print: "x is NOT the smallest number"
#Write an if statement using the or operator:
#Check if y is greater than x or greater than z.
#If True, print: "y is not the smallest number"
#Else, print: "y might be the smallest"
#Write an if statement using the not operator:
#Check if y is not smaller than x.
#If True, print: "y is not smaller than x"
#Else, print: "y is smaller than x"
#Change the values of the variables and run the code again to see how the results change.


#Assigning the variables
x = 11
y = 2
k = 4

#Pinting the values
print(f"x: {x}, y: {y}, k: {k}")

#Write an if statement using the and operator:
if x > y and k < y:
    print("x IS GREATER THAN Y AND k IS LESS THAN Y")
else:
    print("x is NOT GREATER THAN Y AND k IS NOT LESS THAN Y")

if x < y or x < k:
    print("x is less than both")
else:
    print("x is NOT less than both")

    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

    if x != k:
        print("x is not equal to k")    
    else:
        print("x is equal to k")
        