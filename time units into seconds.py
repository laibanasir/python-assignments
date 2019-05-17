#---- 20 program to convert all units of time into seconds ----
def main():
    while True:
        try:
            print('Enter the time in the following format dd/hh/mm/ss')
            time = input('Enter time : ')
            time1 = time.split('/')
            time2 = float(time1[0]) * 86400 + float(time1[1]) * 3600 + float(time1[2]) * 60 + float(time1[3])
            print('Total seconds =', time2)
            break
        except:
            print('Invalid entry, follow the format')
main()
            
