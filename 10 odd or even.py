#---------10 program to find whether a given number is even or odd------
def main():
    while True:
        try:
            num = input('Enter a number to check whether its odd or even : ')
            num = int(num)
            oddoreven(num)
            break
        except:
            print('Enter a valid integer.')
def oddoreven(n):
    if n % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
main()
