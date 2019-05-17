#------11 program to test whether a passed letter is a vowel or not------
def main():
        letter = input('Enter a letter to check if its a vowel or not : ')
        check(letter)
def check(let):
    if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u' or let =='A' or let == 'E' or let == 'I' or let == 'O' or let == 'U':
        print('The letter is a vowel')
    else:
        print('The letter is not a vowel')
main()
