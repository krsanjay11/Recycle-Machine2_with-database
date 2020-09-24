from tkinter import *
from tkinter import messagebox
import sqlite3

def signup():

    con = sqlite3.connect(("userlist.db"))
    c = con.cursor()
    v1= entry1.get()
    v2= entry2.get()
    v3= entry3.get()
    v4= entry4.get()
    if v1 and v2 and v3 and v4:
        # updater = "create table if not exists Data(Name text, Email text, Password int, Mobile int)"
        # updater = "delete from data where Name ='sanjayd'"
        c.execute("insert into data(Name,Email,Password,Mobile) values(?,?,?,?)",(v1,v2,v3,v4))
        # c.execute(updater)
        con.commit()

        messagebox.askokcancel("Message", "Signup Successful")
        main.destroy()
        import signin
    else:
        messagebox.showerror("Error","Enter all values")

main = Tk()
main.geometry("300x300+500+100")
main.config(bg="#82e0aa")
main.title("Registration form")
main.resizable(0,0)

label0 = Label(main, text="Registration form", width =20, bg="#82e0aa", font=("verdana",20))
label0.pack()

labelrow0 = Frame(main, bg="#82e0aa")
labelrow0.pack(expand= True, fill="both")

label1 = Label(labelrow0, text="Full Name",bg="#82e0aa", font=("verdana",15))
label1.place(x=10, y=25)

entry1 = Entry(labelrow0)
entry1.place(x=160, y=30)

label1 = Label(labelrow0, text="Email ",bg="#82e0aa", font=("verdana",15))
label1.place(x=10, y=85)

entry2 = Entry(labelrow0)
entry2.place(x=160, y=90)

labelrow1 = Frame(main, bg="#82e0aa")
labelrow1.pack(expand= True, fill="both")


label3 = Label(labelrow1, text="Password",bg="#82e0aa", font=("verdana",15))
label3.place(x=10, y=5)

entry3 = Entry(labelrow1)
entry3.place(x=160, y=10)

label4 = Label(labelrow1, text="Mobile No. ", bg="#82e0aa",font=("verdana",15))
label4.place(x=10, y=55)

entry4 = Entry(labelrow1)
entry4.place(x=160, y=60)

btnenter = Button(labelrow1,text="Sign up",width="20",command=signup)
btnenter.place(x=80,y=100)

main.mainloop()