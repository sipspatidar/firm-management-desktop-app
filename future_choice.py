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
columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()


def submit():
    return 0
	

def sell_insert():
    global middle_section,date,client,items,quantity,rate,total_var,paid
    print(date.get(),client.get(),items.get(),quantity.get(),rate.get(),total_var.get(),paid.get())
	
    success = True
    try:
        sql = "insert into sell(adate,client,item,quantity,rate,total,paid) values(date('%s'),'%s','%s',%s,%s,%s,'%s')"%(date.get(),client.get(),items.get(),quantity.get(),rate.get(),total_var.get(),paid.get())
        print(sql)		
        cur.execute(sql)
        if items.get()=='250':
            ss = 'tf'
            ww = quantity.get()*35
        if items.get()=='500':
            ss = 'fh'
            ww = quantity.get()*24

        if items.get()=='1000':
            ss = 'ts'
            ww = quantity.get()*12

        print(ss)
        sql = "update stock_maintenance set %s=%s-%i"%(ss,ss,ww)
        print(sql)		

        cur.execute(sql)
		
    except Exception as exp:
        print(exp)
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Sell Successfully Inserted")
        messagebox.showinfo('Successfull', 'Sell Successfully Inserted')
        get_last_sell()
        get_unpaid_sell()
	
def get_last_sell():
    global last_sell	
    for widget in last_sell.winfo_children():
        widget.destroy()
    Label(last_sell,text="-"*40+"Last Five Sells"+"-"*40,font=("Belwe Bd BT",15),background="white").grid(row=1,column=1,columnspan=7)
		
    Label(last_sell,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=3,column=1)
    Label(last_sell,text="Client",font=("Belwe Bd BT",15),background="white").grid(row=3,column=2)
    Label(last_sell,text="Type",font=("Belwe Bd BT",15),background="white").grid(row=3,column=3)
    Label(last_sell,text="Quantity",font=("Belwe Bd BT",15),background="white").grid(row=3,column=4)
    Label(last_sell,text="Rate",font=("Belwe Bd BT",15),background="white").grid(row=3,column=5)
    Label(last_sell,text="Total",font=("Belwe Bd BT",15),background="white").grid(row=3,column=6)
    Label(last_sell,text="Paid",font=("Belwe Bd BT",15),background="white").grid(row=3,column=7)

    try:
        sql = "select * from sell order by adate desc limit 5"
        print(sql)
        cur.execute(sql)
        i=4
        for result in cur:
            Label(last_sell,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i,column=1)
            Label(last_sell,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i,column=2)
            Label(last_sell,text=result[3],font=("Belwe lt BT",15),background="white").grid(row=i,column=3)
            Label(last_sell,text=result[4],font=("Belwe lt BT",15),background="white").grid(row=i,column=4)
            Label(last_sell,text=result[5],font=("Belwe lt BT",15),background="white").grid(row=i,column=5)
            Label(last_sell,text=result[6],font=("Belwe lt BT",15),background="white").grid(row=i,column=6)
            Label(last_sell,text=result[7],font=("Belwe lt BT",15),background="white").grid(row=i,column=7)
            i+=1
    except Exception as exp:
        insert_error(exp)
    
    Label(last_sell,text="-"*80,font=("Belwe Bd BT",15),background="white").grid(row=i,column=1,columnspan=7)
def update_sell(id):
    success = True
    try:
        sql = "update sell set paid='paid' where id=%s"%(id)
        print(sql)		
        cur.execute(sql)
    except Exception as exp:
        print(exp)
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Sell Successfully Updated")
        messagebox.showinfo('Successfull', 'Sell Successfully Updated')
        get_last_sell()
        get_unpaid_sell()
    



def get_unpaid_sell():
    global unpaid_sell	
    for widget in unpaid_sell.winfo_children():
        widget.destroy()
    Label(unpaid_sell,text="-"*40+"Unpaid Sells List"+"-"*40,font=("Belwe Bd BT",15),background="white").grid(row=1,column=1,columnspan=9)
		
    Label(unpaid_sell,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=3,column=1)
    Label(unpaid_sell,text="Client",font=("Belwe Bd BT",15),background="white").grid(row=3,column=2)
    Label(unpaid_sell,text="Type",font=("Belwe Bd BT",15),background="white").grid(row=3,column=3)
    Label(unpaid_sell,text="Quantity",font=("Belwe Bd BT",15),background="white").grid(row=3,column=4)
    Label(unpaid_sell,text="Rate",font=("Belwe Bd BT",15),background="white").grid(row=3,column=5)
    Label(unpaid_sell,text="Total",font=("Belwe Bd BT",15),background="white").grid(row=3,column=6)
    Label(unpaid_sell,text="Action",font=("Belwe Bd BT",15),background="white").grid(row=3,column=7)


    try:
        sql = "select * from sell where paid='not paid' order by adate desc "
        print(sql)
        cur.execute(sql)
        i=4
        for result in cur:
            Label(unpaid_sell,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i,column=1)
            Label(unpaid_sell,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i,column=2)
            Label(unpaid_sell,text=result[3],font=("Belwe lt BT",15),background="white").grid(row=i,column=3)
            Label(unpaid_sell,text=result[4],font=("Belwe lt BT",15),background="white").grid(row=i,column=4)
            Label(unpaid_sell,text=result[5],font=("Belwe lt BT",15),background="white").grid(row=i,column=5)
            Label(unpaid_sell,text=result[6],font=("Belwe lt BT",15),background="white").grid(row=i,column=6)
            tk.Button(unpaid_sell,text="Make Paid",font=("Belwe lt BT",15),command=lambda id=result[0]: update_sell(id) ).grid(row=i,column=7)
            i+=1
    except Exception as exp:
        insert_error(exp)
    
    Label(unpaid_sell,text="-"*80,font=("Belwe Bd BT",15),background="white").grid(row=i+1,column=1,columnspan=7)
