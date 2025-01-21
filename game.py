from tkinter import *
from random import *
import pygame

def game():

    global dessin, launch, balle1, dx, dy, brick1, vie_num, btnvie, tab_brick, tab_live_brick, numbrick, score
    dessin = None
    int = Toplevel()
    int.config(bg="white")
    int.attributes("-fullscreen", True)
    int.title("game")

    pygame.mixer.init()
    pygame.mixer.music.load("musique/GOREBone_Craquements-d-os-2-_ID-1408__LS.ogg")
    pygame.mixer.music.set_volume(0.5)


    btn_play = PhotoImage(file="image/button_play.png")
    picture_life1 = PhotoImage(file="image/life_1.png")
    picture_life2 = PhotoImage(file="image/life_2.png")
    picture_life3 = PhotoImage(file="image/life_3.png")

    state = 0

    global nb_score
    nb_score = 0

    def create_life():
        global tab_life
        tab_life = []
        for i in range(5):
            life = dessin.create_oval(60, 60, 60, 60, fill="red")
            dessin.moveto(life, 300, 400 + (i * 60))
            tab_life.append(life)

    def create_brick():
        global tab_brick, tab_live_brick, nb_score, score, brick_life
        tab_brick = []
        tab_live_brick = []
        for x in range(9):
            for i in range(9):
                brick_life = randint(1, 5)
                tab_live_brick.append(brick_life)
                if brick_life == 5:
                    brick = dessin.create_rectangle(i * 55, x * 20, (i + 1) * 55, (x + 1) * 20, fill="blue")
                    tab_brick.append(brick)

                if brick_life == 4:
                    brick = dessin.create_rectangle(i * 55, x * 20, (i + 1) * 55, (x + 1) * 20, fill="green")
                    tab_brick.append(brick)

                if brick_life == 3:
                    brick = dessin.create_rectangle(i * 55, x * 20, (i + 1) * 55, (x + 1) * 20, fill="pink")
                    tab_brick.append(brick)

                if brick_life == 2:
                    brick = dessin.create_rectangle(i * 55, x * 20, (i + 1) * 55, (x + 1) * 20, fill="purple")
                    tab_brick.append(brick)

                if brick_life == 1:
                    brick = dessin.create_rectangle(i * 55, x * 20, (i + 1) * 55, (x + 1) * 20, fill="yellow")
                    tab_brick.append(brick)


    def move(*args):
        global state, dessin, dx, dy, vie_num, tab_brick, numbrick, launch, tab_live_brick, nb_score, score, brick_life
        colors = ["yellow", "purple", "pink", "green", "blue"]

        btn_start.destroy()

        dessin.move(balle1, dx, dy)
        int.after(10, move)

        if dessin.coords(balle1)[3] < 10:
            dy = -dy
        elif dessin.coords(balle1)[2] < 20:
            dx = -dx
        elif dessin.coords(balle1)[2] > 490:
            dx = -dx
        elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
                (dessin.coords(platformbase)[3]) > dessin.coords(balle1)[3])) and (
                (dessin.coords(platformbase)[2] - 10) < dessin.coords(balle1)[2] < (
                dessin.coords(platformbase)[2] + 15)):
            dy = -dy
            dx = 2
        elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
                dessin.coords(balle1)[3] < (dessin.coords(platformbase)[3]))) and (
                (dessin.coords(platformbase)[2] - 55) < dessin.coords(balle1)[2] < (
                dessin.coords(platformbase)[2] - 30)):
            dy = -dy
            dx = -2
        elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
                dessin.coords(balle1)[3] < (dessin.coords(platformbase)[3]))) and (
                (dessin.coords(platformbase)[2] - 50) < dessin.coords(balle1)[2] < (
                dessin.coords(platformbase)[2] + 10)):
            dy = -dy
            dx = 0

        if dessin.coords(balle1)[3] > 600:
            vie_num = vie_num - 1
            dessin.moveto(balle1, 250, 250)
            dx = 0
            dy = 3
            dessin.itemconfig(balle1, fill="white")
            if vie_num == 2:
                label_life.config(image=picture_life2)
            elif vie_num == 1:
                label_life.config(image=picture_life1)
            elif vie_num == 0:
                label_life.destroy()
                enter_name()

        for brick in tab_brick:
            brick_collision = dessin.find_overlapping(*dessin.coords(brick))
            if balle1 in brick_collision:
                dy = -dy
                brick_index = tab_brick.index(brick)
                tab_live_brick[brick_index] -= 1

                if tab_live_brick[brick_index] > 0:
                    color = colors[tab_live_brick[brick_index] - 1]
                    dessin.itemconfig(brick, fill=color)

                    if color == "green":
                        nb_score = nb_score + 200
                        score.config(text=nb_score)

                    if color == "pink":
                        nb_score = nb_score + 300
                        score.config(text=nb_score)

                    if color == "purple":
                        nb_score = nb_score + 500
                        score.config(text=nb_score)

                    if color == "yellow":
                        nb_score = nb_score + 600
                        score.config(text=nb_score)

                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(1)

                else:
                    dessin.delete(brick)
                    tab_brick.remove(brick)
                    tab_live_brick.pop(brick_index)
                    numbrick -= 1

                    nb_score = nb_score + 800
                    score.config(text=nb_score)

                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(1)


                break
            if numbrick <= 0:
                create_brick()
                numbrick = 81
                dx = 0
                dy = 2
                dessin.moveto(balle1, 250, 300)

    def colorbrick(life):
        colors = ["yellow", "purple", "pink", "green", "blue"]

        return colors[life]

    def moveplat(*args):
        if dessin.coords(platformbase)[2] < 500:
            dessin.move(platformbase, 20, 0)

    def moveplat_rev(*args):
        if dessin.coords(platformbase)[0] > 0:
            dessin.move(platformbase, -20, 0)

    def loose():

        global nb_score, score_sql

        frame_loose = Frame(int, bg="white")
        frame_loose.pack()

        frame_score = Frame(int, bg="white")
        frame_score.pack()

        Game_over = Label(frame_loose, text="GAME OVER", fg="red", font=("yellowstone", 40), bg="white")
        Game_over.pack(pady=20)

        appel_score = IntVar()
        appel_score.set(nb_score)

        display_score = Label(frame_score, text="Ton Score :", bg="white", fg="black", font=("yellowstone", 20))
        display_score.pack(side="left")

        display_score_number = Label(frame_score, textvariable=appel_score, bg="white", fg="black",font=("yellowstone", 20))

        score_sql = display_score_number.cget("text")

        display_score_number.pack(side="right")

        btn_exit = Button(int, text="EXIT", bg="red", fg="white", command=exit_windows, relief="flat", borderwidth=0, font=("yellowstone", 20), width=10)
        btn_exit.pack(pady=10)


    def enter_name():
        global name_player_label

        dessin.destroy()
        score.destroy()
        btn_frame.destroy()

        def confirme_entry():

            name_player_label.config(text=name_player.get())

            btn_valid_entry.destroy()
            name_player.destroy()

            loose()

        name_player = Entry(int, font=("yellowstone", 20), borderwidth=4, fg="gray", bg="white")
        name_player.pack(pady=10)
        name_player.insert(0, "Entrez votre pseudo...")

        btn_valid_entry = Button(int, command=confirme_entry, relief="flat", borderwidth=0, text="Valider", bg="green", fg="white", font=("yellowstone", 15))
        btn_valid_entry.pack(pady=10)

        name_player_label = Label(int, font=("yellowstone", 20), borderwidth=4, fg="gray", bg="white")
        name_player_label.pack(pady=10)


    def restart_game():
        global state, dessin, launch, balle1, dx, dy, brick1, vie_num, btnvie, tab_brick, numbrick, nb_score

        int.destroy()

        state = 0
        nb_score = 0
        dessin = None
        launch = None
        balle1 = None
        dx = 0
        dy = 0
        brick1 = None
        vie_num = 0
        btnvie = None
        tab_brick = []
        numbrick = 0

        btn_frame.destroy()

        game()


    def exit_windows():
        int.destroy()


    score = Label(int, background="black", borderwidth=4, width=5, text=nb_score, fg="white",font=("yellowstone", 20),)
    score.pack(side="top")

    dessin = Canvas(int, bg="black", width=500, height=600)
    dx = 0
    dy = 2
    balle1 = dessin.create_oval(5, 5, 15, 15, fill='white')
    create_life()
    create_brick()

    numbrick = 81
    vie_num = 3
    platformbase = dessin.create_rectangle(80, 30, 20, 20, fill="red")
    border_left = dessin.create_rectangle(30, 750, 20, 20, fill="cyan")
    border_right = dessin.create_rectangle(30, 750, 20, 20, fill="cyan")

    dessin.moveto(platformbase, 220, 500)
    dessin.moveto(balle1, 250, 250)
    dessin.moveto(border_left, 0, 0)
    dessin.moveto(border_right, 491, 0)

    int.bind("<Right>", moveplat)
    int.bind("<Left>", moveplat_rev)

    dessin.pack()

    btn_frame = Frame(int, bg="white")
    btn_frame.pack()

    btn_restart = Button(btn_frame, bg="orange", fg="white", text="RESTART", command=restart_game, relief="flat", borderwidth=0, font=("yellowstone", 20), width=10)
    btn_restart.pack(side= "left", padx=20, pady=10)
    btn_exit = Button(btn_frame, text="EXIT", bg="red", fg="white", command=exit_windows, relief="flat", borderwidth=0, font=("yellowstone", 20), width=10)
    btn_exit.pack(side="right", padx=20, pady=10)

    label_life = Label(int, image=picture_life3, bg="white")
    label_life.pack()

    btn_start = Button(int, text="LANCER", bg="white", fg="black", command=move, relief="flat", borderwidth=0, font=("yellowstone", 20), width=10)
    btn_start.pack()

    int.mainloop()