num1=float(input("Enter the first number:"))
operator=input("Enter operator (+,-,*,/):")
num2=float(input("Enter the second number:"))
if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    if num2!=0:
        result=num1/num2
    else:
        result="Error!Division By Zero."
else:
    result="Invalid Operator!"
print("Result:",result)
