print('''
                        ┌──┐─────┌─┐───────┌┐┌─┐────┌─┐
                        │┌┐├┬┬┐┌┐│─┤┌─┐┌─┬┬┘││┌┼─┬┬┬┤─┤
                        │┌┐│││└┤└┼─││┼└┤│││┼││└┤┼│││├─│
                        └──┴─┴─┴─┴─┘└──┴┴─┴─┘└─┴─┴──┴─┘
            ______________________________________________________
            |      Welcome to the game of Bulls and Cows          | 
            |In this game you will try to find the hidden number  |
            |       You have 5 attempts to find the number        |
            |_____________________________________________________|
      ''')

print("1555" == "1555")
userInput = ""
while len(str(userInput)) != 4:
    try:
        userInput = int(input("Choose number of 4 digits: "))
    except ValueError:
        print("Not an integer!")
bulls = 0
cows = 0
tries = 1
while bulls != 4:
    print("Try number ", tries)
    tries += 1
    try_find = input()
    print(try_find == str(userInput))
    print('try_find ', type(try_find))
    print('userInput ', type(userInput))
    if try_find == str(userInput):
        bulls = 4
# print("Congratulations you won the game of bows and Cows")
