from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from sqlite3 import dbapi2 as sqlite
from log_maker import *
from tkinter import messagebox
from tkinter.tix import *
from math import ceil
import random
from datetime import date as dat

now = dat.today()
today_date = now

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()


def insert_payment():
    global middle_section,date,rs,remark
    print(date.get(),rs.get(),remark.get())
    success = True
    try:
	
	
        sql = "insert into payment(adate,rs,remark,type) values(date('%s'),%i,'%s','gram')"%(date.get(),rs.get(),remark.get())
        cur.execute(sql)

		
    except Exception as exp:
        print(exp)
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Payment Successfully Inserted")
        messagebox.showinfo('Successfull', 'Payment Successfully Inserted')
        get_last_payment()

def get_last_payment():
    global last_payment
	
    for widget in last_payment.winfo_children():
        widget.destroy()
	




    Label(last_payment,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=6,column=1)
    Label(last_payment,text="Amount",font=("Belwe Bd BT",15),background="white").grid(row=6,column=2)
    Label(last_payment,text="Remark",font=("Belwe Bd BT",15),background="white").grid(row=6,column=3)



    try:
        sql = "select * from payment where type='gram'"
        print(sql)
        cur.execute(sql)
        i=7
        for result in cur:

            Label(last_payment,text=result[0],background="white").grid(row=i,column=1)
            Label(last_payment,text=result[1],background="white").grid(row=i,column=2)
            Label(last_payment,text=result[2],background="white").grid(row=i,column=3)
            
            i+=1
    except Exception as exp:
        insert_error(exp)
    
    Label(last_payment,text="-"*80,font=("Belwe Bd BT",15),background="white").grid(row=i,column=1,columnspan=4)
	
def payment():
    global middle_section,last_payment,date,rs,remark

    for widget in middle_section.winfo_children():
        widget.destroy()

    date = StringVar(middle_section,value=today_date)
    rs = IntVar(middle_section)
    remark = StringVar(middle_section)	

 	
	
    date_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=date)
    Label(middle_section,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=1,column=1)
    date_entry.grid(row=2,column=1)

    rs_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=rs)
    Label(middle_section,text="Amount",font=("Belwe Bd BT",15),background="white").grid(row=1,column=2)
    rs_entry.grid(row=2,column=2)

    remark_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=remark)
    Label(middle_section,text="Remark",font=("Belwe Bd BT",15),background="white").grid(row=1,column=3)
    remark_entry.grid(row=2,column=3)




    tk.Button(middle_section,text="Make Payment",font=("Belwe Bd BT",15),command=lambda : insert_payment()).grid(row=2,column=4)
    Label(middle_section,text="-"*60+"Last Raw Material Entry"+"-"*60,font=("Belwe Bd BT",15),background="white").grid(row=3,columnspan=4)

    last_payment = tk.Frame(middle_section,background="white")
    
    get_last_payment()
	
    last_payment.grid(row=4,column=1,columnspan=4)


def insert_raw_material():
    global middle_section,date,type,quantity,raw
    print(date.get(),type.get(),quantity.get())
    success = True
    try:
	
	
        sql = "insert into raw_material_34gram(adate,raw,type,quantity) values(date('%s'),'%s','%s',%i)"%(date.get(),raw.get(),type.get(),quantity.get())
        cur.execute(sql)

        print(sql)		
        sql = "update stock_maintenance_34gram set %s=%s+%i"%(type.get()+raw.get(),type.get()+raw.get(),quantity.get())
        print(sql)		
        cur.execute(sql)
		
    except Exception as exp:
        print(exp)
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Raw Material Successfully Inserted")
        messagebox.showinfo('Successfull', 'Raw Material Successfully Inserted')
        get_last_raw()

