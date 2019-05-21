#-----16 program to compute the distance between the points (x1, y1) and (x2, y2)----
from math import sqrt
def main():
    while True:
        try:
            print('Enter the pairs in the format x,y')
            x1_y1 = input('Enter x1,y1 : ')
            x2_y2 = input('Enter x2,y2 : ')
            first = x1_y1.split(',')
            second = x2_y2.split(',')
            result = calculate(first, second)
            print('The distance between the points' , x1_y1 , 'and' , x2_y2 , 'is' ,result)
            break
        except:
            print('Invalid entries, enter digits in the given format')
def calculate(f, s):
    r1 = (int(s[0]))**2 - (int(f[0]))**2
    r2 = (int(s[1]))**2 - (int(f[1]))**2
    r3 = sqrt(r1 + r2)
    return r3
main()
