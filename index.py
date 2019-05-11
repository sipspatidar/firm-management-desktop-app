from tkinter import *
import tkinter as tk
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk, Image
from tkinter.ttk import *
from log_maker import *
from datetime import date,timedelta
from tkinter import messagebox
login=sqlite.connect("aquatech.sqlite")
l=login.cursor()
WinStat = ''

now = date.today()
today_date = now
yesterday = now-timedelta(days=1)
y = yesterday
last_fifteen = now-timedelta(days=15)
f = last_fifteen
def freport():
    application.destroy()
    
#    login.close()
    
    import mreport
    a = mreport.main()
    
    open_win()
def future_choice():
    application.destroy()
    
#    login.close()
    
    import future_choice
    a = future_choice.main()
    
    open_win()

def payas():
    application.destroy()
    
#    login.close()
    
    import payas
    a = payas.main()
    
    open_win()

def oras():
    application.destroy()
    
#    login.close()
    
    import oras
    a = oras.main()
    
    open_win()

def gram_34():
    application.destroy()
    
#    login.close()
    
    import grams_34
    a = grams_34.main()
    
    open_win()

def dailyincome():
    
    application.destroy()
    
#    login.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    open_win()    
    
def edit_expenses():
    
    application.destroy()
    
#    login.close()
    
    import expenses
    a = expenses.edit_daylist()
    
    open_win()

def view_expenses():
    
    application.destroy()
    
#    login.close()
    
    import expenses
    a = expenses.view_daylist()
    
    open_win()
    

def labour_details():
    
    application.destroy()
#    login.close()
    
    import labour
    a = labour.add_labour()
    
    open_win()

def attendance():
    
    application.destroy()
#    login.close()
    
    import attendance_register
    a = attendance_register.main()
    
    open_win()
def ot():
    
    application.destroy()
#    login.close()
    
    import ot
    a = ot.main()
    
    open_win()

def labour_payment():
    
    application.destroy()
#    login.close()
    
    import make_payment
    a = make_payment.main()
    
    open_win()

def add_clients():
    
    application.destroy()
#    login.close()
    
    import clients
    a = clients.add_client()
    
    open_win()

def view_clients():
    
    application.destroy()
#    login.close()
    
    import clients
    a = clients.view_client()
    
    open_win()


