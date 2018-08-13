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

def letter_check1():
    from functools import partial
    from collections import defaultdict
    source = 'abcdeeffgghhiijk'
    print(source)
    user_input = input('$$$ ')
    
    def list_duplicates(seq):
        print(seq)
        tally = defaultdict(list)
        for i, item in enumerate(seq):
            tally[item].append(i)
            print(tally[item])
            return ((key, locs) for key, locs in tally.items() if len(locs)>1)

    print(list_duplicates(source))
    for dup in sorted(list_duplicates(source)):
        print(dup)
    dups_in_source = partial(list_duplicates, source)
    #print( user_input, dups_in_source(user_input))


    
def game():
    tries_left = 6
    win = 1
    word = list(secret_word().lower())
    correct = ''.join(word)
    print(correct)
    guessed = []
    wrong_guesses = []
    for i in range(len(word)):
        guessed.append('_')

    while tries_left:
        
        
        wrong = ' '.join(wrong_guesses)
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
                guess = ' '.join(guessed)
                word[i] = '_'
                #print(word)
                #print (guessed)
                if ''.join(guessed) == correct:
                    print("\n",' '.join(guessed))
                    print("You have won")
                    exit()
            print(guess)
            print("Wrong guesses are: ",wrong)

            
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

    
