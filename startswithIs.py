#--------8 program to get a new string from a given string where "Is" has been added to the front-------
def main():
    while True:
        try:
            string = input('Enter a string : ')
            if string.startswith('Is'):
                print('Your string' , string , 'is correct.')
            else:
                new_string = 'Is'+string
                print('Your string' , string , 'has been formatted to' , new_string)
            break
        except:
            print('Invalid entry.')
main()
