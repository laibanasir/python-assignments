#---- 32 LCM (Least Common Multiple) ----
print('To find LCM enter ')
num1 = int(input('number 1 : '))
num2 = int(input('number 2 : '))
if num1 > num2:
        lesser = num1
else:
        lesser = num2
while True:
    if(lesser % num1 == 0 and lesser % num2 == 0):
        lcm = lesser
        break
    lesser += 1
    
print('The lcm of' , num1 , 'and' , num2 , 'is' , lcm)
