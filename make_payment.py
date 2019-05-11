from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter.tix import *
import pickle

from tkinter import messagebox
from datetime import date
from sqlite3 import dbapi2 as sqlite
from log_maker import *
from datetime import date as dat

now = dat.today()


month = ['January','February','March','April','May','Jun','July','August','September','October','November','December']
aaa = date.today()

cmonth = month[aaa.month-1]


columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()




def insert_client():
    global dates,name,rs,ot,total
    success = True
    try:
        for i in range(len(name)):
            sql = "insert into labour_payment(adate,name,rs,ot,total) values('%s','%s',%s,%s,%s)"%(dates[i].get(),name[i].get(),rs[i].get(),ot[i].get(),total[i].get())
            cur.execute(sql)
    except Exception as exp:
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Labour Payment Successfully Inserted")
        messagebox.showinfo('Successfull', 'Labour Payment Successfully Inserted')
def load_pickle():
    global total_temp
    total_temp = {}
    try:
        pickle_read = open("dict.pickle","rb")
        dict_temp = pickle.load(pickle_read)
        total_temp = pickle.load(pickle_read)
        pickle_read.close()
        #print(dict)
    except Exception as exp:
        print(exp)
        insert_error(exp)
    print(total_temp)

def calculate():
    global days,ot,rate,total
    total.set((days.get()*rate.get())+(round((ot.get()/10)*rate.get(),2)))

def update_values(*args):
    global name,days,ot,cmonth,total_temp
    print(name.get(),total_temp[cmonth][name.get()])
    sql  = "select sum(hour) from ot where name='%s'"%(name.get())
    cur.execute(sql)
    h = cur.fetchone()	
    days.set(total_temp[cmonth][name.get()])
    ot.set(h[0])
	
	
def main():
    global make_payment,now, expdate, flag,entry_frame,date,name,days,ot,rate,total
    total=0.0
    load_pickle()
    flag='make_payment'
    i=0
    make_payment=Tk()
    make_payment.configure(background="white")
    make_payment.state("zoomed")
    make_payment.title('Labour Payment')
    column_frame = tk.Frame(make_payment,background="white")

    date = StringVar(make_payment,value=aaa)
    name = StringVar(make_payment)
    days = IntVar(make_payment)
    ot = IntVar(make_payment)
    rate = DoubleVar(make_payment)
    total = DoubleVar(make_payment)

    #make_payment.wm_iconbitmap('favicon.ico')
    Label(column_frame,text='Today: '+str(now),font=("Belwe Bd BT",15),background="white").grid(row=0,column=0,columnspan=6)
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",15),background="white").grid(row=2, column=0,columnspan=6)

    column_frame.pack()
	
    entry_frame = tk.Frame(make_payment,background="white")
    Label(entry_frame,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=0, column=0)
    Label(entry_frame,text="Name",font=("Belwe Bd BT",15),background="white").grid(row=0, column=1)
    Label(entry_frame,text="Days",font=("Belwe Bd BT",15),background="white").grid(row=0, column=2)
    Label(entry_frame,text="OT",font=("Belwe Bd BT",15),background="white").grid(row=0, column=3)
    Label(entry_frame,text="Rate",font=("Belwe Bd BT",15),background="white").grid(row=0, column=4)
    Label(entry_frame,text="Total",font=("Belwe Bd BT",15),background="white").grid(row=0, column=5)

    date_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=date)
    date_entry.grid(row=1,column=0)

    sql  = "select name from labour_details"
    cur.execute(sql)

    name_choices = [""]
    for result in cur:
        name_choices.append(result[0])
    name_option = ttk.OptionMenu(entry_frame, name, *name_choices)
    name_option.grid(row=1,column=1)
    
    name.trace('w', update_values)
    days_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=days)
    days_entry.grid(row=1,column=2)

    ot_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=ot)
    ot_entry.grid(row=1,column=3)

    rate_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=rate)
    rate_entry.grid(row=1,column=4)

    total_entry = Entry(entry_frame,font=("Belwe lt BT",10),textvariable=total)
    total_entry.grid(row=1,column=5)

    
    entry_frame.pack()
    
    button_frame = tk.Frame(make_payment,background="white")
    Label(button_frame,text="",background="white").grid(row=0, column=0)

    tk.Button(button_frame,width=10,font=("Belwe Bd BT",15),text='Calculate',command=lambda : calculate()).grid(row=1, column=0)
    tk.Button(button_frame,width=15,font=("Belwe Bd BT",15),text='Submit',command=lambda : Insert_payment()).grid(row=1, column=2)
    tk.Button(button_frame,width=20,font=("Belwe Bd BT",15),text='Return to Main Menu',command=make_payment.destroy).grid(row=1, column=4)
	
    button_frame.pack()
    make_payment.mainloop()
    
    
def mainmenu():
    if flag=='make_payment':
        make_payment.destroy()
    
    

# expiry()