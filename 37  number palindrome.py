#----  program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure ----
def number():
    num_inp = input('Enter digits : ')
    num_inp_rev = num_inp[::-1]
    num_total_inp = int(num_inp) + int(num_inp_rev)
    num_total_inp = str(num_total_inp)
    num_totalrev = num_total_inp[::-1]
    while True :
        if num_total_inp != num_totalrev : 
            print('The final sum of' , num_inp , 'and' , num_inp_rev ,'is' , num_total_inp ,'\nIts reverse is' , num_totalrev , 'and its not a palindrome.\ninput again')
            number()
            break
        else: 
            print('The final sum of' , num_inp , 'and' , num_inp_rev ,'is' , num_total_inp ,'\nIts reverse is' , num_totalrev , 'and its a palindrome.')
            break
number()    
    

 

