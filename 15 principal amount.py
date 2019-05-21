#------ 15 program to compute the future value of a specified principal amount, rate of interest, and a number of years -----
def main():
    while True:
        try:
            print('To compute the future value')
            amount = input('Enter the principal amount : ')
            rate = input('Enter the rate of interest : ')
            years = input('Enter the number of years : ')
            amount = float(amount)
            rate = float(rate)
            years = float(years)
            future(amount, rate, years)
            break
        except:
            print('Invalid entry, please re-enter the digits.')
def future(a, r, y):
    value = a * ((1 + (0.01 * r )) ** y)
    print('The future value of the specified entries will be ' ,format(value,'.2f'))
main()
            
