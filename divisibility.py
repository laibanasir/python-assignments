#------------3 Program to check whether a number is completely divisible by another number ----------
while True:
    try:
        num1 = input('Enter divisor : ')
        num2 = input('Enter divident : ')
        num1 = int(num1)
        num2 = int(num2)
        if num1 % num2 == 0:
            print('The two numbers are completely divisble by eachother.')
        else:
            print('The two numbers are not completely divisble by eachother.')
        break
    except:
        print('Invalid entry. Enter integer values.')
