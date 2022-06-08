import random
import tkinter as tk

welcome_text = '''
      Welcome to the game of Bulls and Cows           
In this game you will try to find the hidden number  
Hidden number consists from 4 digits which not repeat
       You have 15 attempts to find the number'''

def tktk():
    root = tk.Tk()
    root.title("Bulls & Cows")
    root.geometry("720x480")
    welcome_frame = tk.Frame()
    welcome_label = tk.Label(master=welcome_frame, text=welcome_text)
    welcome_label.pack()
    welcome_frame.pack()

    def handle_click(event):
        game()

    button = tk.Button(
        master=welcome_frame,
        text="Start!",
        width=5,
        height=1,
        command=lambda: welcome_frame.pack_forget()
    )
    button.bind("<Button-1>", handle_click)
    button.pack()

    # Run root window's main loop
    root.mainloop()


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


def game():
    print(welcome_text)

    guess = ''.join(random.sample("0123456789", 4))
    tries = 1
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


if __name__ == "__main__":
    tktk()
