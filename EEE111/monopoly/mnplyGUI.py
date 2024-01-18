from mnply_db import *
from tkinter import *
from tkinter import messagebox
from csv import *
from tkinter import filedialog
import tkinter as tk
import sqlite3
import csv
import os

dir = os.path.dirname(os.path.abspath(__file__))
path1 = os.path.join(dir, 'database')

def csv_import():
   conn = sqlite3.connect('gamesaves.db')
   pointer = conn.cursor()
   id_list = []
   name_list = []
   bank_list = []
   stat_list = []
   file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
   if file_path:
      try:
         with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                id_list.append(line[0])
                name_list.append(line[1])
                bank_list.append(line[2])
                stat_list.append(line[3])
      except Exception as e:
         print(f"Error: {e}")
   
   show_data = ''
   for i in range(len(id_list)):
       show_data += "Name: " + str(name_list[i]) + "\t  Balance: " + str(bank_list[i]) + "\t Status: " + str(stat_list[i]) + "\n"

   for i in range(len(id_list)):
       pointer.execute("INSERT INTO Game_Saves VALUES (:p_name, :p_bank, :p_stat)",
                        {
                            'p_name': name_list[i],
                            'p_bank': bank_list[i],
                            'p_stat': stat_list[i],
                        })
   messagebox.showinfo("Import", "The following player data has been imported: \n" + show_data)
   conn.commit()
   conn.close()

def delete_data1():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("DELETE from Game_Saves WHERE oid = " + id_enter5.get())

        conn.commit()
        conn.close()
    
def data_disp():
    disp = tk.Tk()
    disp.title("Player Data")
    disp.iconbitmap(path1)
    disp.geometry('500x500')

    conn_disp = sqlite3.connect('gamesaves.db')
    pointer_disp = conn_disp.cursor()

    pointer_disp.execute("SELECT *, oid FROM Game_Saves")
    data = pointer_disp.fetchall()

    show_data = ''
    for datum in data:
        show_data += str(datum[3]) + "    Name: " + str(datum[0]) + "\t  Balance: " + str(datum[1]) + "\t Status: " + str(datum[2]) + "\n"
        
    data_display = Label(disp, text = show_data)
    data_display.grid(row = 8, column = 0, columnspan = 2)

    conn_disp.commit()
    conn_disp.close()

    disp.mainloop()

def csv_export():
    conn = sqlite3.connect('gamesaves.db')
    pointer = conn.cursor()
        
    pointer.execute("SELECT *, oid FROM Game_Saves")
    data = pointer.fetchall()

    csv_list = []

    data_list = []
    for datum in data:
        data_list.append(f"{datum[3]} " + f"{datum[0]} " + f"{datum[1]} " + f"{datum[2]} \n")

    csv_list.append(data_list)

    with open("mnply.csv", "w") as file:
        Writer = writer(file)
        Writer.writerow(["Name","Balance","Status"])
        Writer.writerows(csv_list)
        messagebox.showinfo("Export","Data has been exported")
        

    conn.commit()
    conn.close()
    
def load_data1(id_num):
    conn = sqlite3.connect('gamesaves.db')
    pointer = conn.cursor()

    id_number = str(id_num())

    query = "SELECT * FROM Game_Saves WHERE oid = ?"

    pointer.execute(query, (id_number,))

    data = pointer.fetchall()

    pointer.execute(query, (id_number,))
    pl_name1.delete(0, END)
    pl_bank1.delete(0, END)
    pl_stat1.delete(0, END)

    for datum in data:
       pl_name1.insert(0, datum[0])
       pl_bank1.insert(0, datum[1])
       pl_stat1.insert(0, datum[2])

    conn.commit()
    conn.close()

