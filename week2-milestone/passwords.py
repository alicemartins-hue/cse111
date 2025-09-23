import math

# Extra feature added for creativity:
# I created the function "iftrue_morepoint" which takes a Boolean value
# and explicitly returns 1 if it is True and 0 if it is False.
# Even though Python can convert Booleans to integers directly with int(True) or int(False),
# I implemented my own version to show understanding of conditionals and return values.


with open("toppasswords.txt", "r", encoding="utf-8") as f:
    toppasswords = f.read()

with open("wordlist.txt", "r", encoding="utf-8") as f:
    wordlist = f.read()

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]


def main():
    password = input("Password: ")
    while True:
        if password not in ("q","Q"):
            strength= password_strength(password)
            print(f"The strenght of your password is {strength} \n")

            print("If you want to quit type q or Q")
            password = input("Password: ")
        else:
            print(f"Exiting program... Good Bye!")
            break


def word_in_file(word, filename, case_sensitive=False):
    """Verify if the word is present in the file choosed
    Parameters
    word: the word (password)
    filename: one file
    case_sensitive: verify if the word are on file
    Return: Boolean"""

    if case_sensitive == True:
        word = word
        filename = filename
    else: 
        word = word.lower()
        filename = filename.lower()

    if word in filename:
        return True
    else:
        return False


def word_has_character(word, character_list):
    """See if each caracter in the word parameter 
    are present in the character_list.
     Parameters
     word: the password
     character_list: list of characters
     Return: Boolean """
    
    for ch in word:
        if ch in character_list:
            return True
    return False


def word_complexity(word):
    """Calculate complexity of the password 
    based on types of character 
    presents in the password.
    Parameter: word
    Return: Integer"""

    score= 0

    upper = word_has_character(word,UPPER)
    lower = word_has_character(word,LOWER)
    digits = word_has_character(word,DIGITS)
    special = word_has_character(word,SPECIAL)
    
    score = iftrue_morepoint(upper) + iftrue_morepoint(lower) + iftrue_morepoint(digits) + iftrue_morepoint(special)
    
    return score


def iftrue_morepoint(word):
    """Check if the parameter is true
    parameter: word
    return: integer"""

    value = 0
    if word == True:
        value = 1
        return value
    else:
        value= 0
        return value


def password_strength(password, min_length=10, strong_length=16):
    """Check length requirements
     Parameters
     password:Check the password lenght
     min_length: 10 characters
     strong_length: 15 characters 
     Return: Integer 
    """
    
    strenght_value = 0
    lenght = len(password)
    toplist = word_in_file(password, toppasswords, True)
    dic = word_in_file(password, wordlist)

    if toplist == True:
        print("Password is a commonly used password and is not secure.")
        return strenght_value
    
    elif dic == True:
        print("Password is a dictionary word and is not secure.")
        return strenght_value
    
    elif lenght <= min_length:
        print("Password is too short and is not secure.")
        strenght_value = 1
        return strenght_value
    
    elif lenght >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        strenght_value = 5
        return strenght_value

    else:
        base = 1
        complexity = word_complexity(password)
        score = base + complexity
        return score


main()

if __name__ == "__main__":
    main()