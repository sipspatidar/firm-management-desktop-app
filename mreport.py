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
print(aaa.month)
find = "____-%"+str(aaa.month)+"-__"

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()

	
	
def main():
    global report_tk,now, expdate, flag,entry_frame,date,name,days,ot,rate,total
    flag='report_tk'
	

	
    report_tk=Tk()
    report_tk.configure(background="white")
    report_tk.state("zoomed")
    report_tk.title('Monthly Report')


    sw= ScrolledWindow(report_tk)
    sw.pack(fill=BOTH,expand=1)
    column_frame = tk.Frame(sw.window,background="white")

    www = tk.Frame(column_frame,background="white")
    Label(www,text="Raw Material",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0,column=0,columnspan=16)
    #for space of one row
    Label(www,text="",font=("Belwe Bd BT",20),background="white",fg="blue").grid(row=1,column=0,columnspan=16)
    entry_frame = tk.Frame(www,background="white")
    Label(entry_frame,text=" Future Choice",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0, column=0,columnspan=5)
    Label(entry_frame,text="Preform",font=("Belwe Bd BT",15),background="white").grid(row=1, column=1)
    Label(entry_frame,text="Lables",font=("Belwe Bd BT",15),background="white").grid(row=1, column=2)
    Label(entry_frame,text="Caps",font=("Belwe Bd BT",15),background="white").grid(row=1, column=3)
    Label(entry_frame,text="Boxes",font=("Belwe Bd BT",15),background="white").grid(row=1, column=4)
	
    sql  = "select sum(quantity) from raw_material where type='preform' and raw='250' and adate like '%s'"%(find)
    print(sql)
    cur.execute(sql)
    fpreform1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='lable' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    flable1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='caps' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='boxes' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='preform' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='lable' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    flable2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='caps' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='boxes' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='preform' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='lable' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    flable3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='caps' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material where type='boxes' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes3 = cur.fetchone()


    Label(entry_frame,text="250",font=("Belwe Bd BT",15),background="white").grid(row=2, column=0)
    Label(entry_frame,text=fpreform1,font=("Belwe lt BT",15),background="white").grid(row=2, column=1)
    Label(entry_frame,text=flable1,font=("Belwe lt BT",15),background="white").grid(row=2, column=2)
    Label(entry_frame,text=fcaps1,font=("Belwe lt BT",15),background="white").grid(row=2, column=3)
    Label(entry_frame,text=fboxes1,font=("Belwe lt BT",15),background="white").grid(row=2, column=4)
    Label(entry_frame,text="500",font=("Belwe Bd BT",15),background="white").grid(row=3, column=0)
    Label(entry_frame,text=fpreform2,font=("Belwe lt BT",15),background="white").grid(row=3, column=1)
    Label(entry_frame,text=flable2,font=("Belwe lt BT",15),background="white").grid(row=3, column=2)
    Label(entry_frame,text=fcaps2,font=("Belwe lt BT",15),background="white").grid(row=3, column=3)
    Label(entry_frame,text=fboxes2,font=("Belwe lt BT",15),background="white").grid(row=3, column=4)
    Label(entry_frame,text="1000",font=("Belwe Bd BT",15),background="white").grid(row=4, column=0)
    Label(entry_frame,text=fpreform3,font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    Label(entry_frame,text=flable3,font=("Belwe lt BT",15),background="white").grid(row=4, column=2)
    Label(entry_frame,text=fcaps3,font=("Belwe lt BT",15),background="white").grid(row=4, column=3)
    Label(entry_frame,text=fboxes3,font=("Belwe lt BT",15),background="white").grid(row=4, column=4)
        
	    
    entry_frame.grid(row=2,column=0,columnspan=5,rowspan=5)


    entry_frame_payas = tk.Frame(www,background="white")
    Label(entry_frame_payas,text=" Payas",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0, column=0,columnspan=5)
    Label(entry_frame_payas,text="Preform",font=("Belwe Bd BT",15),background="white").grid(row=1, column=1)
    Label(entry_frame_payas,text="Lables",font=("Belwe Bd BT",15),background="white").grid(row=1, column=2)
    Label(entry_frame_payas,text="Caps",font=("Belwe Bd BT",15),background="white").grid(row=1, column=3)
    Label(entry_frame_payas,text="Boxes",font=("Belwe Bd BT",15),background="white").grid(row=1, column=4)
	
    sql  = "select sum(quantity) from raw_material_payas where type='preform' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='lable' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    flable1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='caps' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='boxes' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='preform' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='lable' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    flable2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='caps' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='boxes' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='preform' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='lable' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    flable3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='caps' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_payas where type='boxes' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes3 = cur.fetchone()


    Label(entry_frame_payas,text="250",font=("Belwe Bd BT",15),background="white").grid(row=2, column=0)
    Label(entry_frame_payas,text=fpreform1,font=("Belwe lt BT",15),background="white").grid(row=2, column=1)
    Label(entry_frame_payas,text=flable1,font=("Belwe lt BT",15),background="white").grid(row=2, column=2)
    Label(entry_frame_payas,text=fcaps1,font=("Belwe lt BT",15),background="white").grid(row=2, column=3)
    Label(entry_frame_payas,text=fboxes1,font=("Belwe lt BT",15),background="white").grid(row=2, column=4)
    Label(entry_frame_payas,text="500",font=("Belwe Bd BT",15),background="white").grid(row=3, column=0)
    Label(entry_frame_payas,text=fpreform2,font=("Belwe lt BT",15),background="white").grid(row=3, column=1)
    Label(entry_frame_payas,text=flable2,font=("Belwe lt BT",15),background="white").grid(row=3, column=2)
    Label(entry_frame_payas,text=fcaps2,font=("Belwe lt BT",15),background="white").grid(row=3, column=3)
    Label(entry_frame_payas,text=fboxes2,font=("Belwe lt BT",15),background="white").grid(row=3, column=4)
    Label(entry_frame_payas,text="1000",font=("Belwe Bd BT",15),background="white").grid(row=4, column=0)
    Label(entry_frame_payas,text=fpreform3,font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    Label(entry_frame_payas,text=flable3,font=("Belwe lt BT",15),background="white").grid(row=4, column=2)
    Label(entry_frame_payas,text=fcaps3,font=("Belwe lt BT",15),background="white").grid(row=4, column=3)
    Label(entry_frame_payas,text=fboxes3,font=("Belwe lt BT",15),background="white").grid(row=4, column=4)
        
	    
    entry_frame_payas.grid(row=2,column=6,columnspan=5,rowspan=5)

    entry_frame_oras = tk.Frame(www,background="white")
    Label(entry_frame_oras,text=" Oras",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0, column=0,columnspan=5)
    Label(entry_frame_oras,text="Preform",font=("Belwe Bd BT",15),background="white").grid(row=1, column=1)
    Label(entry_frame_oras,text="Lables",font=("Belwe Bd BT",15),background="white").grid(row=1, column=2)
    Label(entry_frame_oras,text="Caps",font=("Belwe Bd BT",15),background="white").grid(row=1, column=3)
    Label(entry_frame_oras,text="Boxes",font=("Belwe Bd BT",15),background="white").grid(row=1, column=4)
	
    sql  = "select sum(quantity) from raw_material_oras where type='preform' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='lable' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    flable1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='caps' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='boxes' and raw='250' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes1 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='preform' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='lable' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    flable2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='caps' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='boxes' and raw='500' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes2 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='preform' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fpreform3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='lable' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    flable3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='caps' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fcaps3 = cur.fetchone()
    sql  = "select sum(quantity) from raw_material_oras where type='boxes' and raw='1000' and adate like '%s'"%(find)
    cur.execute(sql)
    fboxes3 = cur.fetchone()


    Label(entry_frame_oras,text="250",font=("Belwe Bd BT",15),background="white").grid(row=2, column=0)
    Label(entry_frame_oras,text=fpreform1,font=("Belwe lt BT",15),background="white").grid(row=2, column=1)
    Label(entry_frame_oras,text=flable1,font=("Belwe lt BT",15),background="white").grid(row=2, column=2)
    Label(entry_frame_oras,text=fcaps1,font=("Belwe lt BT",15),background="white").grid(row=2, column=3)
    Label(entry_frame_oras,text=fboxes1,font=("Belwe lt BT",15),background="white").grid(row=2, column=4)
    Label(entry_frame_oras,text="500",font=("Belwe Bd BT",15),background="white").grid(row=3, column=0)
    Label(entry_frame_oras,text=fpreform2,font=("Belwe lt BT",15),background="white").grid(row=3, column=1)
    Label(entry_frame_oras,text=flable2,font=("Belwe lt BT",15),background="white").grid(row=3, column=2)
    Label(entry_frame_oras,text=fcaps2,font=("Belwe lt BT",15),background="white").grid(row=3, column=3)
    Label(entry_frame_oras,text=fboxes2,font=("Belwe lt BT",15),background="white").grid(row=3, column=4)
    Label(entry_frame_oras,text="1000",font=("Belwe Bd BT",15),background="white").grid(row=4, column=0)
    Label(entry_frame_oras,text=fpreform3,font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    Label(entry_frame_oras,text=flable3,font=("Belwe lt BT",15),background="white").grid(row=4, column=2)
    Label(entry_frame_oras,text=fcaps3,font=("Belwe lt BT",15),background="white").grid(row=4, column=3)
    Label(entry_frame_oras,text=fboxes3,font=("Belwe lt BT",15),background="white").grid(row=4, column=4)
        
	    
    entry_frame_oras.grid(row=2,column=11,columnspan=5,rowspan=5)
    #for space of one row
    Label(www,text="",font=("Belwe Bd BT",20),background="white",fg="blue").grid(row=8,column=0,columnspan=16)

    prodction_f = tk.Frame(www,background="white")
    Label(prodction_f,text="Production ",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0, column=0,columnspan=4)
    Label(prodction_f,text="250",font=("Belwe Bd BT",15),background="white").grid(row=1, column=1)
    Label(prodction_f,text="500",font=("Belwe Bd BT",15),background="white").grid(row=1, column=2)
    Label(prodction_f,text="1000",font=("Belwe Bd BT",15),background="white").grid(row=1, column=3)
	
    sql  = "select sum(tf),sum(fh),sum(ts) from production where adate like '%s'"%(find)
    cur.execute(sql)
    fcp = cur.fetchone()
    sql  = "select sum(tf),sum(fh),sum(ts) from production_payas where adate like '%s'"%(find)
    cur.execute(sql)
    pp = cur.fetchone()
    sql  = "select sum(tf),sum(fh),sum(ts) from production_oras where adate like '%s'"%(find)
    cur.execute(sql)
    op = cur.fetchone()
    Label(prodction_f,text="Future Choice",font=("Belwe Bd BT",15),background="white").grid(row=2, column=0)
    Label(prodction_f,text=fcp[0],font=("Belwe lt BT",15),background="white").grid(row=2, column=1)
    Label(prodction_f,text=fcp[1],font=("Belwe lt BT",15),background="white").grid(row=2, column=2)
    Label(prodction_f,text=fcp[2],font=("Belwe lt BT",15),background="white").grid(row=2, column=3)
    Label(prodction_f,text="Payas",font=("Belwe Bd BT",15),background="white").grid(row=3, column=0)
    Label(prodction_f,text=pp[0],font=("Belwe lt BT",15),background="white").grid(row=3, column=1)
    Label(prodction_f,text=pp[1],font=("Belwe lt BT",15),background="white").grid(row=3, column=2)
    Label(prodction_f,text=pp[2],font=("Belwe lt BT",15),background="white").grid(row=3, column=3)
    Label(prodction_f,text="Oras",font=("Belwe Bd BT",15),background="white").grid(row=4, column=0)
    Label(prodction_f,text=op[0],font=("Belwe lt BT",15),background="white").grid(row=4, column=1)
    Label(prodction_f,text=op[1],font=("Belwe lt BT",15),background="white").grid(row=4, column=2)
    Label(prodction_f,text=op[2],font=("Belwe lt BT",15),background="white").grid(row=4, column=3)
        
	    
    prodction_f.grid(row=9,column=0,columnspan=5,rowspan=5)

    income = tk.Frame(www,background="white")
    Label(income,text="Income ",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0, column=0,columnspan=4)
    Label(income,text="",font=("Belwe Bd BT",15),background="white").grid(row=1, column=1)
    Label(income,text="Future Choice",font=("Belwe Bd BT",15),background="white").grid(row=2, column=1)
    Label(income,text="payas",font=("Belwe Bd BT",15),background="white").grid(row=3, column=1)
    Label(income,text="Oras",font=("Belwe Bd BT",15),background="white").grid(row=4, column=1)
	
    sql  = "select sum(total) from sell where paid='paid' and adate like '%s'"%(find)
    cur.execute(sql)
    fcs = cur.fetchone()
    sql  = "select sum(rs) from payment where type='payas' and adate like '%s'"%(find)
    cur.execute(sql)
    ps = cur.fetchone()
    sql  = "select sum(rs) from payment where type='oras' and adate like '%s'"%(find)
    cur.execute(sql)
    os = cur.fetchone()
    Label(income,text="",font=("Belwe lt BT",15),background="white").grid(row=1, column=2)
    Label(income,text=fcs[0],font=("Belwe lt BT",15),background="white").grid(row=2, column=2)
    Label(income,text=ps[0],font=("Belwe lt BT",15),background="white").grid(row=3, column=2)
    Label(income,text=os[0],font=("Belwe lt BT",15),background="white").grid(row=4, column=2)
        
    income.grid(row=9,column=6,columnspan=5,rowspan=5)


    expense = tk.Frame(www,background="white")
    Label(expense,text="Expense ",font=("Belwe Bd BT",20),background="white",fg="blue",relief=GROOVE).grid(row=0, column=0,columnspan=4)
    Label(expense,text="",font=("Belwe Bd BT",15),background="white").grid(row=1, column=1)
    Label(expense,text="Future Choice",font=("Belwe Bd BT",15),background="white").grid(row=2, column=1)
    Label(expense,text="",font=("Belwe Bd BT",15),background="white").grid(row=3, column=1)
    Label(expense,text="",font=("Belwe Bd BT",15),background="white").grid(row=4, column=1)
	
    sql  = "select sum(rs) from expenses where adate like '%s'"%(find)
    cur.execute(sql)
    exp = cur.fetchone()
    Label(expense,text="",font=("Belwe lt BT",15),background="white").grid(row=1, column=2)
    Label(expense,text=exp[0],font=("Belwe lt BT",15),background="white").grid(row=2, column=2)
    Label(expense,text="",font=("Belwe lt BT",15),background="white").grid(row=3, column=2)
    Label(expense,text="",font=("Belwe lt BT",15),background="white").grid(row=4, column=2)
        
	    
    expense.grid(row=9,column=11,columnspan=5,rowspan=5)
    www.pack(anchor=CENTER)   
    column_frame.pack(fill=BOTH,expand=1)
   
    report_tk.mainloop()
    
    
def mainmenu():
    if flag=='report_tk':
        report_tk.destroy()
    
    

# expiry()