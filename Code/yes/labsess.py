turkhis_words = []
english_words = []
with open("~/Code/yes/turkish.txt","r") as trk:
    for line in trk:
        turkhis_words.append(line.strip())

with open("english.txt","r") as eng:
    for line in eng:
        english_words.append(line.strip())

turkish_to_english = {}
english_to_turkish = {}

for i in range(len(turkhis_words)):
    current_turkish = turkhis_words[i]
    current_english = english_words[i]
    turkish_to_english[current_turkish] = current_english
    english_to_turkish[current_english] = current_turkish

def translate_turkish_to_english(turkish_word):
    if turkish_word in turkish_to_english:
        print(turkish_to_english[turkish_word])
    else:
        print("nı exist")

def translate_english_to_turkish(english_word):
    if english_word in english_to_turkish:
        print(english_to_turkish[english_word])
    else:
        print("no exist")
##

def solve_polynomial(co, x):
    if not type(x) is int:
        print("Given X is not an integer.")
        return None
    try:
        result = 0
        for i in range(len(co)):
            result += co[i] * x**i  
        return result
    except:
        print("Something is wrong!")
        return None
co = (5,0,3,4)
result = solve_polynomial(co,2)
print(result)
