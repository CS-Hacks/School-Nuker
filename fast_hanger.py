from os import system
from tkinter import LEFT, RIGHT, Button, Label, Tk


def run():
    main.destroy()
    while True:
        system("start")


def exitter():
    quit()


main = Tk()
main.geometry("325x75")
main.title("Crasher")
main.resizable(0, 0)
main.config(background="#272727")
label = Label(
    main,
    background="#272727",
    foreground="#ffffff",
    text="Do you want to Hang the system?",
    font=("Arial", 15),
).pack()
but1 = Button(
    main,
    background="#373737",
    foreground="#ffffff",
    activebackground="#878787",
    activeforeground="#ffffff",
    font=("Arial", 12),
    text="Yes",
    borderwidth=0,
    command=lambda: run(),
).pack(ipadx=30, side=LEFT, padx=10)
but2 = Button(
    main,
    background="#373737",
    foreground="#ffffff",
    activebackground="#878787",
    activeforeground="#ffffff",
    font=("Arial", 12),
    text="No",
    borderwidth=0,
    command=lambda: exitter(),
).pack(ipadx=30, side=RIGHT, padx=10)
main.mainloop()
