#---- to find the number of notes (Sample of notes: 10, 20, 50, 100, 500, and 1000 ) against an given amount ----
print('Find the number of notes in your given amount')
amount = int(input('Enter the amount of money : '))
amu1000 = amount // 1000
amu500 = (amount % 1000 ) // 500
amu100 = ((amount % 1000) % 500) // 100
amu50 = (((amount % 1000) % 500) % 100 ) // 50
amu20 = ((((amount % 1000) % 500) % 100 ) % 50) // 20
amu10 = (((((amount % 1000) % 500) % 100 ) % 50) % 20) // 10
amuleft = (((((amount % 1000) % 500) % 100 ) % 50) % 20) % 10 
print('Amount : ',amount)
print('notes of 1000 : ',amu1000)
print('notes of 500  : ',amu500)
print('notes of 100  : ',amu100)
print('notes of 50   : ',amu50)
print('notes of 20   : ',amu20)
print('notes of 10   : ',amu10)
print('remaining amu : ',amuleft)