def create_account():
    root.destroy()
    
    ''' Opens Create Window '''
    global create_window, WinStat, un, pwd, question_var, ans
    WinStat='create_window'
    create_window=Tk()
    create_window.configure(background="white")
    create_window.state("zoomed")
    #create_window.wm_iconbitmap('favicon.ico')

    create_main_frame = tk.Frame(create_window,background="white")

    img = ImageTk.PhotoImage(Image.open('front.png'))
    panel = Label(create_main_frame, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(create_main_frame,text='Enter Details to Create New Account',font=("Belwe lt BT",15),background="white").grid(row=1,column=0,columnspan=5)
    Label(create_main_frame,text='--------------------------------------------------------------',font=("Belwe lt BT",15),background="white").grid(row=3,column=0,columnspan=5)
    Label(create_main_frame, text='Username',font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    un=Entry(create_main_frame,font=("Belwe lt BT",15),width=15)
    un.grid(row=4, column=2)
    Label(create_main_frame, text='Password',font=("Belwe lt BT",15),background="white").grid(row=5, column=1)
    pwd=Entry(create_main_frame,font=("Belwe lt BT",15),width=15, show="*")
    pwd.grid(row=5, column=2)
    
    question_var = StringVar()
    choices = ['Who is your fav. teacher ?',' What is your childhod name?','What is your Birth Place ?','What is your fav. Dish ?']
    question_var.set(choices[1]) # set the default option 
    question = OptionMenu(create_main_frame, question_var, *choices)
    Label(create_main_frame, text="Choose a dish",font=("Belwe lt BT",15), background="white").grid(row = 6, column = 1)
    question.grid(row = 6, column =2)
    
	
    Label(create_main_frame, text='Answer',font=("Belwe lt BT",15),background="white").grid(row=8, column=1)
    ans=Entry(create_main_frame,font=("Belwe lt BT",15),width=15)
    ans.grid(row=8, column=2)
    Label(create_main_frame,text='',font=("Belwe lt BT",15),background="white").grid(row=9,column=0,columnspan=5)
    tk.Button(create_main_frame,text='Create Account',font=("Belwe lt BT",15),command=signup).grid(row=10, column=1)
    tk.Button(create_main_frame,width=6,text='Close',font=("Belwe lt BT",15),command=create_main_frame.destroy).grid(row=10, column=2)
    Label(create_main_frame,text='--------------------------------------------------------------',font=("Belwe lt BT",15),background="white").grid(row=11,column=0,columnspan=5)
    Label(create_main_frame,text='Have Account',font=("Belwe lt BT",15),background="white").grid(row=12,column=0,columnspan=2)
    tk.Button(create_main_frame,text=' Login Here',font=("Belwe lt BT",15),command=again).grid(row=12,column=2)
    Label(create_main_frame,text='--------------------------------------------------------------',font=("Belwe lt BT",15),background="white").grid(row=13,column=0,columnspan=5)
    
    create_main_frame.pack(anchor=CENTER)
    create_window.mainloop()

def signup():
    u=un.get()
    p=pwd.get()
    q=question_var.get()
    a=ans.get()
    result = False
    if u=="" or p=="" or q=="" or a=="":
        messagebox.showwarning("Warning","Fill All The Information First")
    else:
        try:
            sql="insert into user values('%s','%s','%s','%s')" % (u,p,q,a)
            l.execute(sql)
            login.commit()
            result = True
        except:
            result = False

    if result:
        messagebox.showinfo("Success","Account Created")
    else:
        messagebox.showerror("Error","Account cann\t created or username already exist")
def forgot_pass():
    root.destroy()
    
    ''' Opens Create Window '''
    global forgot_window, WinStat, un, question_var, ans
    WinStat='forgot_window'
    forgot_window=Tk()
    forgot_window.configure(background="white")
    forgot_window.state("zoomed")

    #forgot_window.wm_iconbitmap('favicon.ico')

    forgot_main_frame = tk.Frame(forgot_window,background="white")

    img = ImageTk.PhotoImage(Image.open('front.png'))
    panel = Label(forgot_main_frame, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(forgot_main_frame,text='Enter Details to Get Your Password',font=("Belwe lt BT",15),background="white").grid(row=1,column=0,columnspan=5)
    Label(forgot_main_frame,text='--------------------------------------------------------------',font=("Belwe lt BT",15),background="white").grid(row=3,column=0,columnspan=5)
    Label(forgot_main_frame, text='Username',font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    un=Entry(forgot_main_frame,font=("Belwe lt BT",15),width=15)
    un.grid(row=4, column=2)
    
    question_var = StringVar()
    choices = ['Who is your fav. teacher ?',' What is your childhod name?','What is your Birth Place ?','What is your fav. Dish ?']
    question_var.set(choices[1]) # set the default option 
    question = OptionMenu(forgot_main_frame, question_var, *choices)
    Label(forgot_main_frame, text="Choose a dish",font=("Belwe lt BT",15), background="white").grid(row = 6, column = 1)
    question.grid(row = 6, column = 2)
    
	
    Label(forgot_main_frame, text='Answer',font=("Belwe lt BT",15),background="white").grid(row=8, column=1)
    ans=Entry(forgot_main_frame,font=("Belwe lt BT",15),width=15)
    ans.grid(row=8, column=2)
    Label(forgot_main_frame,text='',font=("Belwe lt BT",15),background="white").grid(row=9,column=0,columnspan=5)
    tk.Button(forgot_main_frame,text='Recover Password',font=("Belwe lt BT",15),command=get_pass).grid(row=10, column=1)
    tk.Button(forgot_main_frame,width=6,text='Close',font=("Belwe lt BT",15),command=forgot_main_frame.destroy).grid(row=10, column=2)
    Label(forgot_main_frame,text='--------------------------------------------------------------',font=("Belwe lt BT",15),background="white").grid(row=11,column=0,columnspan=5)
    Label(forgot_main_frame,text='Have Account',font=("Belwe lt BT",15),background="white").grid(row=12,column=0,columnspan=2)
    tk.Button(forgot_main_frame,text=' Login Here',font=("Belwe lt BT",15),command=again).grid(row=12,column=2)
    Label(forgot_main_frame,text='--------------------------------------------------------------',font=("Belwe lt BT",15),background="white").grid(row=13,column=0,columnspan=5)
    
    forgot_main_frame.pack(anchor=CENTER)  
    forgot_window.mainloop()

def get_pass():
    global un, pwd, root,question_var, ans
    u=un.get()
    q=question_var.get()
    a=ans.get()
    password = ""
    if u=="" or  q=="" or a=="":
        messagebox.showwarning("Warning","Please Fill All The Details")
    else:
        try:
            sql="select * from user where username='%s' and question='%s' and answer='%s'" % (u,q,a)
            l.execute(sql)
        except:
            print("")
        count = 0	
        for i in l:  
            password = i[1]		
        if password!="":
            messagebox.showinfo("Information","Your Password is"+password)
        else:
            messagebox.showerror("Error","Wrong information")
	
def again():   
    ''' Main Login Window'''
    global un, pwd, WinStat, root, application,create_window,forgot_window
    if WinStat=='application':
        application.destroy()
    elif WinStat=='create_window':
        create_window.destroy()
    elif WinStat=='forgot_window':
        forgot_window.destroy()
    root=Tk()
    root.title('MP AquaTech PVT. LMT.')
    root.state("zoomed")
    #root.attributes("-fullscreen",'True')
    #root.wm_iconbitmap('favicon.ico')
    root.configure(background="white")
	
    root_frame = tk.Frame(root,background="white")
    img = ImageTk.PhotoImage(Image.open('front.png'))
    panel = Label(root_frame, image = img).grid(row=0, column=0,columnspan=5)
   
    Label(root_frame,text='Enter Details to Login',font=("Belwe Bd BT",20),background="white").grid(row=1,column=0,columnspan=5)
    Label(root_frame,text='--------------------------------------------------------------',background="white").grid(row=3,column=0,columnspan=5)
    Label(root_frame, text='Username : ',font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    un=Entry(root_frame,font=("Belwe lt BT",15),width=15)
    un.grid(row=4, column=2)
    Label(root_frame, text='Password : ',font=("Belwe lt BT",15),background="white").grid(row=5, column=1)
    pwd=Entry(root_frame,font=("Belwe lt BT",15),width=15, show="*")
    pwd.grid(row=5, column=2)
    Label(root_frame,text='',background="white").grid(row=6,column=0,columnspan=5)
    login_button = tk.Button(root_frame,width=6,font=("Belwe lt BT",15),text='Login',command=check)
    login_button.grid(row=7, column=1)
	
    tk.Button(root_frame,width=6,text='Close',font=("Belwe lt BT",15),command=root.destroy).grid(row=7, column=2)
    Label(root_frame,text='--------------------------------------------------------------',background="white").grid(row=8,column=0,columnspan=5)
    tk.Button(root_frame,text='Forgot Password',font=("Belwe lt BT",15),command=forgot_pass).grid(row=9,column=0,columnspan=4)
    Label(root_frame,text='--------------------------------------------------------------',background="white").grid(row=10,column=0,columnspan=5)
    tk.Button(root_frame,text='Create New Account',font=("Belwe lt BT",15),command=create_account).grid(row=11,column=0,columnspan=4)
    Label(root_frame,text='--------------------------------------------------------------',background="white").grid(row=12,column=0,columnspan=5)
    root.bind("<Return>",check)
	
    root_frame.pack(anchor=CENTER)
    root.mainloop()
    
def check(event=None):   
    ''' Check Button for Login Window '''
    global un, pwd, root
    u=un.get()
    p=pwd.get()
    
    if u=="" or p=="":
        messagebox.showwarning('Warning', 'Please Fill all the details')
    else:
        try:
            sql="select * from user where username='%s' and password='%s'" % (u,p)
            l.execute(sql)
        except:
            print("")
        count = 0
        for i in l:
            count+=1		
        if count>0:
            root.destroy()
            #login.close()
            open_win()
        else:
            messagebox.showerror('Error', 'Wrong Username/Password')
	
	
	
   
    
        
    

def open_win(): 
    ''' Opens Main Window '''
    global application, WinStat
    con=sqlite.connect("aquatech.sqlite")
    cur=con.cursor()

    WinStat='application'
    application=Tk()
    #application.wm_iconbitmap('favicon.ico')
  
    application.title("MP AquaTech PVT. LMT.")
    application.geometry("800x400")
    application.configure(background="white")
    application.state("zoomed")

    
    main_frame = tk.Frame(application,background="white")
	
    left_bottle = tk.Frame(main_frame,background="white")
    b_img = ImageTk.PhotoImage(Image.open('bottle.png'))
    panel = Label(left_bottle, image = b_img).pack(fill=BOTH,expand=1)
    left_bottle.grid(row=0,column=0,sticky="N")

    app_frame = tk.Frame(main_frame,background="white")
    ''' Main Window Picture '''
    img = ImageTk.PhotoImage(Image.open('collage.jpg'))
    panel = Label(app_frame, image = img).grid(row=0, column=0,columnspan=8)
    
    menu_bar = Menu(app_frame)
    bottle = Menu(menu_bar,tearoff=0)
    labour = Menu(menu_bar,tearoff=0)
    manage_clients = Menu(menu_bar,tearoff=0)
    expenses = Menu(menu_bar,tearoff=0)
    report = Menu(menu_bar,tearoff=0)
    '''Stock Maintainance'''
    bottle.add_command(label="Future Choice", command=future_choice)
    bottle.add_command(label="Payas", command=payas)
    bottle.add_command(label="Oras", command=oras)
    bottle.add_command(label="34 Grams", command=gram_34)
    '''Expiry Check'''
    labour.add_command(label="Labour Details", command=labour_details)
    labour.add_command(label="Attendance", command=attendance)
    labour.add_command(label="Over Time", command=ot)
    labour.add_command(label="Salary", command=labour_payment)
    '''Billing'''
    expenses.add_command(label="Enter Expenses", command=edit_expenses)
    expenses.add_command(label="View Expenses", command=view_expenses)
    '''Billing'''
    manage_clients.add_command(label="Add Clients", command=add_clients)
    manage_clients.add_command(label="View Clients", command=view_clients)

    
    menu_bar.add_cascade(label="Bottle", menu=bottle)
    menu_bar.add_cascade(label="Labour", menu=labour)
    menu_bar.add_cascade(label="Expenses", menu=expenses)
    menu_bar.add_cascade(label="Manage Clients", menu=manage_clients)
    menu_bar.add_cascade(label="Report",command=freport)
    menu_bar.add_cascade(label="Logout",command=again)
    application.config(menu=menu_bar)
    
    
    last_expenses = tk.Frame(app_frame,bg="white")
    tk.Label(last_expenses,background="white",font=("Belwe Bd BT",20),text="Last Day Expenses",fg="blue").grid(row=1, column=1,columnspan=2)
    sql = "select * from expenses where adate='%s'"%(y)
    print(sql)
    cur.execute(sql)
    i=3
    total = 0
    for result in cur:
    
        Label(last_expenses,background="white",font=("Belwe lt BT",15),text=result[2]).grid(row=i, column=1)
        Label(last_expenses,background="white",font=("Belwe lt BT",15),text=result[3]).grid(row=i, column=2)
        i+=1
        total += result[3]
    Label(last_expenses,background="white",font=("Belwe Bd BT",15),text="-"*40).grid(row=i, column=1,columnspan=2)
    Label(last_expenses,background="white",font=("Belwe Bd BT",15),text="Total =  ").grid(row=i+1, column=1)
    Label(last_expenses,background="white",font=("Belwe Bd BT",15),text=total).grid(row=i+1, column=2)
    last_expenses.grid(row=1,column=0,columnspan=2,sticky="N")


    last_sell = tk.Frame(app_frame,bg="white")
    tk.Label(last_sell,text="Last Day Sell",font=("Belwe Bd BT",20),background="white",fg="blue").grid(row=0, column=0,columnspan=3)
    sql = "select * from sell where adate='%s'"%(y)
    print(sql)
    cur.execute(sql)
    i=3
    total = 0
    for result in cur:
    
        Label(last_sell,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i, column=0)
        Label(last_sell,text=result[6],font=("Belwe lt BT",15),background="white").grid(row=i, column=1)
        Label(last_sell,text=result[7],font=("Belwe lt BT",15),background="white").grid(row=i, column=2)
        i+=1
        total += result[6]
    Label(last_sell,text="-"*40,font=("Belwe Bd BT",15),background="white").grid(row=i, column=0,columnspan=3)
    Label(last_sell,text="Total",font=("Belwe Bd BT",15),background="white").grid(row=i+1, column=0)
    Label(last_sell,text=" = ",font=("Belwe Bd BT",15),background="white").grid(row=i+1, column=1)
    Label(last_sell,text=total,font=("Belwe Bd BT",15),background="white").grid(row=i+1, column=2)
    last_sell.grid(row=1,column=2,columnspan=3,sticky="N")

    not_paid = tk.Frame(app_frame,background="white")
    tk.Label(not_paid,text="Payment Pending",font=("Belwe Bd BT",20),background="white",fg="blue").grid(row=1, column=0,columnspan=3)
    sql = "select * from sell where date(adate)<=date('%s') and paid='not paid' order by adate"%(f)
    print(sql)
    cur.execute(sql)
    i=3
    total = 0
    for result in cur:
    
        Label(not_paid,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i, column=0)
        Label(not_paid,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i, column=1)
        Label(not_paid,text=result[6],font=("Belwe lt BT",15),background="white").grid(row=i, column=2)
        i+=1
    Label(not_paid,text="-"*40,font=("Belwe Bd BT",15),background="white").grid(row=i, column=0,columnspan=3)
    not_paid.grid(row=1,column=5,columnspan=3,sticky="N")


    app_frame.grid(row=0,column=1,sticky="N")

    right_bottle = tk.Frame(main_frame,background="white")
    r_img = ImageTk.PhotoImage(Image.open('bottle.png'))
    panel = Label(right_bottle, image = r_img, relief=FLAT).pack(fill=BOTH,expand=1)
    right_bottle.grid(row=0,column=2,sticky="N")
	
    main_frame.pack(anchor=CENTER)
        
    application.mainloop()

    

def check_db():
    
    try:
        l.execute("CREATE TABLE IF NOT EXISTS user(username varchar(50) not null primary key,password varchar(50) not null,question varchar(50) not null,answer varchar(50) not null);")
        l.execute("CREATE TABLE IF NOT EXISTS 'payment' ('adate' date NOT NULL,'rs' int(11) NOT NULL,'remark' text NOT NULL,'type' text NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'clients' ('id' integer PRIMARY KEY AUTOINCREMENT,'name' text NOT NULL,'address' text NOT NULL,'mobile' int(12) NOT NULL,'phone' int(12) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'expenses'( 'id' integer PRIMARY KEY AUTOINCREMENT,'adate' date NOT NULL, 'name' text NOT NULL,'rs' double NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'ot'( 'adate' date NOT NULL, 'name' text NOT NULL,'hour' int(2) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'labour_payment' ('adate' date NOT NULL,'name' text NOT NULL,'rs' decimal(10,0) NOT NULL,'ot' decimal(10,0) NOT NULL,'total' decimal(10,0) NOT NULL,'shift' int(1) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'labour_attendance' ('name' text NOT NULL,'Jun' text NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'labour_details' ('name' text NOT NULL,'other' text NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'production' ('adate' date NOT NULL,'tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'production_payas' ('adate' date NOT NULL,'tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'production_oras' ('adate' date NOT NULL,'tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'production_34gram' ('adate' date NOT NULL,'tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'raw_material' ('id' integer PRIMARY KEY AUTOINCREMENT,'adate' date NOT NULL,'raw' text NOT NULL,'type' text NOT NULL,'quantity' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'raw_material_payas' ('id' integer PRIMARY KEY AUTOINCREMENT,'adate' date NOT NULL,'raw' text NOT NULL,'type' text NOT NULL,'quantity' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'raw_material_oras' ('id' integer PRIMARY KEY AUTOINCREMENT,'adate' date NOT NULL,'raw' text NOT NULL,'type' text NOT NULL,'quantity' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'raw_material_34gram' ('id' integer PRIMARY KEY AUTOINCREMENT,'adate' date NOT NULL,'raw' text NOT NULL,'type' text NOT NULL,'quantity' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'sell' ( 'id' integer PRIMARY KEY AUTOINCREMENT,'adate' date NOT NULL,'client' text NOT NULL,'item' text NOT NULL,'quantity' int(11) NOT NULL,'rate' double NOT NULL,'total' double NOT NULL,'paid' text NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'stock_maintenance'('tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL, 'preform250' int(11) NOT NULL,'preform500' int(11) NOT NULL,'preform1000' int(11) NOT NULL,'lable250' int(11) NOT NULL,'lable500' int(11) NOT NULL,'lable1000' int(11) NOT NULL,'caps250' int(11) NOT NULL,'caps500' int(11) NOT NULL,'caps1000' int(11) NOT NULL,'boxes250' int(11) NOT NULL,'boxes500' int(11) NOT NULL,'boxes1000' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'stock_maintenance_payas'('tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL, 'preform250' int(11) NOT NULL,'preform500' int(11) NOT NULL,'preform1000' int(11) NOT NULL,'lable250' int(11) NOT NULL,'lable500' int(11) NOT NULL,'lable1000' int(11) NOT NULL,'caps250' int(11) NOT NULL,'caps500' int(11) NOT NULL,'caps1000' int(11) NOT NULL,'boxes250' int(11) NOT NULL,'boxes500' int(11) NOT NULL,'boxes1000' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'stock_maintenance_oras'('tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL, 'preform250' int(11) NOT NULL,'preform500' int(11) NOT NULL,'preform1000' int(11) NOT NULL,'lable250' int(11) NOT NULL,'lable500' int(11) NOT NULL,'lable1000' int(11) NOT NULL,'caps250' int(11) NOT NULL,'caps500' int(11) NOT NULL,'caps1000' int(11) NOT NULL,'boxes250' int(11) NOT NULL,'boxes500' int(11) NOT NULL,'boxes1000' int(11) NOT NULL)")
        l.execute("CREATE TABLE IF NOT EXISTS 'stock_maintenance_34gram'('tf' int(11) NOT NULL,'fh' int(11) NOT NULL,'ts' int(11) NOT NULL, 'preform250' int(11) NOT NULL,'preform500' int(11) NOT NULL,'preform1000' int(11) NOT NULL,'lable250' int(11) NOT NULL,'lable500' int(11) NOT NULL,'lable1000' int(11) NOT NULL,'caps250' int(11) NOT NULL,'caps500' int(11) NOT NULL,'caps1000' int(11) NOT NULL,'boxes250' int(11) NOT NULL,'boxes500' int(11) NOT NULL,'boxes1000' int(11) NOT NULL)")
        l.execute("select * from stock_maintenance")

        if l.fetchone() is None:
            l.execute("insert into stock_maintenance values(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)")

        l.execute("select * from stock_maintenance_payas")

        if l.fetchone() is None:
            l.execute("insert into stock_maintenance_payas values(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)")

        l.execute("select * from stock_maintenance_oras")

        if l.fetchone() is None:
            l.execute("insert into stock_maintenance_oras values(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)")
            
        l.execute("select * from stock_maintenance_34gram")

        if l.fetchone() is None:
            l.execute("insert into stock_maintenance_34gram values(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)")
            
        login.commit()
        insert_info("Datebase Created Successfully or Already Exist")
        
    except Exception as exp:
        insert_error(exp)	
        
    
    
    
check_db()  
again()