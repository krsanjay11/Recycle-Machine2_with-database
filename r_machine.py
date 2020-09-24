from tkinter import *
import sqlite3

val = 0
val = round(val, 2)
cal1, cal2, cal3, m, n, o = 0, 0, 0, 0, 0, 0


def can():
    can = Tk()
    can.geometry("350x250+500+200")
    can.config(bg="#fae5d3")
    can.resizable(0, 0)
    can.title("Can")

    def ok():
        can.destroy()

    def cal():
        global val
        global cal1
        global m
        a = int(lb_Enter.get())
        cal = a * 2.80
        cal = round(cal, 2)
        val += cal
        cal1 += cal
        cal1 = round(cal1, 2)
        m += a
        val = round(val, 2)
        p = str(val)
        lbl_total.config(text=("Rs. " + p),fg='BLACK')
        cal11 = str(cal)
        lbl2.config(text="Rs. " + cal11,fg="blue")

    lb1s = Label(can, text="   Enter the Quantity of can   ", bg="blue", fg="white", font=("verdana", 18))
    lb1s.place(x=0, y=0)

    price = Label(can, text=" Cost -  Rs.2.80 per Can each", bg="#fae5d3", fg="Black", font=("verdana", 14))
    price.place(x=30, y=35)

    lb = Label(can, text="Enter value ", bg="#fae5d3", fg="blue", font=("verdana", 18))
    lb.place(x=90, y=65)

    lb_Enter = Entry(can)
    lb_Enter.place(x=100, y=110)

    btn = Button(can, text=" Enter ", command=cal)
    btn.pack()
    btn.place(x=140, y=137)

    lbl1 = Label(can, text="Amount added  ", bg="#fae5d3", fg="black", font=("verdana", 16))
    lbl1.place(x=40, y=170)

    lbl2 = Label(can, text='Rs. 0.0', bg="#fae5d3", fg="black", font=("verdana", 16))
    lbl2.place(x=205, y=170)

    btn_ok = Button(can, text=" Continue ", command=ok)
    btn_ok.pack()
    btn_ok.place(x=130, y=210)


def bottle():
    bottle = Tk()
    bottle.geometry("350x250+500+200")
    bottle.config(bg="#fae5d3")
    bottle.resizable(0, 0)
    bottle.title("Bottle")

    def ok():
        bottle.destroy()

    def cal():
        global val
        global cal2
        global n
        a = int(lb_Enter.get())
        cal = a * 2.10
        cal = round(cal, 2)
        val += cal
        cal2 += cal
        cal2 = round(cal2, 3)
        n += a
        val = round(val, 2)
        p = str(val)
        lbl_total.config(text=("Rs. " + p),fg='BLACK')
        cal22 = str(cal)
        lbl2.config(text="Rs. " + cal22,fg="blue")

    lb1 = Label(bottle, text=" Enter the Quantity of Bottle  ", bg="blue", fg="white", font=("verdana", 18))
    lb1.place(x=0, y=0)

    price = Label(bottle, text=" Cost -  Rs.2.10 per Bottle each", bg="#fae5d3", fg="Black", font=("verdana", 14))
    price.place(x=30, y=35)

    lb = Label(bottle, text="Enter value ", bg="#fae5d3", fg="blue", font=("verdana", 18))
    lb.place(x=90, y=65)

    lb_Enter = Entry(bottle)
    lb_Enter.place(x=100, y=110)

    btn = Button(bottle, text=" Enter ", command=cal)
    btn.pack()
    btn.place(x=140, y=137)

    lbl1 = Label(bottle, text="Amount added      ", bg="#fae5d3", fg="black", font=("verdana", 16))
    lbl1.place(x=40, y=170)

    lbl2 = Label(bottle, text='Rs. 0.0', bg="#fae5d3", fg="black", font=("verdana", 16))
    lbl2.place(x=205, y=170)

    btn_ok2 = Button(bottle, text=" Continue ", command=ok)
    btn_ok2.pack()
    btn_ok2.place(x=130, y=210)


def paper():
    paper = Tk()
    paper.geometry("350x250+500+200")
    paper.config(bg="#fae5d3")
    paper.resizable(0, 0)
    paper.title("Paper")

    def ok():
        paper.destroy()

    def cal():
        global val
        global cal3
        global o
        a = int(lb_Enter.get())
        cal = a * 4.20
        cal = round(cal, 2)
        val += cal
        cal3 += cal
        cal3 = round(cal3)
        o += a
        val = round(val, 2)
        p = str(val)
        lbl_total.config(text=("Rs. " + p),fg="black")
        cal33 = str(cal)
        lbl2.config(text=("Rs. " + cal33),fg="blue")

    lb1 = Label(paper, text=" Enter the Quantity of Paper  ", bg="blue", fg="white", font=("verdana", 18))
    lb1.place(x=0, y=0)

    price = Label(paper, text=" Cost -  Rs.4.20 per Paper each", bg="#fae5d3", fg="Black", font=("verdana", 14))
    price.place(x=30, y=35)

    lb = Label(paper, text="Enter value ", bg="#fae5d3", fg="blue", font=("verdana", 18))
    lb.place(x=90, y=65)

    lb_Enter = Entry(paper)
    lb_Enter.place(x=100, y=110)

    btn = Button(paper, text=" Enter ", command=cal)
    btn.pack()
    btn.place(x=140, y=137)

    lbl1 = Label(paper, text="Amount added ", bg="#fae5d3", fg="black", font=("verdana", 16))
    lbl1.place(x=40, y=170)

    lbl2 = Label(paper, text='Rs. 0.0 ', bg="#fae5d3", fg="black", font=("verdana", 16))
    lbl2.place(x=205, y=170)

    btn_ok3 = Button(paper, text=" Continue ", command=ok)
    btn_ok3.pack()
    btn_ok3.place(x=130, y=210)


