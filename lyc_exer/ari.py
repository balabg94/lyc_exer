import string
import math

def ari(f):
    out = {1: "Kindergarten",
           2: "First Grade",
           3: "Second Grade",
           4: "Third Grade",
           5: "Fourth Grade",
           6: "Fifth Grade",
           7: "Sixth Grade",
           8: "Seventh Grade",
           9: "Eight Grade",
           10: "Ninth Grade",
           11: "Tenth Grade",
           12: "Eleventh Grade",
           13: "Twelfth Grade",
           14: "College"}

    
    text = open(f)
    s = text.read()
    s = s.lower()
    words = s.count(' ')
    characters = 0
    sentences = 0
    for i in s:
        if i in string.ascii_lowercase or i.isdigit():
            #print(i.isdigit())
           # print(i)
            characters += 1
    #return characters
    #return words
    symbols = ['.', '!', '?']
    for i in s:
        if i in symbols:
            sentences += 1
            continue
        else:
            continue

    nsentences = s.count(".") + s.count("!") + s.count("?")
    
   # print(words, characters, sentences)
    first_div = characters/words
    second_div = words/sentences

    first_var = 4.71*first_div
    second_var = 0.5*second_div

    score = first_var + second_var - 21.43

    score = math.ceil(score)
    
    return out[score]
