# Challenge 10: Write a function to generate a pass phrase similar to what 
# diceware does

import secrets

def pass_phrase_generator (word_count):
    with open("diceware_wordlist.txt", 'r') as file:
        words = file.read().split()

        word_list = {int(key): value for key, value in zip(words[::2], words[1::2])}

        secret_phrase = []
        for _ in range(word_count):
            dice_number = secrets.choice(list(word_list.keys()))
            secret_phrase.append(word_list.get(dice_number))

    return(secret_phrase)
        

print(" ".join(pass_phrase_generator(5)))