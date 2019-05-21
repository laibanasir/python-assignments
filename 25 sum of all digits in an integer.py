#---- 25 to calculate sum of the digits in an integer ----
num = input('Enter an integer to calculate the sum of all its digits : ')
total = 0
for n in num:
    total += int(n)
print('The sum of all the digits in' , num , 'is' , total)
