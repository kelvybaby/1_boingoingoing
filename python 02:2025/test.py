import numpy as np
import pandas as pd
from matplotlib.pyplot import plot, show, title
import seaborn as sns

'''
print("All libraries imported successfully!")

# Simple plot
data = [1, 2, 3, 4, 5]
plot(data)
title("Test Plot")
show()
'''

'kelvin'
def guess_the_number() -> None:
    secret_number = 7  # The number to guess
    guess = int(input("Guess a number between 1 and 10: "))  # Get user input

    if guess == secret_number:
        print("Woohoo! You guessed it right! The number was", secret_number)
    else:
        print("Sorry, wrong guess. The secret number was", secret_number)


guess_the_number()


