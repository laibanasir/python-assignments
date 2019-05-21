#------6 Program to get the volume of a sphere V=4 / 3 πr3-------
def main():
    while True:
        try:
            rad = input('Enter the radius of the sphere : ')
            rad = float(rad)
            volume(rad)
            break
        except:
            print('Invalid entry. Enter digits only.')
            
def volume(r):
    pi = 3.14
    vol = (4 / 3) * pi * (r ** 3)
    print('The volume of the sphere is' , vol)
    
main()
