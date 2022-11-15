from os import system
from tkinter import BOTTOM, LEFT, RIGHT, TOP, Button, Label, Text, Tk, Y

import pymysql


def run1():
    main.destroy()
    global main2
    main2 = Tk()
    main2.geometry("475x75")
    main2.title("DB Deleter")
    main2.resizable(0, 0)
    main2.config(background="#272727")
    label = Label(
        main2,
        background="#272727",
        foreground="#ffffff",
        text="Do you want to delete all databases(second check)?",
        font=("Arial", 15),
    ).pack()
    but1 = Button(
        main2,
        background="#373737",
        foreground="#ffffff",
        activebackground="#878787",
        activeforeground="#ffffff",
        font=("Arial", 12),
        text="Yes",
        borderwidth=0,
        command=lambda: run2(),
    ).pack(ipadx=30, side=LEFT, padx=10)
    but2 = Button(
        main2,
        background="#373737",
        foreground="#ffffff",
        activebackground="#878787",
        activeforeground="#ffffff",
        font=("Arial", 12),
        text="No",
        borderwidth=0,
        command=lambda: quit(),
    ).pack(ipadx=30, side=RIGHT, padx=10)
    main2.mainloop()


def run2():
    result = []
    main2.destroy()

    def temp(a):
        global inp
        inp = a.get("1.0", "end-1c")
        main3.destroy()

    global inp
    main3 = Tk()
    main3.geometry("400x100")
    main3.title("DB Deleter")
    main3.config(background="#666666")
    l = Label(
        main3,
        background="#272727",
        foreground="#ffffff",
        text="What is the server password?",
        font=("Arial", 15),
    )
    inp = Text(
        main3,
        height=10000,
        width=10000,
        background="#272727",
        foreground="#ffffff",
        borderwidth=0,
        font=("Arial", 15),
        insertbackground="#ffffff",
    )
    but3 = Button(
        main3,
        background="#373737",
        foreground="#ffffff",
        activebackground="#878787",
        activeforeground="#ffffff",
        font=("Arial", 12),
        text="Enter",
        borderwidth=0,
        command=lambda: temp(inp),
    )
    l.pack(side=TOP)
    but3.pack(fill=Y, side=BOTTOM)
    inp.pack()
    main3.mainloop()
    try:
        print(inp)
        conn = pymysql.connect(user="root", host="localhost", password=inp)
    except:
        while True:
            global inp2
            main3 = Tk()
            main3.geometry("400x100")
            main3.title("DB Deleter")
            main3.config(background="#666666")
            l = Label(
                main3,
                background="#272727",
                foreground="#ffffff",
                text="Incorrect password, please type again.",
                font=("Arial", 15),
            )
            inp2 = Text(
                main3,
                height=10000,
                width=10000,
                background="#272727",
                foreground="#ffffff",
                borderwidth=0,
                font=("Arial", 15),
                insertbackground="#ffffff",
            )
            but3 = Button(
                main3,
                background="#373737",
                foreground="#ffffff",
                activebackground="#878787",
                activeforeground="#ffffff",
                font=("Arial", 12),
                text="Enter",
                borderwidth=0,
                command=lambda: temp(inp2),
            )
            l.pack(side=TOP)
            but3.pack(fill=Y, side=BOTTOM)
            inp2.pack()
            main3.mainloop()
            try:
                print(inp)
                conn = pymysql.connect(user="root", host="localhost", password=inp)
                break
            except:
                continue
    cur = conn.cursor()
    cur.execute("show databases")
    res = cur.fetchall()
    for val in res:
        result.append(val[0])
    for db in result:
        if db not in ("information_schema", "performance_schema", "mysql"):
            cur.execute(f"drop database {db}")


main = Tk()
main.geometry("500x75")
main.title("DB Deleter")
main.resizable(0, 0)
main.config(background="#272727")
label = Label(
    main,
    background="#272727",
    foreground="#ffffff",
    text="Do you want to delete all databases(This is irreversible)",
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
    command=lambda: run1(),
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
    command=lambda: quit(),
).pack(ipadx=30, side=RIGHT, padx=10)
main.mainloop()
