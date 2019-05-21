#--------12 area of a triangle ------
def main():
    while True:
        try:
            print('To calculate the area of a triangle')
            base = input('Enter its base: ')
            height = input('Enter its height : ')
            base = float(base)
            height = float(height)
            area(base, height)
            break
        except:
            print('Invalid entry, digits must be entered.') 
def area(b,h):
    area = 1 / 2 * ( b * h )
    print('The area of the triangle is' , area)
main()
    
