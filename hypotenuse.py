#----18 program to calculate the hypotenuse of a right angled triangle----
from math import sqrt
def main():
    while True:
        try:
            print('Enter the length of the shorter sides')
            a = float(input('a : '))
            b = float(input('b : '))
            c = sqrt(a ** 2 + b ** 2)
            print('Hypotenuse :' , c)
            break
        except:
            print('Invalid entry')
main()