def get_last_raw():
    global last_raw
	
    for widget in last_raw.winfo_children():
        widget.destroy()
	




    Label(last_raw,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=6,column=1)
    Label(last_raw,text="Bottle",font=("Belwe Bd BT",15),background="white").grid(row=6,column=2)
    Label(last_raw,text="Type",font=("Belwe Bd BT",15),background="white").grid(row=6,column=3)
    Label(last_raw,text="Quantity",font=("Belwe Bd BT",15),background="white").grid(row=6,column=4)



    try:
        sql = "select * from raw_material_34gram order by id desc"
        print(sql)
        cur.execute(sql)
        i=7
        for result in cur:

            Label(last_raw,text=result[1],background="white").grid(row=i,column=1)
            Label(last_raw,text=result[2],background="white").grid(row=i,column=2)
            Label(last_raw,text=result[3],background="white").grid(row=i,column=3)
            Label(last_raw,text=result[4],background="white").grid(row=i,column=4)
            
            i+=1
    except Exception as exp:
        insert_error(exp)
    
    Label(last_raw,text="-"*80,font=("Belwe Bd BT",15),background="white").grid(row=i,column=1,columnspan=4)
	
def raw_material():
    global middle_section,last_raw,date,type,quantity,raw

    for widget in middle_section.winfo_children():
        widget.destroy()

    date = StringVar(middle_section,value=today_date)
    type = StringVar(middle_section)
    raw = StringVar(middle_section)
    quantity = IntVar(middle_section)	

    type_choices = [ "","preform","caps","lable","boxes"]
    type.set(type_choices[1]) # set the default option
    raw_choices = [ "","250","500","1000"]
    raw.set(raw_choices[1]) # set the default option
	
	
    date_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=date)
    Label(middle_section,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=1,column=1)
    date_entry.grid(row=2,column=1)

    raw_option = ttk.OptionMenu(middle_section, raw, *raw_choices)
    Label(middle_section,text="Select Bootle",font=("Belwe Bd BT",15),background="white").grid(row=1,column=2)
    raw_option.grid(row=2,column=2)

    type_option = ttk.OptionMenu(middle_section, type, *type_choices)
    Label(middle_section,text="Select Type",font=("Belwe Bd BT",15),background="white").grid(row=1,column=3)
    type_option.grid(row=2,column=3)

    quantity_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=quantity)
    Label(middle_section,text="Quantity",font=("Belwe Bd BT",15),background="white").grid(row=1,column=4)
    quantity_entry.grid(row=2,column=4)



    tk.Button(middle_section,text="Add Raw material",font=("Belwe Bd BT",15),command=lambda : insert_raw_material()).grid(row=2,column=5)
    Label(middle_section,text="-"*60+"Last Raw Material Entry"+"-"*60,font=("Belwe Bd BT",15),background="white").grid(row=3,columnspan=5)

    last_raw = tk.Frame(middle_section,background="white")
    
    get_last_raw()
	
    last_raw.grid(row=4,column=1,columnspan=4)
	
    

def production_insert():
    global middle_section,date,thousand,two_fifty,five_hundred
    
    p250 = round(two_fifty.get()/106,2)
    p500 = round(five_hundred.get()/70,2)
    p100 = round(thousand.get()/29,2)
    l250 = two_fifty.get()
    l500 = five_hundred.get()
    l100 = thousand.get()
    c250 = two_fifty.get()
    c500 = five_hundred.get()
    c100 = thousand.get()
    b250 = ceil(two_fifty.get()/35)
    b500 = ceil(five_hundred.get()/24)
    b100 = ceil(thousand.get()/12)

    print(p250,p500,p100,l250,l500,l100,c250,c500,c100,b250,b500,b100)

    print(date.get(),two_fifty.get(),five_hundred.get(),thousand.get())
    success = True
    try:
        sql = "insert into production_34gram(adate,tf,fh,ts) values(date('%s'),%i,%i,%i)"%(date.get(),two_fifty.get(),five_hundred.get(),thousand.get())
        cur.execute(sql)

        print(sql)		
        sql = "update stock_maintenance_34gram set tf=tf+%i,fh=fh+%i,ts=ts+%i,preform250=preform250-%f,preform500=preform500-%f,preform1000=preform1000-%f,lable250=lable250-%i,lable500=lable500-%i,lable1000=lable1000-%i,caps250=caps250-%i,caps500=caps500-%i,caps1000=caps1000-%i,boxes250=boxes250-%i,boxes500=boxes500-%i,boxes1000=boxes1000-%i"%(two_fifty.get(),five_hundred.get(),thousand.get(),p250,p500,p100,l250,l500,l100,c250,c500,c100,b250,b500,b100)
        print(sql)
        cur.execute(sql)
		
    except Exception as exp:
        print(exp)
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Production Successfully Inserted")
        messagebox.showinfo('Successfull', 'Production Successfully Inserted')
        get_last_production()

