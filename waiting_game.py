# Challenge 4 : Play the Waiting Game
# ----------------------------------------
# Your goal is to implement a function, waiting_game(), that prints a message for the player to wait a random amount of time, somewhere between two to four seconds. When the player presses Enter, that starts a timer. The player's goal is to wait the specified number of seconds and then press Enter again. That displays the elapsed time, along with a message about whether the player was too fast, too slow, or right on target.

import random
import time

def waiting_game():
    seconds = random.randrange(2, 4)
    print(f"Your target time is {seconds} seconds")
    
    input("--Press Enter to Begin--")
    
    start_time = time.time()

    input(f"...Press Enter again after {seconds} seconds...")

    end_time = time.time()

    elapsed_time = end_time - start_time

    difference = abs(elapsed_time - seconds)

    score = "too slow" if elapsed_time > seconds else "too fast"

    return f"Elapsed time: {'%.2f' % (elapsed_time)} ({'%.2f' % (difference)} seconds {score})"

print(waiting_game())