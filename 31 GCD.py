#---- 31 GCD (Greatest Common Divisor) ----
print('To find GCD enter ')
num1 = int(input('number 1 : '))
num2 = int(input('number 2 : '))
if num1 > num2:
        smaller = num2
else:
        smaller = num1
for i in range(1, smaller+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        gcd = i
print('The gcd of' , num1 , 'and' , num2 , 'is' , gcd)
