from tkinter import *
import game
import scoreboard


menu = Tk()
menu.config(bg="white")
menu.attributes("-fullscreen", True)
menu.title("Menu")

title = PhotoImage(file="image/title.png")
start = PhotoImage(file="image/button_play.png")
exit = PhotoImage(file="image/button_exit.png")

def on_game():
    game.game()

def exit_windows():
    menu.destroy()

name_game = Label(menu, image=title, bg="white")
name_game.pack(anchor="center", pady=100)

start_game = Button(menu, image=start, command=on_game, relief="flat", borderwidth=0, bg="white")
start_game.pack(pady=10)
btn_exit = Button(menu, image=exit, command=exit_windows, relief="flat", borderwidth=0, bg="white")
btn_exit.pack(ipadx=20, pady=5)

def open_score():
    scoreboard.score()

btn_top_score = Button(menu, text="Tableau Des Scores", relief="flat", font=("yellowstone", 20), bg="green", fg="white", command=open_score)
btn_top_score.pack(pady=10)

menu.mainloop()