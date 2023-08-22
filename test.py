def sum(a,b):  
    print(a+b)
    
def sub(a,b):  
    print(a-b)
    
def mul(a,b):
    print(a*b)
    
def div(a,b):
    print(a/b)

a = int(input("Enter first number = "))
b = int(input("Enter second number = ")) 
L = print("1 = ADD ,2 = Subtract, 3 = Multiply, 4 = Divide")    
Cal = int(input("Enter the number for operation required"))

if Cal == 1:
    sum(a,b)
    
elif Cal == 2:
    sub(a,b)
    
elif Cal == 3:
    mul(a,b)
    
elif Cal == 4:
    div(a,b)
    
else :
    print("WRONG INPUT FOR OPERATIONS")
    
