#---- program to get the Fibonacci series between 0 to 50 ----
print('The Fibonacci series')
num = int(input('Enter the number of digits that you want in the series : '))
first = 0
second = 1
nextnum = 0
print(first , second , end=' ')
for num in range(2, num) :
    nextnum = first + second
    print(nextnum , end = ' ')
    first = second 
    second = nextnum 
    