def load_data2(id_num):
    conn = sqlite3.connect('gamesaves.db')
    pointer = conn.cursor()

    id_number = str(id_num())

    query = "SELECT * FROM Game_Saves WHERE oid = ?"

    pointer.execute(query, (id_number,))

    data = pointer.fetchall()

    pl_name2.delete(0, END)
    pl_bank2.delete(0, END)
    pl_stat2.delete(0, END)

    for datum in data:
       pl_name2.insert(0, datum[0])
       pl_bank2.insert(0, datum[1])
       pl_stat2.insert(0, datum[2])

    conn.commit()
    conn.close()

def load_data3(id_num):
    conn = sqlite3.connect('gamesaves.db')
    pointer = conn.cursor()

    id_number = str(id_num())

    query = "SELECT * FROM Game_Saves WHERE oid = ?"

    pointer.execute(query, (id_number,))

    data = pointer.fetchall()

    pl_name3.delete(0, END)
    pl_bank3.delete(0, END)
    pl_stat3.delete(0, END)

    for datum in data:
       pl_name3.insert(0, datum[0])
       pl_bank3.insert(0, datum[1])
       pl_stat3.insert(0, datum[2])

    conn.commit()
    conn.close()

def load_data4(id_num):
    conn = sqlite3.connect('gamesaves.db')
    pointer = conn.cursor()

    id_number = str(id_num())

    query = "SELECT * FROM Game_Saves WHERE oid = ?"

    pointer.execute(query, (id_number,))

    data = pointer.fetchall()

    for datum in data:
       pl_name4.insert(0, datum[0])
       pl_bank4.insert(0, datum[1])
       pl_stat4.insert(0, datum[2])

    conn.commit()
    conn.close()


def record_data1():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("INSERT INTO Game_Saves VALUES (:p_name, :p_bank, :p_stat)",
                        {
                            'p_name': pl_name1.get(),
                            'p_bank': pl_bank1.get(),
                            'p_stat': pl_stat1.get(),
                        })

        #p_name.delete(0, END)
        #p_bank.delete(0, END)
        #p_stat.delete(0, END)

        conn.commit()
        conn.close()

def record_data2():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("INSERT INTO Game_Saves VALUES (:p_name, :p_bank, :p_stat)",
                        {
                            'p_name': pl_name2.get(),
                            'p_bank': pl_bank2.get(),
                            'p_stat': pl_stat2.get(),
                        })

        #p_name.delete(0, END)
        #p_bank.delete(0, END)
        #p_stat.delete(0, END)

        conn.commit()
        conn.close()

def record_data3():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("INSERT INTO Game_Saves VALUES (:p_name, :p_bank, :p_stat)",
                        {
                            'p_name': pl_name3.get(),
                            'p_bank': pl_bank3.get(),
                            'p_stat': pl_stat3.get(),
                        })

        #p_name.delete(0, END)
        #p_bank.delete(0, END)
        #p_stat.delete(0, END)

        conn.commit()
        conn.close()

def record_data4():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("INSERT INTO Game_Saves VALUES (:p_name, :p_bank, :p_stat)",
                        {
                            'p_name': pl_name4.get(),
                            'p_bank': pl_bank4.get(),
                            'p_stat': pl_stat4.get(),
                        })

        #p_name.delete(0, END)
        #p_bank.delete(0, END)
        #p_stat.delete(0, END)

        conn.commit()
        conn.close()

def bank_alter1(op):
    amount = float(bank_input1.get())
    current_amount = float(pl_bank1.get())
    if op == "add":
        new_amount = current_amount + amount
    else:
        new_amount = current_amount - amount
    text = str(new_amount)
    pl_bank1.delete(0, END)
    pl_bank1.insert(END, text)

    if float(pl_bank1.get()) < 0:
        br = "BANKRUPT"
        pl_stat1.delete(0, END)
        pl_stat1.insert(END, br)
    elif float(pl_bank1.get()) == 0:
         br = "BANKRUPT"
         pl_stat1.delete(0, END)
         pl_stat1.insert(END, br)
    else: 
        at = "ACTIVE"
        pl_stat1.delete(0, END)
        pl_stat1.insert(END, at)

