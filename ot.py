from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import dbapi2 as sqlite
from log_maker import *
import time
from tkinter.tix import *
from datetime import date as dat

now = dat.today()

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()




def insert_labour():
    global date,name,hour
    success = True
    try:
        sql = "insert into ot(adate,name,hour) values(date('%s'),'%s',%i)"%(date.get(),name.get(),hour.get())
        print(sql)
        cur.execute(sql)
    except Exception as exp:
        c.rollback()
        success = False
        print(exp)
        insert_error(exp)
    if success:
        c.commit()
        insert_info("ot Successfully Inserted")
        messagebox.showinfo('Successfull', 'OT Successfully Inserted')
        get_ot()	
	
def get_ot():
    global ot_view
	
    for widget in ot_view.winfo_children():
        widget.destroy()
    Label(ot_view,text="-"*80,font=("Belwe Bd BT",10),background="white").grid(row=1,column=1,columnspan=3)
    Label(ot_view,text="Date",font=("Belwe Bd BT",10),background="white").grid(row=2,column=1)
    Label(ot_view,text="Name",font=("Belwe Bd BT",10),background="white").grid(row=2,column=2)
    Label(ot_view,text="Hour",font=("Belwe Bd BT",10),background="white").grid(row=2,column=3)



    try:
        sql = "select adate,name,hour from ot"
        cur.execute(sql)
        i=3
        for result in cur:
            Label(ot_view,text=result[0],font=("Belwe lt BT",10),background="white").grid(row=i,column=1)
            Label(ot_view,text=result[1],font=("Belwe lt BT",10),background="white").grid(row=i,column=2)
            Label(ot_view,text=result[2],font=("Belwe lt BT",10),background="white").grid(row=i,column=3)
            i+=1
    except Exception as exp:
        insert_error(exp)
	
def main():
    global flag,entry_frame,ot_view,date,name,hour
    flag='overtime'

    overtime=Tk()
    overtime.configure(background="white")
    overtime.state("zoomed")
    column_frame = tk.Frame(overtime,background="white")
	
    overtime.title('Over time')
    #overtime.wm_iconbitmap('favicon.ico')
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",10),background="white").grid(row=2, column=0,columnspan=3)



    column_frame.pack()
	
    entry_frame = tk.Frame(overtime,background="white")
    Label(entry_frame,text="Date",font=("Belwe Bd BT",10),background="white").grid(row=0, column=1)
    Label(entry_frame,text="Name",font=("Belwe Bd BT",10),background="white").grid(row=0, column=2)
    Label(entry_frame,text="Hour",font=("Belwe Bd BT",10),background="white").grid(row=0, column=3)

    date = StringVar(entry_frame,value=now)
    name = StringVar(entry_frame)
    hour = IntVar(entry_frame)
    i=0

    date_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=date)
    date_entry.grid(row=1,column=1)

    sql  = "select name from labour_details"
    cur.execute(sql)

    name_choices = [result[0] for result in cur]
    name_option = ttk.OptionMenu(entry_frame, name, *name_choices)
    name_option.grid(row=1,column=2)

    hour_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=hour)
    hour_entry.grid(row=1,column=3)
   
    entry_frame.pack()




   
    button_frame = tk.Frame(overtime,background="white")
    Label(button_frame,text="",font=("Belwe Bd BT",10),background="white").grid(row=0,column=0)
    tk.Button(button_frame,width=10,text='Insert Details',font=("Belwe Bd BT",10),command=lambda:insert_labour()).grid(row=1, column=2)
    tk.Button(button_frame,width=20,text='Return to Main Menu',font=("Belwe Bd BT",10),command=overtime.destroy).grid(row=1, column=4)
    Label(button_frame,background="white").grid(row=2, column=0)
	
    button_frame.pack()
    
    sw= ScrolledWindow(overtime)
    sw.pack()

    ot_view = tk.Frame(sw.window,background="white")
    
    get_ot()
	
	
    ot_view.pack(fill=BOTH, expand=1)
	
    overtime.mainloop()
    
  
def mainmenu():
    if flag=='expirychk':
        expirychk.destroy()
    
    

# expiry()
#view_client()