#-----22 program to calculate body mass index -----
def main():
    while True:
        try:
            height = float(input('Enter height in meters : '))
            weight = float(input('Enter weight in kilograms : '))
            BMI = weight / height**2
            print('Your BMI is ',BMI)
            break
        except:
            print('Invalid entry. Enter again')
main()
