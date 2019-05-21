#---- 32 LCM (Least Common Multiple) ----
print('To find LCM enter ')
num1 = int(input('number 1 : '))
num2 = int(input('number 2 : '))
if num1 > num2:
        greater = num2
else:
        greater = num1
while True:
    if((num1 % greater == 0) and (num2 % greater == 0)):
        lcm = greater
        break
    greater += 1
    
print('The lcm of' , num1 , 'and' , num2 , 'is' , lcm)
