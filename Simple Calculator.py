#Simple Calculator

# a = number, b = another number
#Output resul = a + b (Example)

firstNumber = input()

op = input() #specifiying the operator

otherNumber = input()
print()

#specifiying which operator to use, then perform according to it.
if op == "+":
    result = int(firstNumber) + int(otherNumber)
    print(result)
    print()
if op == "-":
    result = int(firstNumber) - int(otherNumber)
    print(result)
    print()
if op == "*":
    result = int(firstNumber) * int(otherNumber)
    print(result)
    print()
if op == "//":
    result = int(firstNumber) // int(otherNumber)
    print(result)
    print()
    
#Maybe to add a while-loop to keep it going...?
