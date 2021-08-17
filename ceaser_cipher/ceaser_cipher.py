import nltk
import re
from nltk.corpus import words, names
from nltk.util import pr


nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


word_list = words.words()
name_list = names.words()

def is_english(text):

    candidate_words = text.split()
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower()  in word_list or word  in name_list:
            continue
        else:
            return False
    return True
            

    


def encrypt(string , key):
    string_shifted=''
    string=string.lower()
    
    for char in string:
        if char.isalpha()==True:
            shifted=ord(char) + key  
            if shifted  > 122:
                shifted-=26
            elif shifted < 97 :
                shifted+=26   
            string_shifted+=chr(shifted)
        else:
            string_shifted+=char
    return string_shifted 

        
def decrypt(shifted_string , key):
    return encrypt(shifted_string,-key)


def crack(text):  
    for i in range(1,27):
        check_text=encrypt(text,i)
        if is_english(check_text):
            return check_text
    



if __name__=="__main__":
    print(encrypt('It was the best of times, it was the worst of times.',15))
    print(decrypt('vw wa fipo',14))
    print(is_english("welcome home"))
    print(crack("kszqcas vcas"))
    print(encrypt("Hello world",5))
    print(crack("mjqqt btwqi"))
    print(crack('xi lph iwt qthi du ixbth, xi lph iwt ldghi du ixbth.'))