from tkinter import *
from tkinter import messagebox
import sqlite3

def signup():
    main.destroy()
    import signup

def signin():
    v1 = entry1.get()
    v2 = entry2.get()

    con = sqlite3.connect(("userlist.db"))
    c = con.cursor()

    c.execute("select * from data where Name=? and Password=?",(v1,v2))
    if c.fetchall():
        labelpass.config(fg="green", text="Login success")
        main.destroy()
        import r_machine
    else:
        labelpass.config(fg="red", text="Login fail")



main = Tk()
main.geometry("300x250+500+100")
main.config(bg="#cc99ff")
main.title("Login Page")
main.resizable(0,0)


label0 = Label(main, text="Welcome to Login", width =17, bg="#cc99ff", font=("verdana",20))
label0.pack()

labelrow0 = Frame(main, bg="#cc99ff")
labelrow0.pack(expand= True, fill="both")

label1 = Label(labelrow0, text="Name",bg="#cc99ff", font=("verdana",15))
label1.place(x=10, y=25)

entry1 = Entry(labelrow0)
entry1.place(x=160, y=30)

label1 = Label(labelrow0, text="password ",bg="#cc99ff", font=("verdana",15))
label1.place(x=10, y=85)

entry2 = Entry(labelrow0,show='*')
entry2.place(x=160, y=90)

labelpass = Label(labelrow0, text="Nothing",fg="#cc99ff", bg="#cc99ff",font=("verdana",15))
labelpass.place(x=100,y=120)

btnlogin = Button(labelrow0,text="Login",width="20",command=signin)
btnlogin.place(x=80,y=150)

btnsignup = Button(labelrow0,text="Sign up",width="20",command=signup)
btnsignup.place(x=80,y=180)

main.mainloop()