def bank_alter2(op):
    amount = float(bank_input2.get())
    current_amount = float(pl_bank2.get())
    if op == "add":
        new_amount = current_amount + amount
    else:
        new_amount = current_amount - amount
    text = str(new_amount)
    pl_bank2.delete(0, END)
    pl_bank2.insert(END, text)

    if float(pl_bank2.get()) < 0:
        br = "BANKRUPT"
        pl_stat2.delete(0, END)
        pl_stat2.insert(END, br)
    elif float(pl_bank2.get()) == 0:
         br = "BANKRUPT"
         pl_stat2.delete(0, END)
         pl_stat2.insert(END, br)
    else: 
        at = "ACTIVE"
        pl_stat2.delete(0, END)
        pl_stat2.insert(END, at)

def bank_alter3(op):
    amount = float(bank_input3.get())
    current_amount = float(pl_bank3.get())
    if op == "add":
        new_amount = current_amount + amount
    else:
        new_amount = current_amount - amount
    text = str(new_amount)
    pl_bank3.delete(0, END)
    pl_bank3.insert(END, text)

    if float(pl_bank3.get()) < 0:
        br = "BANKRUPT"
        pl_stat3.delete(0, END)
        pl_stat3.insert(END, br)
    elif float(pl_bank3.get()) == 0:
         br = "BANKRUPT"
         pl_stat3.delete(0, END)
         pl_stat3.insert(END, br)
    else: 
        at = "ACTIVE"
        pl_stat3.delete(0, END)
        pl_stat3.insert(END, at)

def bank_alter4(op):
    amount = float(bank_input4.get())
    current_amount = float(pl_bank4.get())
    if op == "add":
        new_amount = current_amount + amount
    else:
        new_amount = current_amount - amount
    text = str(new_amount)
    pl_bank4.delete(0, END)
    pl_bank4.insert(END, text)

    if float(pl_bank4.get()) < 0:
        br = "BANKRUPT"
        pl_stat4.delete(0, END)
        pl_stat4.insert(END, br)
    elif float(pl_bank4.get()) == 0:
         br = "BANKRUPT"
         pl_stat4.delete(0, END)
         pl_stat4.insert(END, br)
    else: 
        at = "ACTIVE"
        pl_stat4.delete(0, END)
        pl_stat4.insert(END, at)

def pass_go1():
    current_amount = float(pl_bank1.get())
    new_amount = current_amount + 200
    balance = str(new_amount)
    pl_bank1.delete(0, END)
    pl_bank1.insert(END, balance)
    at = "ACTIVE"
    pl_stat1.delete(0, END)
    pl_stat1.insert(END, at)

def pass_go2():
    current_amount = float(pl_bank2.get())
    new_amount = current_amount + 200
    balance = str(new_amount)
    pl_bank2.delete(0, END)
    pl_bank2.insert(END, balance)
    at = "ACTIVE"
    pl_stat2.delete(0, END)
    pl_stat2.insert(END, at)

def pass_go3():
    current_amount = float(pl_bank3.get())
    new_amount = current_amount + 200
    balance = str(new_amount)
    pl_bank3.delete(0, END)
    pl_bank3.insert(END, balance)
    at = "ACTIVE"
    pl_stat3.delete(0, END)
    pl_stat3.insert(END, at)

def pass_go4():
    current_amount = float(pl_bank4.get())
    new_amount = current_amount + 200
    balance = str(new_amount)
    pl_bank4.delete(0, END)
    pl_bank4.insert(END, balance)
    at = "ACTIVE"
    pl_stat4.delete(0, END)
    pl_stat4.insert(END, at)
    

root = tk.Tk()
root.title("Monopoly Bank Tracker")

player_nametags = []
player_bank = []
player_status = []
player_id = []

