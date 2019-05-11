from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import dbapi2 as sqlite
from log_maker import *
import time
from tkinter.tix import *

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()




def addBox():
    global entry_frame,name,address,m_no,p_no

    # I use len(all_entries) to get nuber of next free column
    next_row = len(name)


    # add entry in second row
    name.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    name[next_row].grid(row=next_row+1, column=1)
    address.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    address[next_row].grid(row=next_row+1, column=2)
    m_no.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    m_no[next_row].grid(row=next_row+1, column=3)
    p_no.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    p_no[next_row].grid(row=next_row+1, column=4)

def insert_client():
    global name,address,m_no,p_no
    success = True
    try:
        for i in range(len(name)):
            sql = "insert into clients(name,address,mobile,phone) values('%s','%s','%s','%s')"%(name[i].get(),address[i].get(),m_no[i].get(),p_no[i].get())
            cur.execute(sql)
    except Exception as exp:
        c.rollback()
        success = False
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Clients Successfully Inserted")
        messagebox.showinfo('Successfull', 'Clients Successfully Inserted')
        get_client()	
def delete_row(id):
    print(id)
    success = True
    try:
        sql="delete from clients where id=%s"%(id)
        cur.execute(sql)
        get_client()
    except Exception as exp:
        insert_error(exp)
    if success:
        c.commit()
        insert_info("Clients Successfully Deleted")
        messagebox.showinfo('Successfull', 'Clients Details Deleted')
	
def get_client():
    global client_view
	
    for widget in client_view.winfo_children():
        widget.destroy()
    Label(client_view,text="-"*80,font=("Belwe Bd BT",15),background="white").grid(row=1,column=1,columnspan=2)
    Label(client_view,text="name",font=("Belwe Bd BT",15),background="white").grid(row=2,column=1)
    Label(client_view,text="Action",font=("Belwe Bd BT",15),background="white").grid(row=2,column=2)



    try:
        sql = "select id,name from clients"
        cur.execute(sql)
        i=3
        for result in cur:
            Label(client_view,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i,column=1)
            tk.Button(client_view,width=15,text='Delete',font=("Belwe lt BT",15),command=lambda item=result[0]:delete_row(item)).grid(row=i, column=2)
            i+=1
    except Exception as exp:
        insert_error(exp)
	
def add_client():
    global flag,entry_frame,client_view,name,address,m_no,p_no
    flag='add_client'

    add_client=Tk()
    add_client.configure(background="white")
    add_client.state("zoomed")

    sw= ScrolledWindow(add_client)
    sw.pack(fill=BOTH,expand=1)
    add_client_main_frame = tk.Frame(sw.window,background="white")
    column_frame = tk.Frame(add_client_main_frame,background="white")
	
    add_client.title('Add Client Details')
    #add_client.wm_iconbitmap('favicon.ico')
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",15),background="white").grid(row=2, column=0,columnspan=3)

    column_frame.pack()
	
    entry_frame = tk.Frame(add_client_main_frame,background="white")
    Label(entry_frame,text="Name",font=("Belwe Bd BT",15),background="white").grid(row=0, column=1)
    Label(entry_frame,text="Address",font=("Belwe Bd BT",15),background="white").grid(row=0, column=2)
    Label(entry_frame,text="Mobile Number",font=("Belwe Bd BT",15),background="white").grid(row=0, column=3)
    Label(entry_frame,text="Phone Number",font=("Belwe Bd BT",15),background="white").grid(row=0, column=4)

    name = []
    address = []
    m_no = []
    p_no = []
    i=0
    name.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    name[i].grid(row=i+1, column=1)
    address.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    address[i].grid(row=i+1, column=2)
    m_no.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    m_no[i].grid(row=i+1, column=3)
    p_no.append(Entry(entry_frame,font=("Belwe lt BT",15)))
    p_no[i].grid(row=i+1, column=4)
    
    entry_frame.pack()
    
    button_frame = tk.Frame(add_client_main_frame,background="white")
    Label(button_frame,background="white").grid(row=0, column=0)
    tk.Button(button_frame,width=15,text='Add Box',font=("Belwe Bd BT",15),command=addBox).grid(row=1, column=0)
    tk.Button(button_frame,width=15,text='Insert Details',font=("Belwe Bd BT",15),command=lambda:insert_client()).grid(row=1, column=2)
    tk.Button(button_frame,width=20,text='Return to Main Menu',font=("Belwe Bd BT",15),command=add_client.destroy).grid(row=1, column=4)
    Label(button_frame,background="white").grid(row=2, column=0)
	
    button_frame.pack()
    

    client_view = tk.Frame(add_client_main_frame,background="white")
    
    get_client()
	
	
    client_view.pack()
    add_client_main_frame.pack(fill=BOTH,expand=1)
    add_client.mainloop()
