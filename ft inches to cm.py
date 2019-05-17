#-----17 program to convert height (in feet and inches) to centimetres-----
def main():
    while True:
        try:
            print('Enter the height in the following format ft,inches')
            height = input('Enter height : ')
            h = height.split(',')
            centi = float(h[0]) * 30.48 + float(h[1]) * 2.54
            print('The given height in centimeters is' , centi , 'cm')
            break
        except:
            print('Invalid entry, follow the format')
main()