bank_input1 = Entry(root)
bank_input1.grid(row = 4, column = 0, padx = 8, pady = 8)
bank_input2 = Entry(root)
bank_input2.grid(row = 4, column = 1, padx = 8, pady = 8)
bank_input3 = Entry(root)
bank_input3.grid(row = 4, column = 2, padx = 8, pady = 8)
bank_input4 = Entry(root)
bank_input4.grid(row = 4, column = 3, padx = 8, pady = 8)


pl_name1 = Entry(root)
pl_name1.grid(row = 0, column = 0, padx = 8, pady = 8)
player_nametags.append(pl_name1)
pl_name2 = Entry(root)
pl_name2.grid(row = 0, column = 1, padx = 8, pady = 8)
player_nametags.append(pl_name2)
pl_name3 = Entry(root)
pl_name3.grid(row = 0, column = 2, padx = 8, pady = 8)
player_nametags.append(pl_name3)
pl_name4 = Entry(root)
pl_name4.grid(row = 0, column = 3, padx = 8, pady = 8)
player_nametags.append(pl_name4)

pl_bank1 = Entry(root)
pl_bank1.grid(row = 1 , column = 0, padx = 8, pady = 10)
pl_bank1.insert(0, "1500")
player_bank.append(pl_bank1)
pl_bank2 = Entry(root)
pl_bank2.grid(row = 1 , column = 1, padx = 8, pady = 10)
pl_bank2.insert(0, "1500")
player_bank.append(pl_bank2)
pl_bank3 = Entry(root)
pl_bank3.grid(row = 1 , column = 2, padx = 8, pady = 10)
pl_bank3.insert(0, "1500")
player_bank.append(pl_bank3)
pl_bank4 = Entry(root)
pl_bank4.grid(row = 1 , column = 3, padx = 8, pady = 10)
pl_bank4.insert(0, "1500")
player_bank.append(pl_bank4)

pl_stat1 = Entry(root)
pl_stat1.insert(0, "ACTIVE")
pl_stat1.grid(row = 2, column = 0, padx = 15, pady = 18)
player_status.append(pl_stat1)
pl_stat2 = Entry(root)
pl_stat2.insert(0, "ACTIVE")
pl_stat2.grid(row = 2, column = 1, padx = 15, pady = 18)
player_status.append(pl_stat2)
pl_stat3 = Entry(root)
pl_stat3.insert(0, "ACTIVE")
pl_stat3.grid(row = 2, column = 2, padx = 15, pady = 18)
player_status.append(pl_stat3)
pl_stat4 = Entry(root)
pl_stat4.insert(0, "ACTIVE")
pl_stat4.grid(row = 2, column = 3, padx = 15, pady = 18)
player_status.append(pl_stat4)

go_button1 = Button(root, text = "Pass GO", command = lambda : pass_go1())
go_button1.grid(row = 3, column = 0, padx = 7, pady = 7)
go_button2 = Button(root, text = "Pass GO", command = lambda : pass_go2())
go_button2.grid(row = 3, column = 1, padx = 7, pady = 7) 
go_button3 = Button(root, text = "Pass GO", command = lambda : pass_go3())
go_button3.grid(row = 3, column = 2, padx = 7, pady = 7) 
go_button4 = Button(root, text = "Pass GO", command = lambda : pass_go4())
go_button4.grid(row = 3, column = 3, padx = 7, pady = 7) 

add_button1 = Button(root, text="Add", command = lambda x = "add" : bank_alter1(x))
add_button1.grid(row = 5, column = 0, padx = 7, pady = 7)
add_button2 = Button(root, text="Add", command = lambda x = "add" : bank_alter2(x))
add_button2.grid(row = 5, column = 1, padx = 7, pady = 7)
add_button3 = Button(root, text="Add", command = lambda x = "add" : bank_alter3(x))
add_button3.grid(row = 5, column = 2, padx = 7, pady = 7)
add_button4 = Button(root, text="Add", command = lambda x = "add" : bank_alter4(x))
add_button4.grid(row = 5, column = 3, padx = 7, pady = 7)