def get_detail(c_name):
    top = Tk()
    sw= ScrolledWindow(top)
    sw.pack()
    top.configure(background="white")
	
    c_view = tk.Frame(sw.window	,background="white")
    sql = "select * from sell where client='%s'"%(c_name)
    print(sql)
    cur.execute(sql)
    i=0
    for result in cur:
        Label(c_view,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i,column=0)
        Label(c_view,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i,column=1)
        Label(c_view,text=result[3],font=("Belwe lt BT",15),background="white").grid(row=i,column=2)
        Label(c_view,text=result[4],font=("Belwe lt BT",15),background="white").grid(row=i,column=3)
        Label(c_view,text=result[5],font=("Belwe lt BT",15),background="white").grid(row=i,column=4)
        Label(c_view,text=result[6],font=("Belwe lt BT",15),background="white").grid(row=i,column=5)
        Label(c_view,text=result[7],font=("Belwe lt BT",15),background="white").grid(row=i,column=6)
        i+=1   
    c_view.pack(fill=BOTH, expand=1)
	
	
def view_client():
    flag='view_client'

    view_client=Tk()
    view_client.configure(background="white")
    view_client.state("zoomed")

    sw= ScrolledWindow(view_client)
    sw.pack(fill=BOTH,expand=1)

    view_client_main_frame = tk.Frame(sw.window,background="white")
    column_frame = tk.Frame(view_client_main_frame,background="white")
	
    view_client.title('View Client Details')
    #view_client.wm_iconbitmap('favicon.ico')
    Label(column_frame,text="View Clients Details",font=("Belwe Bd BT",15),background="white").grid(row=1, column=0,columnspan=3)
    Label(column_frame,text='-'*80,font=("Belwe Bd BT",15),background="white").grid(row=2, column=0,columnspan=3)

    column_frame.pack()
    entry_frame = tk.Frame(view_client_main_frame,background="white")
    Label(entry_frame,text="Name",font=("Belwe Bd BT",15),background="white").grid(row=0, column=1)
    Label(entry_frame,text="Address",font=("Belwe Bd BT",15),background="white").grid(row=0, column=2)
    Label(entry_frame,text="Mobile Number",font=("Belwe Bd BT",15),background="white").grid(row=0, column=3)
    Label(entry_frame,text="Phone Number",font=("Belwe Bd BT",15),background="white").grid(row=0, column=4)
    Label(entry_frame,text="View Transaction Deatils",font=("Belwe Bd BT",15),background="white").grid(row=0, column=5)

    i=0
    
    sql = "select * from clients"
    cur.execute(sql)	
	
    for result in cur:
        Label(entry_frame,text=result[1],font=("Belwe lt BT",15),background="white").grid(row=i+1, column=1)
        Label(entry_frame,text=result[2],font=("Belwe lt BT",15),background="white").grid(row=i+1, column=2)
        Label(entry_frame,text=result[3],font=("Belwe lt BT",15),background="white").grid(row=i+1, column=3)
        Label(entry_frame,text=result[4],font=("Belwe lt BT",15),background="white").grid(row=i+1, column=4)
        tk.Button(entry_frame,width=15,text='Payment Details',font=("Belwe lt BT",15),command=lambda c_name=result[1]: get_detail(c_name)).grid(row=i+1, column=5)
        i+=1
    
    entry_frame.pack()
    """
    button_frame = tk.Frame(view_client,background="white")
    Label(button_frame,background="white").grid(row=0,column=0)
    tk.Button(button_frame,width=20,text='Return to Main Menu',font=("Belwe Bd BT",15),command=view_client.destroy).grid(row=1, column=4)
	
    button_frame.pack()
	"""
    
    view_client_main_frame.pack(fill=BOTH,expand=1)
	
    view_client.mainloop()
    
  
def mainmenu():
    if flag=='expirychk':
        expirychk.destroy()
    
    

# expiry()
#view_client()