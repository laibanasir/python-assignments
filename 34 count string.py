#---- 34 count vowels / consonants ----
print('To count vowels / consonants.')
string = input('Enter string: ')
string = string.lower()
vowelcount = 0
consonantcount = 0
for s in string :
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' :
        vowelcount += 1
    else: 
        consonantcount +=1 
print('number of vowels : ',vowelcount,'\nnumber of consonants : ',consonantcount)