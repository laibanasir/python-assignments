#---- 24 sum of first n positive integers ----
print('To find the sum of first n positive numbers ')
num = int(input('Enter n number : '))
total = 0
for n in range (1, num + 1):
    total += n
print('Sum of first' , num , 'postive integers is' , total)
