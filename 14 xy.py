#------14  program to solve (x + y) * (x + y)-----
def main():
    while True:
        try:
            print('(x + y) * (x + y)')
            x = input('Enter the value of x : ')
            y = input('Enter the value of y : ')
            x = float(x)
            y = float(y)
            formula(x, y)
            break
        except:
            print('Invalid entry, enter digits')
def formula(x, y):
    ans = (x + y) * (x + y)
    print('The answer of (x + y) * (x + y) is' , ans)
main()
