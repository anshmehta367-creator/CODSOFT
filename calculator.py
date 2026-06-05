#Calculator
#defining function for each operation
def add():
    return(num1 + num2)

def sub():
    return(num1 - num2)

def mul():
    return(num1 * num2)

def div():
    return(num1 / num2)

def fldiv():
    return(num1 // num2)

def mod():
    return(num1 % num2)
      
print("\n")
print("*************************  Calculator  **********************")
#Operations to perform serial wise
print("Select the operation from below to perform on two numbers\n" "1. Addition\n" "2. Subtraction\n" "3. Multiplication\n" "4. Division\n" "5. Floor Division\n" "6. Modulus\n")

#Operation to perform
number = int(input('enter operation to perform: '))
#Enter the numbers
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
#conditional statements
if number == 1:
    print("Addition : ", add())
    print("Operation Successful")

elif number == 2:
    print("Subtraction : ", sub())
    print("Operation Successful")
    
elif number == 3:
    print("Multiplication : ", mul())
    print("Operation Successful")

elif number == 4:
    print("Division : ", div())
    print("Operation Successful")

elif number == 5:
    print("Floor Division : ", fldiv())
    print("Operation Successful")

elif number == 6:
    print("Modulus : ", mod())
    print("Operation Successful")

else:
    print("Enter Valid Operation Number")





