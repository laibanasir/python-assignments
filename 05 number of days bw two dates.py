#----------5 Program to calculate number of days between two dates----------
while True:
    try:
        print('Enter date in the format : dd/mm/yy')
        date1 = input('Enter the first date : ')
        date2 = input('Enter the second date : ')
        date_1 = date1.split('/')
        date_2 = date2.split('/')
        diff = (int(date_2[2]) * 365 + int(date_2[1]) * 30 + int(date_2[0])) - (int(date_1[2]) * 365 + int(date_1[1]) * 30 + int(date_1[0]))
        print('The number of days between' , date2 , 'and' , date1 , 'is' , diff ,'days.')
        break
    except:
        print('Follow the format and use digits only')
