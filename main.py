from database_interface import *
from statistical_calculations import *
from key_logging import *
import tkinter as tk

black_color = "#121212"
gray_color = "#1E1E1E"
white_color = "#ffffff"
purple_color = "#6200EE"

def create_label(text):
    label = tk.Label(root, text=text, bg=purple_color, fg=white_color, font=40)
    label.pack(fill="x")
    return label

def create_entry():
    entry = tk.Entry(root, bg=gray_color, fg=white_color)
    entry.pack()
    return entry

def create_button(text, function):
    button = tk.Button(root, text=text, bg=gray_color, fg=white_color, command=function)
    button.pack()
    return button

def clear_window():
    for e in root.winfo_children():
        e.destroy()

def render_menu():
    clear_window()
    study_btn = create_button("Study", lambda: enter_name("study"))
    login_btn = create_button("Login", lambda: enter_name("login"))

def render_error(text):
    clear_window()
    label = create_label(text)
    button = create_button("Menu", render_menu)

def submit_phrase(mode, name, times):
    times = remove_brute_errors(times)
    if mode == "study":
        M = expected_value(times)
        D = variance(times, M)
        if check_user(name):
            old_M, old_D = get_user(name)
            M = (old_M + M) / 2
            D = (old_D + D) / 2
        set_user(name, M, D)
    if mode == "login":
        etalon_M, etalon_D = get_user(name)
        if not Fisher_coefficient(etalon_D, times) or not equal_center(etalon_M, etalon_D, times):
            render_error("Incorrect handwriting")
            return
    clear_window()
    label = create_label(f"Successfully {mode} as {name}")
    button = create_button("Menu", render_menu)
        
def enter_phrase(mode, name):
    times = []
    clear_window()
    label = create_label("Phrase (enter 10 chars)")
    entry = create_entry()
    btn = create_button("Start", lambda: measure_times(times))
    button = create_button("Next", lambda: submit_phrase(mode, name, times))

def submit_name(mode, name):
    if mode == "login" and not check_user(name):
        render_error("No such user")
        return
    enter_phrase(mode, name)

def enter_name(mode):
    clear_window()
    label = create_label("Name")
    entry = create_entry()
    button = create_button("Next", lambda: submit_name(mode, entry.get()))

if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap("favicon.png")
    root.title("Super Secure App")
    root.geometry("400x200+400+200")
    root.resizable(False, False)
    root.config(bg=black_color)

    render_menu()

    root.mainloop()
