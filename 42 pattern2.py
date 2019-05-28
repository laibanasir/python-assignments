#---- pattern with nested loop ----
for row in range(1, 6):
    for col in range(1, row+1):
        print(col, end ='')
    print("")
for row in range(4, 0, -1):
    for col in range(1, row + 1):
        print(col, end ='')
    print("")
