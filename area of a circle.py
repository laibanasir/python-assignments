#---------------------1 Program which accepts the radius of a circle from the user and compute the area --------------------
pi = 3.14
while True: 
    try:
        rad = input("Enter radius : ")
        rad = float(rad)
        area = pi * rad**2
        print('The area of the circle with radius ',rad , 'is ', area)
        break
    except:
        print('Enter a valid radius.')
