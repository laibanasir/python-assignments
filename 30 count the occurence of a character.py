#---- 30 to count the occurence of a specific character in a string ----
print('To count the occurrence of a spicific character in a string')
what = input('which character\'s occurence do you want to count? \n')
string = input('Enter string : ')
count = 0
for i in string:
    if what == i:
        count += 1
print('The character' , what , 'has appeared' , count , 'times.')
