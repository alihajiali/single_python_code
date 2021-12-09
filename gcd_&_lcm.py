# get number

number1 = int(input("please enter number1 : "))
number2 = int(input("please enter number2 : "))


# the greatest common divisor of the two integers
# way1


check = min(number1, number2)
 
while check > 0:
    if number1%check == 0 and number2%check == 0:
        print(f'''the greatest common divisor of the 
        {number1} and {number2} is {check}''')
        break
    check -= 1
    
   
# the greatest common divisor of the two integers
# way2


def func(number1, number2):
    if number2 == 0:
        return number1
    else:
        return func(number2, number1%number2)
 
result = func(number1, number2)
print(f'''the greatest common divisor of the 
        {number1} and {number2} is {result}''')


# the greatest common divisor of the two integers
# way3


import math

print(f'''the greatest common divisor of the 
        {number1} and {number2} is {math.gcd(number1, number2)}''')


#----------------------------------------------------------------------


# The smallest denominator of the two integers
# way1

check = max(number1, number2)

while(True):
    if check%number1 == 0 and check%number2 == 0:
        print(f'''the smallest denominator divisor of the 
        {number1} and {number2} is {check}''')
        break
    check += 1
    
    
# The smallest denominator of the two integers
# way2


import math

print(f'''the smallest denominator divisor of the 
        {number1} and {number2} is {abs(number1*number2) // math.gcd(number1, number2)}''')
