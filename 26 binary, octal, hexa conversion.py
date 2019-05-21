#---- 26 integer conversion to binary, octal and hexadecimal ----
def binary(num, rem, res):
    if num > 1:
        binary(num // 2, rem, res)
        rem = num % 2
        res = str(rem) + res
        print(res , end = '' )
        
def octal(num, rem, res):
    if num > 1:
        octal(num // 8, rem, res)
        rem = num % 8
        res = str(rem) + res
        print(res , end = '' )

def hexa(num, rem, res):
    if num > 1:
        hexa(num // 16, rem, res)
        rem = num % 16
        res = str(rem) + res
        print(res , end = '' )
        
print('Binary, octal and hexadecimal conversion\n')
print('select an option from the menu: \n1. Binary conversion\n2. Octal conversion \n3. Hexadecimal conversion\n')
choice = int(input(': '))
rem = 0
res = ""

if choice == 1 :
    num = int(input('enter a decimal number : '))
    print('Binary : ')
    binary(num, rem, res)
    
elif choice == 2 :
    num = int(input('enter a decimal number : '))
    print('Octal : ')
    octal(num, rem, res)

elif choice == 3 :
    num = int(input('enter a decimal number : '))
    print('Hexa-decimal : ')
    hexa(num, rem, res)
    

    

