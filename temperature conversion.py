#----- 23 program to convert temperatures to and from Celsius, Fahrenheit -----
def main():
    while True:
        try:
            print('Enter an option from the menu: \n1. Fahrenheit to celcius\n2. Celcius to Fahrenheit')
            option = int(input('---------------------------------------------------------------\n'))
            if option == 1:
                f2c()
            elif option == 2:
                c2f()
            break
        except:
            print('Invalid entry, enter again.')
def f2c():
    print('---------------------------------------------------------\nFahrenheit to Celcius ')
    temp = float(input('enter temperature : '))
    ctemp = (32 * temp - 32) * 5/9
    print('Temperature in celcius :' , ctemp)
def c2f():
    print('----------------------------------------------------------\nCelcius to Fahrenheit ')
    temp = float(input('enter temperature : '))
    ftemp = (temp * 9/5) + 32
    print('Temperature in fahrenheit :' , ftemp)
main()

    
    
