import random

def secret_word():
    wordfile = "/usr/share/dict/words"
    min_length = 6
    
    good_words = []
    f = open(wordfile)
    for i in f:
        word = i.strip()
        if word.isalpha() and len(word) >= min_length:
            good_words.append(word)
    f.close()
    
    return random.choice(good_words)
    

#print (secret_word().lower())


def letter_check(w, uinput):
    letter_indices = []
    number = w.count(uinput)
    for i in range(1, number+1):
        letter_index = w.index(uinput)
        letter_indices.append(letter_index)
        w[letter_index] = '-'
    return letter_indices
    


    
def game():
    tries_left = 6
    word = list(secret_word().lower())
    correct = ''.join(word)
    print(correct)
    guessed = []
    wrong_guesses = []
    for i in word:
        guessed.append('_')

    while tries_left:

        user_input = input("\n\nGuess a letter > ")


        if len(user_input) != 1:
            print("Please enter a single letter")
            continue

        
        if user_input in word:
            letter_indices = list(letter_check(word, user_input))
            for i in letter_indices:
                # print(word)
                # print(guessed)
                guessed[i] = user_input
                guess_word = ''.join(guessed)
                word[i] = '_'
                #print(word)
                #print (guessed)
                if guess_word == correct:
                    print("\n",guess_word)
                    print("You have won")
                    exit()
            print(' '.join(guessed))
            print("Wrong guesses are: ",' '.join(wrong_guesses))

            
        else:
            print("\nWrong")
            print(' '.join(guessed))
            if user_input not in wrong_guesses:
                wrong_guesses.append(user_input)
                print("Wrong guesses are: ",' '.join(wrong_guesses))
            else:
                 print("Wrong guesses are: ",' '.join(wrong_guesses))
            if tries_left == 1:
                print("The right word is ", correct)
                print("You have been hanged.")
                exit()
            else:
                tries_left -= 1
                print("lifes left: ", tries_left)

    

