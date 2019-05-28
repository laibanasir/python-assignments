#---- program that accepts a string and calculate the number of digits and letters ----
print('To count letters and digits in a given string')
string = input('Enter string : ')
digits = 0
letters = 0
for s in string :
    if s.isdigit() :
        digits += 1
    elif s.isalpha() :
        letters += 1
print('Letters : ',letters ,'\nDigits : ',digits)