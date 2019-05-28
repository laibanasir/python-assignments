#---- program to create the multiplication table (from 1 to 10) of a number ---
print('Multiplicaion table (1 to 10)')
num = int(input('Enter a number to see its table : '))
for i in range(1, 11) :
    print(num , 'x' , i ,'=' , num * i )
