import random
import tkinter as tk

welcome_text = '''
      Welcome to the game of Bulls and Cows           
In this game you will try to find the hidden number  
Hidden number consists from 4 digits which not repeat
       You have 15 attempts to find the number'''
game_win = "Congratulations you won the game of Bulls and Cows"
game_over = "Sorry but you lost. Right answer was:"
secret = ''.join(random.sample("0123456789", 4))
current_guess_count = 1
tries = 16
game_frame_crated = False


def create_root():
    """Create main root"""
    root = tk.Tk()
    root.title("Bulls & Cows")
    root.geometry("720x480")
    return root


def crate_frame():
    """Create frame widget"""
    global game_frame
    game_frame = tk.Frame()
    game_frame.pack()


def create_label(label_text):
    """Create label widget for given frame"""
    global game_frame
    frame_label = tk.Label(master=game_frame, text=label_text)
    frame_label.pack()


def create_entry():
    """Crete entry widget"""
    global entry
    guess = tk.StringVar()
    entry = tk.Entry(master=game_frame, textvariable=guess)
    entry.pack()
    entry.bind("<Return>", lambda x: check_bull_cow(guess.get()))
    entry.focus()


def bull_cow_game():
    """Main function that starts with init"""
    global secret, current_guess_count, tries
    root = create_root()
    crate_frame()
    create_label(welcome_text)

    button = tk.Button(
        master=game_frame,
        text="Start!",
        width=5,
        height=1,
        command=lambda: game()
    )
    button.pack()

    # Run root window's main loop
    root.mainloop()


def is_valid_guess(guess):
    """Check if user given guess is valid"""
    if len(str(guess)) == 4 and guess.isnumeric():
        return True
    return False


def clear_frame():
    """Clears out all the widgets in given frame"""
    for widgets in game_frame.winfo_children():
        widgets.destroy()


def check_bull_cow(guess):
    """Function to check how many Bulls and Cows user gets after answering"""
    global secret, current_guess_count
    if is_valid_guess(guess):
        if secret == guess:
            clear_frame()
            create_label(game_win)
        else:
            bull = 0
            cow = 0
            for i in range(len(secret)):
                if secret[i] in guess:
                    cow += 1
                if secret[i] == guess[i]:
                    bull += 1
            current_guess_count += 1
            entry.pack_forget()
            create_label(f"{guess}")
            create_label(f"{bull}A{cow - bull}B")
            game()


def game():
    global secret, current_guess_count, tries, game_frame_crated
    if current_guess_count == 1:
        clear_frame()
    if current_guess_count == tries:
        clear_frame()
        create_label(f"{game_over} {secret}")
    else:
        if not game_frame_crated:
            game_frame_crated = True
        label_text = f"Try number {current_guess_count}"
        create_label(label_text)
        create_entry()

    # Cheat to know wat is hidden number, uncomment to cheat
    # print("Hidden number was: ", secret)


if __name__ == "__main__":
    bull_cow_game()
