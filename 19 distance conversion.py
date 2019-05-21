#----17 program to convert the distance (in feet) to inches, yards, and miles. 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile----
def main():
    while True:
        try:
            dis = float(input('Enter the distance in feet : '))
            inches = dis / 12
            yard = dis / 3
            mile = dis / 5280
            print('Distance in feet :' , dis,'\nDistance in inches :' , inches,'\nDistance in yards :' , yard ,'\nDistance in miles :' , mile)
            break
        except:
            print('Enter a valid distance')
main()