def calculate():
    global middle_section,last_sell,unpaid_sell,date,client,items,quantity,rate,total_var,paid,gst
    print(gst.get())
    if gst.get() == 1:
         total_var.set(round(int((quantity.get())*rate.get()*118)/100,2))
    else:
         total_var.set(round(int(quantity.get())*rate.get(),2))

def sell():
    global middle_section,last_sell,unpaid_sell,date,client,items,quantity,rate,total_var,paid,gst
    for widget in middle_section.winfo_children():
        widget.destroy()

    date = StringVar(middle_section,value=today_date)
    client = StringVar(middle_section)
    items = StringVar(middle_section)
    quantity = IntVar(middle_section)
    rate = DoubleVar(middle_section)
    total_var = DoubleVar(middle_section)
    paid = StringVar(middle_section)


    # Dictionary with options
	
    items_choices = [ "Select Bottle","250","500","1000" ]
    paid_choices = [ "Select Option","paid","not paid" ]
	

    date_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=date)
    Label(middle_section,text="Date",font=("Belwe Bd BT",15),background="white").grid(row=1,column=1)
    date_entry.grid(row=2,column=1)

    client_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=client)
    Label(middle_section,text="Client",font=("Belwe Bd BT",15),background="white").grid(row=1,column=2)
    client_entry.grid(row=2,column=2)

    items_option = ttk.OptionMenu(middle_section, items, *items_choices)
    Label(middle_section,text="Select Items",font=("Belwe Bd BT",15),background="white").grid(row=1,column=3)
    items_option.grid(row=2,column=3)

    quantity_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=quantity)
    Label(middle_section,text="Quantity",font=("Belwe Bd BT",15),background="white").grid(row=1,column=4)
    quantity_entry.grid(row=2,column=4)

    rate_entry = Entry(middle_section,font=("Belwe lt BT",10),textvariable=rate)
    Label(middle_section,text="rate",font=("Belwe Bd BT",15),background="white").grid(row=1,column=5)
    rate_entry.grid(row=2,column=5)

    Label(middle_section,text="GST",font=("Belwe Bd BT",15),background="white").grid(row=1,column=6)

    gst = IntVar(middle_section)    
    C1 = Checkbutton(middle_section, text = "", variable = gst,onvalue = 1, offvalue = 0)
    C1.grid(row=2,column=6)
	
    Label(middle_section,text="Total",font=("Belwe Bd BT",15),background="white").grid(row=1,column=7,columnspan=2)
    total_entry = Label(middle_section,font=("Belwe lt BT",15),textvariable=total_var)
    tk.Button(middle_section,text="calculate",font=("Belwe lt BT",15),command=lambda : calculate()).grid(row=2,column=8)
    total_entry.grid(row=2,column=7)

    paid_option = ttk.OptionMenu(middle_section, paid, *paid_choices)
    Label(middle_section,text="Paid/Not",font=("Belwe Bd BT",15),background="white").grid(row=1,column=9)
    paid_option.grid(row=2,column=9)

    items.set(items_choices[1])
    paid.set(paid_choices[1])

    tk.Button(middle_section,text="Add Sell",font=("Belwe Bd BT",15),command=lambda : sell_insert()).grid(row=2,column=10)
    	
    client_names = tk.Frame(middle_section,background="white")
    Label(client_names,text="-"*10+"Select Client Names From Here"+"-"*10,font=("Belwe Bd BT",15),background="white").pack(side=TOP)
    sql  = "select name from clients"
    cur.execute(sql)
    def onmousewheel(event):
        print(event.delta)
        listbox1.yview('scroll',event.delta,'units')
        return "break"
    def select_cn(e):
        name=listbox1.curselection()
        client.set(client_names_list[name[0]])
        print(listbox1)
    scrollbar = Scrollbar(client_names)

    listbox1 = Listbox(client_names,height=5)
    listbox1.pack()
	
    client_names_list = []
	
	
	
	
    for result in cur:
        listbox1.insert(END,result[0])
        client_names_list.append(result[0])

        #tk.Button(client_names,text=result[0],font=("Belwe lt BT",15),command=lambda name=result[0]: client.set(name) ).pack()
    listbox1.config(yscrollcommand=scrollbar.set)
    listbox1.bind('<MouseWheel>',onmousewheel)
    listbox1.bind('<<ListboxSelect>>', select_cn)    

    client_names.grid(row=3,column=1,columnspan=2,sticky="W")
	
	
    #View Last Sells
    last_sell = tk.Frame(middle_section,background="white")
    
    get_last_sell()
    last_sell.grid(row=3,column=3,columnspan=7,sticky="E")

    #View unpaid Sells
    unpaid_sell = tk.Frame(middle_section,background="white")
    get_unpaid_sell()
    unpaid_sell.grid(row=6,column=1,columnspan=9,sticky="S")


