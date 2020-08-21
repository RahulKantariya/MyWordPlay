import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return (data[word])
    elif len(get_close_matches(word,data.keys())) > 0:
        choice=input(f"did you mean {get_close_matches(word,data.keys())[0]} instead of {word} ? if yes then enter y or no then enter n: ")
        if choice == 'y':
            return (data[get_close_matches(word,data.keys())[0]])
        elif choice == 'n':
            return ("this word is doesn't exists plese try agian..")
        else:
           return ("sorry!! we don't understand your entry")
    else:
        return ("this word is doesn't exist, please double cheack your word before enter it")
word=input("enter the word: ")

output=translate(word)

if type(output) == list:
    for item in output:
        txt=item
        print(txt)
else:
    txt2=output
    print(txt2)






