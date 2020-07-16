import random
guess = ''.join(random.sample("0123456789", 4))
tries = 1
print('''
            ______________________________________________________
            |      Welcome to the game of Bulls and Cows          | 
            |In this game you will try to find the hidden number  |
            |Hidden number consists from 4 digits which not repeat|
            |       You have 15 attempts to find the number       |
            |_____________________________________________________|
      ''')


def check_bull_cow(secret, guess):
    bull = 0
    cow = 0
    for i in range(len(secret)):
        if secret[i] in guess:
            cow += 1
        if secret[i] == guess[i]:
            bull += 1
    print(f"{bull}A{cow-bull}B")
    # return f"{bull}A{cow-bull}B"


while tries != 16:
    print("Try number ", tries)
    tries += 1
    try_find = ''
    while len(str(try_find)) != 4:
        try:
            try_find = input()
        except ValueError:
            print("Not an integer!")
    check_bull_cow(guess, try_find)
    if try_find == str(guess):
        print("Congratulations you won the game of Bulls and Cows")
        break
print("Hidden number was: ", guess)
