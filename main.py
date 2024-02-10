#Remove pass and complete the cde
def check_character(word, index):
   sent = word[index].lower()
   if sent.islower() == True:
       return 'letter'
   elif word.isspace() == True:
       return 'space'
   
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))