#---- 32 Prints user's name in reverse order ----
first = input('Enter first name : ')
last = input('Enter last name : ')
full = first + ' ' + last
full = full[::-1]
print('Your name in reverse order is :' , full)
