#---- 27 binary to decimal conversion ----
print('Binary to decimal conversion\n')
binary = input('Enter binary number : ')
binary = binary[::-1]
decimal = 0
for i, bit in enumerate(binary):
    decimal += int(bit) * 2 ** i
print('Decimal :' , decimal)
