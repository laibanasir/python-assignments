#---- to check whether given input is palindrome or not ----
print('check whether your input is palindrome or not')
string = input('provide input : ')
string1 = string[::-1]
if string == string1 :
    print('palindrome')
else:
    print('not palindrome') 