def get_last_production():
    global last_production
    for widget in last_production.winfo_children():
        widget.destroy()
    
	
    Label(last_production,text="-"*40+"Last Production"+"-"*40,font=("Belwe Bd BT",15),background="white").grid(row=1,column=1,columnspan=4)

		
    Label(last_production,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=3,column=1)
    Label(last_production,text="250ml",font=("Belwe Bd BT",15),background="white").grid(row=3,column=2)
    Label(last_production,text="500ml",font=("Belwe Bd BT",15),background="white").grid(row=3,column=3)
    Label(last_production,text="1000ml",font=("Belwe Bd BT",15),background="white").grid(row=3,column=4)

    try:
        sql = "select * from production_34gram order by adate desc"
        cur.execute(sql)
        i=4
        for result in cur:
            Label(last_production,text=result[0],font=("Belwe lt BT",15),background="white").grid(row=i,column=1)
            Label(last_production,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i,column=2)
            Label(last_production,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i,column=3)
            Label(last_production,text=result[3],font=("Belwe lt BT",15),background="white").grid(row=i,column=4)
            i+=1
			
    except Exception as exp:
        insert_error(exp)

    Label(last_production,text="-"*80,font=("Belwe Bd BT",15),background="white").grid(row=14,column=1,columnspan=4)
    

def production():
    global middle_section,last_production,date,thousand,two_fifty,five_hundred

    for widget in middle_section.winfo_children():
        widget.destroy()
    two_fifty = IntVar(middle_section)
    five_hundred = IntVar(middle_section)
    thousand = IntVar(middle_section)
    date = StringVar(middle_section,value=today_date)

    date_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=date)
    Label(middle_section,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=1,column=1)
    date_entry.grid(row=2,column=1)
	
    two_fifty_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=two_fifty)
    Label(middle_section,text="250 ml.",font=("Belwe Bd BT",15),background="white").grid(row=1,column=2)
    two_fifty_entry.grid(row=2,column=2)

    five_hundred_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=five_hundred)
    Label(middle_section,text="500 ml.",font=("Belwe Bd BT",15),background="white").grid(row=1,column=3)
    five_hundred_entry.grid(row=2,column=3)

    thousand_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=thousand)
    Label(middle_section,text="1000 ml.",font=("Belwe Bd BT",15),background="white").grid(row=1,column=4)
    thousand_entry.grid(row=2,column=4)

    tk.Button(middle_section,text="Add",font=("Belwe Bd BT",15),command=lambda : production_insert()).grid(row=2,column=5)
	
	
    last_production = tk.Frame(middle_section,background="white")
    
    get_last_production()

	
	
    last_production.grid(row=4,column=1,columnspan=5)
	

	
	
	
	
