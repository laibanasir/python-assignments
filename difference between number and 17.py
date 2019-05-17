#----------7 Program to get the difference between a given number and 17, difference cannot be negative----------
def main():
    while True:
        try:
            num = input('Enter number to get the difference between it and 17 : ')
            diff(num)
            break
        except:
            print('Invalid entry. Enter digits')
            
def diff(n):
    n = float(n)
    if n > 17:
        print('Enter a number lesser than 17, as the difference cannot be negetive.')
        main()
    else:
        difference = 17 - n
        print('The difference between' , n , ' and 17 is' , difference)
        
main()
