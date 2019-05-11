import pickle
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import dbapi2 as sqlite
from datetime import date
from log_maker import *
from tkinter.tix import *


month = ['January','February','March','April','May','Jun','July','August','September','October','November','December']
now = date.today()
current_month = now.month-1
mo = month[current_month]
print(mo)

c=sqlite.connect("aquatech.sqlite")
cur=c.cursor()


def load_pickle():
    global labour_names
    try:
        pickle_read = open("dict.pickle","rb")
        dict_temp = pickle.load(pickle_read)
        total_temp = pickle.load(pickle_read)
        pickle_read.close()
        #print(dict)
    except Exception as exp:
        print(exp)
        insert_error(exp)
        dict_temp = {i:{j:[0 for i in range(31)] for j in labour_names} for i in month }
        total_temp = {i:{j:0 for j in labour_names} for i in month }
        #print(dict)
	
    for name in labour_names:
        for m in month:
            if name not in dict_temp[m]:
                dict_temp[m][name] = [0 for i in range(31)]
                total_temp[m][name] = 0
    return dict_temp,total_temp
			

	
			
			
			


def readstatus(ch_var):
    global labour_names,mo,dict,var,awindow
    for name in labour_names:
        print(name,mo)
        a = 0
        for i in range(31):
            if ch_var[mo][name][i].get() is 1:
                print(ch_var[mo][name][i].get(),end=" ")
                a+=1
            dict[mo][name][i] = ch_var[mo][name][i].get()
        total[mo][name] = a
        print(total)
    #print(dict)
    pickle_out  = open("dict.pickle","wb")
    pickle.dump(dict,pickle_out)
    pickle.dump(total,pickle_out)
    pickle_out.close()

    messagebox.showinfo('Successfull', 'Attendance Successfully Inserted')
    awindow.destroy()	


	
def change(dict):
    global mo
    var = dict.copy()

    for name in labour_names:
        for i in range(31):
            var[mo][name][i] = IntVar(value=dict[mo][name][i])
            #ch_var[mo][name][i].set(dict[mo][name][i].get())
	
    return var
def change_month(w):
    global current_month,mo,month,awindow
    current_month = current_month+w
    if current_month<0:
        current_month = 11
    if current_month>11:
        current_month = 0
    mo = month[current_month]
    print(mo)
    awindow.destroy()
    main()
	
def main():
    global dict,mo,labour_names,var,awindow,total


    sql = "select name from labour_details"
    cur.execute(sql)
    result =  cur.fetchall()
    labour_names = [name[0] for name in result]

    print(list(labour_names))

    awindow = Tk()
    awindow.title("Attendance Register")
    awindow.configure(background="white")
    awindow.state("zoomed")
    
    sw = ScrolledWindow(awindow)
    sw.pack()

    window = tk.Frame(sw.window,background="white")
    dict,total = load_pickle()
    #mo = 'Jun'
    var = change(dict)

    Label(window,text="-"*250,font=("Belwe Bd BT",10),background="white").grid(row=0,column=0,columnspan=32)
    tk.Button(window,text="Previous",font=("Belwe Bd BT",10),command=lambda : change_month(-1)).grid(row=1,column=0)
    Label(window,text=mo,font=("Belwe Bd BT",15),background="white").grid(row=1,column=1,columnspan=30)
    tk.Button(window,text="Next",font=("Belwe Bd BT",10),command=lambda : change_month(+1)).grid(row=1,column=31)
    Label(window,text="-"*250,font=("Belwe Bd BT",10),background="white").grid(row=2,column=0,columnspan=32)

    for i in range(1,32):
        Label(window,text=i,font=("Belwe lt BT",10),background="white").grid(row=3,column=i)

    j = 3

    for name in labour_names:
        Label(window,text=name,font=("Belwe lt BT",12),background="white").grid(row=j+1,column=0)
    
        for i in range(31):
        
            Checkbutton(window, text='', var=var[mo][name][i],onvalue = 1, offvalue = 0,command=lambda : print(var[mo][name][i].get())).grid(column=i+1, row=j+1)
        j+=1        

    tk.Button(window,text="Update",font=("Belwe Bd BT",10),command=lambda ch = var:readstatus(ch)).grid(row=j+3+1,column=0)
    window.pack(fill=BOTH,expand=1)

    window.mainloop()