def insert_raw_material():
    global middle_section,date,type,quantity,raw
    print(date.get(),type.get(),quantity.get())
    success = True
    try:
	
	
        sql = "insert into raw_material(adate,raw,type,quantity) values(date('%s'),'%s','%s',%i)"%(date.get(),raw.get(),type.get(),quantity.get())
        cur.execute(sql)

        print(sql)		
        sql = "update stock_maintenance set %s=%s+%i"%(type.get()+raw.get(),type.get()+raw.get(),quantity.get())
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
        sql = "select * from raw_material order by id desc"
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
    p100 = round(thousand.get()/51,2)
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
        sql = "insert into production(adate,tf,fh,ts) values(date('%s'),%i,%i,%i)"%(date.get(),two_fifty.get(),five_hundred.get(),thousand.get())
        cur.execute(sql)

        print(sql)		
        sql = "update stock_maintenance set tf=tf+%i,fh=fh+%i,ts=ts+%i,preform250=preform250-%f,preform500=preform500-%f,preform1000=preform1000-%f,lable250=lable250-%i,lable500=lable500-%i,lable1000=lable1000-%i,caps250=caps250-%i,caps500=caps500-%i,caps1000=caps1000-%i,boxes250=boxes250-%i,boxes500=boxes500-%i,boxes1000=boxes1000-%i"%(two_fifty.get(),five_hundred.get(),thousand.get(),p250,p500,p100,l250,l500,l100,c250,c500,c100,b250,b500,b100)
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
        sql = "select * from production order by adate desc"
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

    
    sql="select * from stock_maintenance"
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
    ''' Future Choice GUI '''
    global middle_section
    flag='Future Choice'
    future_choice=Tk()
    future_choice.configure(background="white")
    future_choice.title('Future Choice')
    future_choice.state("zoomed")
    #billingsto.wm_iconbitmap('favicon.ico')
    #Label(future_choice,text='-'*48+'Future Choice'+'-'*49).grid(row=0,column=0,columnspan=7,sticky='W')
    
    side_menu = tk.Frame(future_choice,background="white")

    tk.Button(side_menu,width=20,text='SELLS',font=("Belwe Bd BT",15),command=sell).grid(row=0, column=1)
    tk.Button(side_menu,width=20,text='RAW MATERIAL',font=("Belwe Bd BT",15),command=raw_material).grid(row=0, column=2)
    tk.Button(side_menu,width=20,text='PRODUCTION',font=("Belwe Bd BT",15),command=production).grid(row=0, column=3)
    tk.Button(side_menu,width=20,text='STOCK MAINTENANCE',font=("Belwe Bd BT",15),command=stock_maintain).grid(row=0, column=4)
    tk.Button(side_menu,width=20,text='Back to Main Menu',font=("Belwe Bd BT",15),command=future_choice.destroy).grid(row=0, column=5)
    Label(side_menu,text='-'*200,font=("Belwe Bd BT",15),background="white").grid(row=2,column=1,columnspan=5,sticky='N')
	
    side_menu.pack(side=TOP)
    sw= ScrolledWindow(future_choice)
    sw.pack()

    middle_section = tk.Frame(sw.window,background="white")
    Label(middle_section,text='-'*48+'Future Choice'+'-'*49,font=("Belwe Bd BT",15),background="white").grid(row=0,column=0,columnspan=9,sticky='N')
    middle_section.pack(fill=BOTH,expand=1)

    future_choice.mainloop()


    
def mainmenu():
    if flag=='sto':
        sto.destroy()
    elif flag=='billingsto':
        billingsto.destroy()  
    elif flag=='dailyinco':
        dailyinco.destroy()
        
main()