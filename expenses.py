from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.tix import *

from sqlite3 import dbapi2 as sqlite
from datetime import date
from log_maker import *

now = date.today()
month = ['January','February','March','April','May','Jun','July','August','September','October','November','December']


c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()


def addBox():
    global name,rs,entry_frame

    # I use len(all_entries) to get nuber of next free column
    next_row = len(name)


    # add entry in second row
    name.append(Entry(entry_frame,font=("Belwe lt BT",10)))
    name[next_row].grid(row=next_row+1, column=0)
    rs.append(Entry(entry_frame,font=("Belwe lt BT",10)))
    rs[next_row].grid(row=next_row+1, column=1)

	
def delete_row(id,date=0,month=0):
    print(id,date,month)
    success = True

    try:
        sql="delete from expenses where id=%s"%(id)
        cur.execute(sql)
        if date!=0:
            ref(date)
        if month!=0:
            get_expenses_for_month(month)
    except Exception as exp:
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Expenses Successfully Inserted")
        messagebox.showinfo('Successfull', 'Expenses Successfully Inserted')

def get_expenses(date,frame):
    for widget in frame.winfo_children():
        widget.destroy()
    Label(frame,text="----------Expenses of This Date----------",font=("Belwe Bd BT",10),background="white").grid(row=3, column=0,columnspan=3)
    Label(frame,text="Name",font=("Belwe Bd BT",10),background="white").grid(row=4, column=0)
    Label(frame,text="Rs.",font=("Belwe Bd BT",10),background="white").grid(row=4, column=1)
    Label(frame,text="Delete",font=("Belwe Bd BT",10),background="white").grid(row=4, column=2)


    try:
        sql="select * from expenses where adate='%s'" % (date)
        cur.execute(sql)
        i=4
        total = 0
        for result in cur:
            Label(frame,text=result[2],font=("Belwe lt BT",10),background="white").grid(row=i+1, column=0)
            Label(frame,text=result[3],font=("Belwe lt BT",10),background="white").grid(row=i+1, column=1)
            tk.Button(frame,width=10,text='Delete',command=lambda item=result[0]:delete_row(item,date=date)).grid(row=i+1, column=2)
            i+=1
            total+=float(result[3])
        Label(frame,text="-"*80,font=("Belwe Bd BT",10),background="white").grid(row=i+1, column=0,columnspan=3)
        Label(frame,text="total = ",font=("Belwe Bd BT",10),background="white").grid(row=i+2, column=0)
        Label(frame,text=total,font=("Belwe Bd BT",10),background="white").grid(row=i+2, column=1)
        
    except Exception as exp:
        insert_error(exp)
def ref(date):
    global view_frame
	
    get_expenses(date,view_frame)
	
	
	
def insert_expenses():
    global day,name,rs,date
    success = True
    try:
        for i in range(len(name)):
            print(date,name[i].get(),rs[i].get())
            sql = "insert into expenses(adate,name,rs) values(date('%s'),'%s',%.2f);"% (date,name[i].get(),float(rs[i].get())) 
            cur.execute(sql)
            print(sql)
    except Exception as exp:
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Expenses Successfully Inserted")
        messagebox.showinfo('Successfull', 'Expenses Successfully Inserted')

        ref(date)	
	
def edit(i):
    global editexp,edit_date,view_frame,date,name,rs,entry_frame
  
    date = now.replace(day=i)
    print(date)
    name = []
    rs = []
    edit_date.destroy()
    editexp=Tk()
    editexp.configure(background="white")
    editexp.state("zoomed")

    flag='editexp'
    column_frame = tk.Frame(editexp,background="white")
	
    editexp.title('edit expenses for day '+str(i))
    #editexp.wm_iconbitmap('favicon.ico')
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",10),background="white").grid(row=2, column=0,columnspan=3)

    column_frame.pack()
	
    entry_frame = tk.Frame(editexp,background="white")
    Label(entry_frame,text="Name",font=("Belwe Bd BT",10),background="white").grid(row=0, column=0)
    Label(entry_frame,text="Rs.",font=("Belwe Bd BT",10),background="white").grid(row=0, column=1)

    name.append(Entry(entry_frame,font=("Belwe lt BT",10)))
    name[0].grid(row=1, column=0)
    rs.append(Entry(entry_frame,font=("Belwe lt BT",10)))
    rs[0].grid(row=1, column=1)
    
    entry_frame.pack()
    
    button_frame = tk.Frame(editexp,background="white")
    Label(button_frame,text="",font=("Belwe Bd BT",10),background="white").grid(row=0, column=0)
    tk.Button(button_frame,width=10,font=("Belwe Bd BT",10),text='Add Box',command=addBox).grid(row=1, column=0)
    tk.Button(button_frame,width=10,font=("Belwe Bd BT",10),text='Insert',command=insert_expenses).grid(row=1, column=2)
    tk.Button(button_frame,width=20,font=("Belwe Bd BT",10),text='Return to Main Menu',command=editexp.destroy).grid(row=1, column=4)
	
    button_frame.pack()
    try:
        sw= ScrolledWindow(editexp)
        sw.pack()
    except Exception as exp:
        insert_error(exp)
    view_frame = tk.Frame(sw.window,background="white")

    get_expenses(date,view_frame)

    view_frame.pack(side=TOP,fill=BOTH, expand=1)
	
	
    editexp.mainloop()
    
	
