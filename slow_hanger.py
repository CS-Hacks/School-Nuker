from tkinter import LEFT, RIGHT, Button, Label, Tk

planet = "32 ascii char string (=32 bytes)"
blackhole = []
blackhole1 = []
blackhole2 = []
blackhole3 = []
blackhole4 = []
blackhole5 = []
blackhole6 = []
blackhole7 = []


def run():
    main.destroy()
    while True:
        blackhole.append(planet)
        blackhole1.append(planet)
        blackhole2.append(planet)
        blackhole3.append(planet)
        blackhole4.append(planet)
        blackhole5.append(planet)
        blackhole6.append(planet)
        blackhole7.append(planet)


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
