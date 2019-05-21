#---- 28 octal to decimal conversion ----
print('Octal to decimal conversion\n')
octal = input('Enter octal number : ')
octal = octal[::-1]
decimal = 0
for i, bit in enumerate(octal):
    decimal += int(bit) * 8 ** i
print('Decimal :' , decimal)