minus_button1 = Button(root, text="Subtract", command = lambda x = "sub" : bank_alter1(x))
minus_button1.grid(row = 6, column = 0, padx = 7, pady = 7)
minus_button2 = Button(root, text="Subtract", command = lambda x = "sub" : bank_alter2(x))
minus_button2.grid(row = 6, column = 1, padx = 7, pady = 7)
minus_button3 = Button(root, text="Subtract", command = lambda x = "sub" : bank_alter3(x))
minus_button3.grid(row = 6, column = 2, padx = 7, pady = 7)
minus_button4 = Button(root, text="Subtract", command = lambda x = "sub" : bank_alter4(x))
minus_button4.grid(row = 6, column = 3, padx = 7, pady = 7)

save_button1 = Button(root, text = "Save Player Data", command = record_data1)
save_button1.grid(row = 9, column = 0, padx = 7, pady = 13)
save_button2 = Button(root, text = "Save Player Data", command = record_data2)
save_button2.grid(row = 9, column = 1, padx = 7, pady = 13)
save_button3 = Button(root, text = "Save Player Data", command = record_data3)
save_button3.grid(row = 9, column = 2, padx = 7, pady = 13)
save_button4 = Button(root, text = "Save Player Data", command = record_data4)
save_button4.grid(row = 9, column = 3, padx = 7, pady = 13)

id_header1 = Label(root, text = "Enter Player ID")
id_header1.grid(row = 10, column = 0, padx = 15, ipadx = 75)
id_enter1 = Entry(root, width = 30)
id_enter1.grid(row = 11, column = 0)
player_id.append(id_enter1)
id_header2 = Label(root, text = "Enter Player ID")
id_header2.grid(row = 10, column = 1, padx = 15, ipadx = 75)
id_enter2 = Entry(root, width = 30)
id_enter2.grid(row = 11, column = 1)
player_id.append(id_enter2)
id_header3 = Label(root, text = "Enter Player ID")
id_header3.grid(row = 10, column = 2, padx = 15, ipadx = 75)
id_enter3 = Entry(root, width = 30)
id_enter3.grid(row = 11, column = 2)
player_id.append(id_enter3)
id_header4 = Label(root, text = "Enter Player ID")
id_header4.grid(row = 10, column = 3, padx = 15, ipadx = 75)
id_enter4 = Entry(root, width = 30)
id_enter4.grid(row = 11, column = 3)
player_id.append(id_enter4)

load_button1 = Button(root, text = "Load Player Data", command = lambda x = id_enter1.get : load_data1(x))
load_button1.grid(row = 12, column = 0, padx = 7, pady = 13)
load_button2 = Button(root, text = "Load Player Data", command = lambda x = id_enter2.get : load_data2(x))
load_button2.grid(row = 12, column = 1, padx = 7, pady = 13)
load_button3 = Button(root, text = "Load Player Data", command = lambda x = id_enter3.get : load_data3(x))
load_button3.grid(row = 12, column = 2, padx = 7, pady = 13)
load_button4 = Button(root, text = "Load Player Data", command = lambda x = id_enter4.get : load_data4(x))
load_button4.grid(row = 12, column = 3, padx = 7, pady = 13)

csv_exp = Button(root, text = "Export to CSV File", command = csv_export)
csv_exp.grid(row = 14, column = 0, padx = 7, pady = 13)
csv_imp = Button(root, text = "Import Player Data", command = csv_import)
csv_imp.grid(row = 14, column = 1, padx = 7, pady = 13)
disp_button = Button(text = "Show Database", command = data_disp)
disp_button.grid(row = 14, column = 2, padx = 7, pady = 13)
del_button = Button(root, text = "Delete player data (enter ID): ", command = delete_data1)
del_button.grid(row = 13, column = 3, padx = 7, pady = 13)
id_enter5 = Entry(root, width = 30)
id_enter5.grid(row = 14, column = 3, padx = 7, pady = 13)


root.mainloop()
