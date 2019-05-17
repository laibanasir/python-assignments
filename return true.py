#-----13  program that will return true if the two given integer values are equal or their sum or difference is 5 ------
def main():
    while True:
        try:
            num1 = input('Enter first integer : ')
            num2 = input('Enter second integer : ')
            num1 = int(num1)
            num2 = int(num2)
            value = check(num1, num2)
            print(value)
            break
        except:
            print('Invalid entry, enter integral values.')
def check(n1, n2):
    if n1 == n2 or n1 - n2 == 5 or n1 + n2 == 5:
        return True
    else:
        return False
main()