def edit_daylist():
    global edit_date, expdate,c, cur, flag, days
    
    flag='edit_date'
    i=0
    dates = []
    name = []
    rs = []
    ot = []
    paid = []
    edit_date=Tk()
    edit_date.title('Edit_Expenses')
    edit_date.configure(background="white")
    edit_date.state("zoomed")

    heading_frame = tk.Frame(edit_date,background="white")

    Label(heading_frame,text= "Current Month :"+now.strftime("%B"),font=("Belwe Bd BT",10),background="white").grid(row=1, column=0,columnspan=3)
    Label(heading_frame,text= "Today's Date :"+str(now),font=("Belwe Bd BT",10),background="white").grid(row=2, column=0,columnspan=3)
    Label(heading_frame,text='-'*80,font=("Belwe Bd BT",10),background="white").grid(row=4, column=0,columnspan=3)

    heading_frame.pack(side=TOP)
    
    button_frame = tk.Frame(edit_date,background="white")
    k = 1
    for i in range(1,4):
        for j in range(1,11):
            tk.Button(button_frame,width=10,text=k,font=("Belwe lt BT",10),command=lambda item=k:edit(item)).grid(row=i,column=j)
            k+=1
    tk.Button(button_frame,width=10,text=k,font=("Belwe lt BT",10),command=lambda item=k:edit(item)).grid(row=4,column=1)
    
    button_frame.pack()
    tk.Button(edit_date,width=20,text='Return to Main Menu',font=("Belwe Bd BT",10),command=edit_date.destroy).pack(side=BOTTOM)
	
	
    edit_date.mainloop()
    

	
	
def get_expenses_for_month(find):
    global entry_frame
    for widget in entry_frame.winfo_children():
        widget.destroy()

    i = 1
    total = 0
    sql = "select * from expenses where adate like '%s'"%(find)
    print(sql)
    cur.execute(sql)
    Label(entry_frame,text="Name",font=("Belwe Bd BT",10),background="white").grid(row=0, column=1)
    Label(entry_frame,text="Rs.",font=("Belwe Bd BT",10),background="white").grid(row=0, column=2)
    Label(entry_frame,text="Delete",font=("Belwe Bd BT",10),background="white").grid(row=0, column=3)
    for result in cur:
        Label(entry_frame,text=result[2],font=("Belwe lt BT",10),background="white").grid(row=i+1, column=1)
        Label(entry_frame,text=result[3],font=("Belwe lt BT",10),background="white").grid(row=i+1, column=2)
        tk.Button(entry_frame,width=10,text='Delete',font=("Belwe lt BT",10),command=lambda item=result[0]:delete_row(item,month=find)).grid(row=i+1, column=3)
        i+=1
        total += float(result[3])
    Label(entry_frame,text="-"*80,font=("Belwe Bd BT",10),background="white").grid(row=i+1, column=1,columnspan=4)
    Label(entry_frame,text="total = ",font=("Belwe Bd BT",10),background="white").grid(row=i+2, column=1)
    Label(entry_frame,text=total,font=("Belwe Bd BT",10),background="white").grid(row=i+2, column=2)

def view(i):
    global viewdate,name,rs,entry_frame
    viewdate.destroy()
    find = "____-%"+str(i+1)+"-__"
    viewexp=Tk()
    viewexp.configure(background="white")
    viewexp.state("zoomed")

    flag='viewexp'
	
    viewexp.title('View Expenses for month '+str(month[i]))
    #viewexp.wm_iconbitmap('favicon.ico')
    column_frame = tk.Frame(viewexp,background="white")

    Label(column_frame,text='View Expenses',font=("Belwe Bd BT",10),background="white").grid(row=1, column=0,columnspan=3)
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",10),background="white").grid(row=2, column=0,columnspan=3)

    column_frame.pack()
    sw= ScrolledWindow(viewexp)
    sw.pack()

    entry_frame = tk.Frame(sw.window,background="white")
    Label(entry_frame,text="Name",font=("Belwe Bd BT",10),background="white").grid(row=0, column=1)
    Label(entry_frame,text="Rs.",font=("Belwe Bd BT",10),background="white").grid(row=0, column=2)
    Label(entry_frame,text="Delete",font=("Belwe Bd BT",10),background="white").grid(row=0, column=3)

 
    get_expenses_for_month(find)        

    entry_frame.pack(fill=BOTH,expand=1)
	
	
	
    
	
    
	
	
    viewexp.mainloop()
    
	
def view_daylist():
    global viewdate, expdate,c, cur, flag, days
    
    viewdate=Tk()
    viewdate.title('View_Expenses')
    viewdate.configure(background="white")
    viewdate.state("zoomed")

    heading_frame = tk.Frame(viewdate,background="white")

    Label(heading_frame,text= "Current Month :"+now.strftime("%B"),font=("Belwe Bd BT",10),background="white").grid(row=1, column=0,columnspan=3)
    Label(heading_frame,text= "Today's Date :"+str(now),font=("Belwe Bd BT",10),background="white").grid(row=2, column=0,columnspan=3)
    Label(heading_frame,text='-'*80,font=("Belwe Bd BT",10),background="white").grid(row=4, column=0,columnspan=3)

    heading_frame.pack(side=TOP)
	
    column_frame = tk.Frame(viewdate,background="white")
	
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",10),background="white").grid(row=2, column=0,columnspan=3)
	
    
    button_frame = tk.Frame(viewdate,background="white")
    k = 0
    for i in range(1,3):
        for j in range(1,7):
            tk.Button(button_frame,width=10,font=("Belwe Bd BT",10),text=month[k],command=lambda item=k:view(item)).grid(row=i,column=j)
            k+=1
    
    button_frame.pack()
	
    Label(viewdate,background="white").pack()
    tk.Button(viewdate,width=20,font=("Belwe Bd BT",10),text='Return to Main Menu',command=viewdate.destroy).pack(side=BOTTOM)
	
	
    viewdate.mainloop()

def mainmenu():
    global expirychk,editexp
    if flag=='expirychk':
        expirychk.destroy()
    elif flag=="editexp":
        editexp.destroy()
    

