#----------2 Program to check if a number is positive, negative or zero ------------
while True:
    try:
        num = input('Enter a number to check its nature : ')
        num = float(num)
        if num > 1:
            print('positive')
        elif num < 1:
            print('negetive')
        elif num == 0:
            print('zero')
        break
    except:
        print('Invalid entry.')
