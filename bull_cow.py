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
    tk_frame = tk.Frame()
    tk_frame.pack()
    return tk_frame


def create_label(given_frame, label_text):
    """Create label widget for given frame"""
    frame_label = tk.Label(master=given_frame, text=label_text)
    frame_label.pack()


def create_entry():
    """Crete entry widget"""
    global entry
    guess = tk.StringVar()
    entry = tk.Entry(master=game_frame, textvariable=guess)
    entry.pack()
    entry.bind("<Return>", lambda x: check_bull_cow(guess.get()))
    entry.focus()


def start_game(welcome_frame):
    """Removes welcome frame after starting the game"""
    welcome_frame.pack_forget()


def bull_cow_game():
    """Main function that starts with init"""
    global secret, current_guess_count, tries
    root = create_root()
    # TODO remove welcome frame and leave only one frame
    welcome_frame = crate_frame()
    create_label(welcome_frame, welcome_text)

    def handle_click(self):
        game(welcome_frame)

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


def is_valid_guess(guess):
    """Check if user given guess is valid"""
    if len(str(guess)) == 4 and guess.isnumeric():
        return True
    return False


def clear_frame():
    """Clears out all the widgets in given frame"""
    for widgets in game_frame.winfo_children():
        print(widgets)
        widgets.destroy()


def check_bull_cow(guess):
    """Function to check how many Bulls and Cows user gets after answering"""
    global secret, current_guess_count
    if is_valid_guess(guess):
        if secret == guess:
            clear_frame()
            create_label(game_frame, game_win)
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
            create_label(game_frame, f"{bull}A{cow - bull}B")
            game(False)


def game(welcome_frame):
    global secret, current_guess_count, tries, game_frame, game_frame_crated
    if welcome_frame:
        if current_guess_count == 0:
            start_game(welcome_frame)
    if current_guess_count == tries:
        clear_frame()
        create_label(game_frame, f"{game_over} {secret}")
    else:
        if not game_frame_crated:
            game_frame = crate_frame()
            game_frame_crated = True
        label_text = f"Try number {current_guess_count}"
        create_label(game_frame, label_text)
        create_entry()

    # Cheat to know wat is hidden number, uncomment to cheat
    # print("Hidden number was: ", secret)


if __name__ == "__main__":
    bull_cow_game()
