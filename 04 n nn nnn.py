#----------------------------4 Program that accepts an integer (n) and computes the value of (n+nn+nnn) -------------------------------
while True:
    try:
        n = input('Enter a number : ')
        n = int(n)
        n1 = str(n) + str(n)
        n2 = str(n) + str(n) + str(n)
        compute = n + int(n1) + int(n2)
        print('n + n n + n n n = ' , n , '+' , n , n , '+' , n , n , n , '=' , compute)
        break
    except:
        print('Invalid entry. The number should be an integer.')