def stock_maintain():
    global middle_section

    for widget in middle_section.winfo_children():
        widget.destroy()

		
    bottle_frame = tk.Frame(middle_section,background="white")
    Label(bottle_frame,text="-"*30+"Bottles"+"-"*30,font=("Belwe Bd BT",15),background="white").grid(row=1,column=1,columnspan=4)
    Label(bottle_frame,text="",font=("Belwe Bd BT",15),background="white").grid(row=2,column=1)
    Label(bottle_frame,text="250",font=("Belwe Bd BT",15),background="white").grid(row=2,column=2)
    Label(bottle_frame,text="500",font=("Belwe Bd BT",15),background="white").grid(row=2,column=3)
    Label(bottle_frame,text="1000",font=("Belwe Bd BT",15),background="white").grid(row=2,column=4)

    
    sql="select * from stock_maintenance_34gram"
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
    Label(bottle_frame,text="",font=("Belwe lt BT",15),background="white").grid(row=3,column=1)
    Label(bottle_frame,text="Bottle",font=("Belwe lt BT",15),background="white").grid(row=4,column=1)
    Label(bottle_frame,text=result[0],font=("Belwe lt BT",15),background="white").grid(row=4,column=2)
    Label(bottle_frame,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=4,column=3)
    Label(bottle_frame,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=4,column=4)
    Label(bottle_frame,text="Preform",font=("Belwe lt BT",15),background="white").grid(row=5,column=1)
    Label(bottle_frame,text=result[3],font=("Belwe lt BT",15),background="white").grid(row=5,column=2)
    Label(bottle_frame,text=result[4],font=("Belwe lt BT",15),background="white").grid(row=5,column=3)
    Label(bottle_frame,text=result[5],font=("Belwe lt BT",15),background="white").grid(row=5,column=4)
    Label(bottle_frame,text="Lable",font=("Belwe lt BT",15),background="white").grid(row=6,column=1)
    Label(bottle_frame,text=result[6],font=("Belwe lt BT",15),background="white").grid(row=6,column=2)
    Label(bottle_frame,text=result[7],font=("Belwe lt BT",15),background="white").grid(row=6,column=3)
    Label(bottle_frame,text=result[8],font=("Belwe lt BT",15),background="white").grid(row=6,column=4)
    Label(bottle_frame,text="Caps",font=("Belwe lt BT",15),background="white").grid(row=7,column=1)
    Label(bottle_frame,text=result[9],font=("Belwe lt BT",15),background="white").grid(row=7,column=2)
    Label(bottle_frame,text=result[10],font=("Belwe lt BT",15),background="white").grid(row=7,column=3)
    Label(bottle_frame,text=result[11],font=("Belwe lt BT",15),background="white").grid(row=7,column=4)
    Label(bottle_frame,text="Boxes",font=("Belwe lt BT",15),background="white").grid(row=8,column=1)
    Label(bottle_frame,text=result[12],font=("Belwe lt BT",15),background="white").grid(row=8,column=2)
    Label(bottle_frame,text=result[13],font=("Belwe lt BT",15),background="white").grid(row=8,column=3)
    Label(bottle_frame,text=result[14],font=("Belwe lt BT",15),background="white").grid(row=8,column=4)

    bottle_frame.grid(row=1,column=1,sticky="W",columnspan=4)

	


def main():
    ''' 34gram GUI '''
    global middle_section
    flag='34gram'
    gram_34=Tk()
    gram_34.configure(background="white")
    gram_34.title('34gram')
    gram_34.state("zoomed")
    #billingsto.wm_iconbitmap('favicon.ico')
    #Label(gram_34,text='-'*48+'34gram'+'-'*49).grid(row=0,column=0,columnspan=7,sticky='W')
    
    side_menu = tk.Frame(gram_34,background="white")

    tk.Button(side_menu,width=20,text='SEND PAYMENT',font=("Belwe Bd BT",15),command=payment).grid(row=0, column=1)
    tk.Button(side_menu,width=20,text='RAW MATERIAL',font=("Belwe Bd BT",15),command=raw_material).grid(row=0, column=2)
    tk.Button(side_menu,width=20,text='PRODUCTION',font=("Belwe Bd BT",15),command=production).grid(row=0, column=3)
    tk.Button(side_menu,width=20,text='STOCK MAINTENANCE',font=("Belwe Bd BT",15),command=stock_maintain).grid(row=0, column=4)
    tk.Button(side_menu,width=20,text='Back to Main Menu',font=("Belwe Bd BT",15),command=gram_34.destroy).grid(row=0, column=5)
    Label(side_menu,text='-'*200,font=("Belwe Bd BT",15),background="white").grid(row=2,column=1,columnspan=5,sticky='N')
	
    side_menu.pack(side=TOP)

    sw= ScrolledWindow(gram_34)
    sw.pack()

    middle_section = tk.Frame(sw.window,background="white")
    Label(middle_section,text='-'*48+'34 Grams'+'-'*49,font=("Belwe Bd BT",15),background="white").grid(row=0,column=0,columnspan=9,sticky='N')
    middle_section.pack(fill=BOTH,expand=1)

    gram_34.mainloop()


    
def mainmenu():
    if flag=='sto':
        sto.destroy()
    elif flag=='billingsto':
        billingsto.destroy()  
    elif flag=='dailyinco':
        dailyinco.destroy()
        
main()