def reciept():
    rec = Tk()
    rec.title("Reciept")
    rec.geometry("390x380+500+150")
    rec.config(bg="#fcf3cf")
    rec.resizable(0, 0)

    def pr():
        rec.destroy()

    lb1 = Label(rec, text="---------       Reciept       ---------", bg="#fcf3cf", fg="black", font=("verdana", 18))
    lb1.place(x=0, y=0)

    lbl1 = Label(rec, text="                                                ", bg="white", fg="black",
                 font=("verdana", 18))
    lbl1.pack(padx=0, pady=30)

    q = m + n + o
    p = str(q)
    j = str(m)
    k = str(n)
    l = str(o)
    cal44 = "Rs. " + str(val)
    cal11 = "Rs. " + str(cal1)
    cal22 = "Rs. " + str(cal2)
    cal33 = "Rs. " + str(cal3)
    lbl_text = Label(lbl1, text=("Total Can(s)            " + j), bg="#a569bd", font=("verdana", 18))
    lbl_text.pack(expand=True, fill="both")

    lbl_total = Label(lbl1, text=("Amount for Cans        " + cal11), bg="silver", font=("verdana", 18))
    lbl_total.pack(expand=True, fill="both")

    lbl_text = Label(lbl1, text=("Total Bottle(s)         " + k), bg="#a569bd", font=("verdana", 18))
    lbl_text.pack(expand=True, fill="both")

    lbl_total = Label(lbl1, text=("Amount for Bottles     " + cal22), bg="silver", font=("verdana", 18))
    lbl_total.pack(expand=True, fill="both")

    lbl_text = Label(lbl1, text=("Total Paper(s)          " + l), bg="#a569bd", font=("verdana", 18))
    lbl_text.pack(expand=True, fill="both")

    lbl_total = Label(lbl1, text=("Amount for Papers      " + cal33), bg="silver", font=("verdana", 18))
    lbl_total.pack(expand=True, fill="both")

    lbl_text = Label(lbl1, text=("Total Item              " + p), bg="#a569bd", font=("verdana", 18))
    lbl_text.pack(expand=True, fill="both")

    lbl_total = Label(lbl1, text="Total Amount Added ", bg="white", font=("verdana", 18))
    lbl_total.pack(expand=True, fill="both")

    lbl_total = Label(lbl1, text=cal44, bg="white", font=("verdana", 18))
    lbl_total.pack(expand=True, fill="both")

    btn = Button(rec, text="OK", command=pr)
    btn.pack()
    btn.place(x=170, y=350)


def exit():
    q = m + n + o
    p = str(q)
    j = str(m)
    k = str(n)
    l = str(o)
    cal44 = "Rs. " + str(val)
    cal11 = "Rs. " + str(cal1)
    cal22 = "Rs. " + str(cal2)
    cal33 = "Rs. " + str(cal3)

    con = sqlite3.connect(("recyclelist.db"))
    c = con.cursor()
    # updater = "create table if not exists list(Can int, Can_amount int, Bottle int, Bottle_amount int,Paper int,Papar_amount int,Quantity int,Total_amount int)"
    # updater = "delete from data where Name ='sanjayd'"
    c.execute("insert into list(Can,Can_amount,Bottle,Bottle_amount,Paper,Papar_amount,Quantity,Total_amount) values(?,?,?,?,?,?,?,?)", (j,cal11,k,cal22,l,cal33,p,cal44))
    # c.execute(updater)
    con.commit()
    root.destroy()


root = Tk()
root.geometry("300x300+500+150")
root.resizable(100, 100)
root.title("Recycle Machine")

lbl = Label(root, text="  ", font=("verdana", 18), background="#82e0aa", fg='#000000')
lbl.pack(expand=True, fill="both")

lb = Label(lbl, text="Recycle Machine", bg="#82e0aa",fg="#004d40", font=("verdana", 22,),)
lb.pack(expand=True, fill="both")

lb = Label(lbl, text="Save Environment Save Earth", bg="#82e0aa", font=("verdana", 12))
lb.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root, bg="#ffffff")
btnrow2.pack(expand=True, fill="both")

lb2 = Label(root, text="   ", bg="#f000ff", font=("verdana", 18))
lb2.pack(expand=True, fill="both")

lbl_text = Label(lb2, text="Total Balance: ", bg="#82e0aa", font=("verdana", 18))
lbl_text.pack(expand=True, fill="both")

lbl_total = Label(lb2, text=" Rs. 0.0 ", bg="#82e0aa",fg="white", font=("verdana", 18))
lbl_total.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text=" Can ",
    bg="#d7dbdd",
    font=("verdana", 22),
    relief=RIDGE,
    border=1,
    command=can
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="Bottle",
    bg="#d7dbdd",
    font=("verdana", 22),
    relief=RIDGE,
    border=1,
    command=bottle
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn1 = Button(
    btnrow2,
    text="Paper",
    bg="#d7dbdd",
    font=("verdana", 22),
    relief=RIDGE,
    border=1,
    command=paper
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow2,
    text="Exit    ",
    bg="#D7dbdd",
    font=("verdana", 22),
    relief=RIDGE,
    border=1,
    command=exit
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn_r = Button(
    lb2,
    text="Print Reciept",
    bg="#d7dbdd",
    font=("verdana", 14),
    relief=RIDGE,
    border=1,
    command=reciept
)
btn_r.pack(side=RIGHT, expand=True, fill="both")

root.mainloop()
