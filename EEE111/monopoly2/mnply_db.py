from tkinter import *
import tkinter as tk
import sqlite3
class MonopolyDB():
    global edit_data
    global open_save
    global delete_data
    global update_data
    global record_data

    def record_data():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("INSERT INTO Game_Saves VALUES (:p_name, :p_bank, :p_stat)",
                        {
                            'p_name': pl_name.get(),
                            'p_bank': pl_bank.get(),
                            'p_stat': pl_stat.get(),
                        })

        #p_name.delete(0, END)
        #p_bank.delete(0, END)
        #p_stat.delete(0, END)

        conn.commit()
        conn.close()

    def edit_data():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        id_records = id_enter5.get()

        pointer.execute("""UPDATE Game_Saves SET
                        
                            player_name = :p_name,
                            player_bank = :p_bank,
                            player_status = :p_stat
                        
                        WHERE oid = :oid""",
                        {
                            'p_name': p_name_edit.get(),
                            'p_bank': p_bank_edit.get(),
                            'p_stat': p_stat_edit.get(),
                            'oid': id_records
                        }
                        )
        #p_name.delete(0, END)
        #p_bank.delete(0, END)
        #p_stat.delete(0, END)

        conn.commit()
        conn.close()

        edit.destroy()

    def update_data():
        global edit
        edit = tk.Tk()
        edit.title("Monopoly Game Load")
        edit.iconbitmap(r"C:\Users\Nathan Salvador\EEE111\monopoly\database")
        edit.geometry('400x250')

        conn_edit = sqlite3.connect('gamesaves.db')
        pointer_edit = conn_edit.cursor()
        
        global p_name_edit
        global p_bank_edit
        global p_stat_edit

        p_name_edit = Entry(edit, width = 25)
        p_name_edit.grid(row = 0, column = 1, padx = 12)
        p_name_header_edit = Label(edit, text = "Player Name")
        p_name_header_edit.grid(row = 0, column = 0)

        p_bank_edit = Entry(edit, width = 25)
        p_bank_edit.grid(row = 1, column = 1, padx = 12)
        p_bank_header_edit = Label(edit, text = "Bank Balance")
        p_bank_header_edit.grid(row = 1, column = 0)

        p_stat_edit = Entry(edit, width = 25)
        p_stat_edit.grid(row = 2, column = 1, padx = 12)
        p_stat_header_edit = Label(edit, text = "Gameplay Status")
        p_stat_header_edit.grid(row = 2, column = 0)

        edit_button_edit = Button(edit, text = "Edit Game Load", command = edit_data)
        edit_button_edit.grid(row = 4, column = 0,  padx = 12, columnspan = 2)

        id_records = id_enter5.get()
        print(id_enter5.get())

        pointer_edit.execute("SELECT * FROM Game_Saves WHERE oid = " + id_records)
        
        data_edit = pointer_edit.fetchall()
        print(data_edit)

        for datum_edit in data_edit:
            p_name_edit.insert(0, datum_edit[0])
            p_bank_edit.insert(0, datum_edit[1])
            p_stat_edit.insert(0, datum_edit[2])

        conn_edit.commit()
        conn_edit.close()

    def delete_data():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()

        pointer.execute("DELETE from Game_Saves WHERE oid = " + id_enter5.get())

        conn.commit()
        conn.close()

    def open_save():
        conn = sqlite3.connect('gamesaves.db')
        pointer = conn.cursor()
        
        pointer.execute("SELECT *, oid FROM Game_Saves")
        data = pointer.fetchall()
        print(data)

        show_data = ''
        for datum in data:
            show_data += str(datum[3]) + "    Name: " + str(datum[0]) + "\t  Balance: " + str(datum[1]) + "\t Status: " + str(datum[2]) + "\n"
        
        data_display = Label(root, text = show_data)
        data_display.grid(row = 8, column = 0, columnspan = 2)
        conn.commit()
        conn.close()

root = tk.Tk()
root.title("Monopoly Game Load")
root.iconbitmap(r"C:\Users\Nathan Salvador\EEE111\monopoly\database")
root.geometry('500x500')

conn = sqlite3.connect('gamesaves.db')
pointer = conn.cursor()

'''
pointer.execute("""CREATE TABLE Game_Saves (
                player_name text,
                player_bank integer,
                player_status text
)

""")
'''
pl_name = Entry(root, width = 25)
pl_name.grid(row = 0, column = 1, padx = 12)
p_name_header = Label(root, text = "Player Name")
p_name_header.grid(row = 0, column = 0)

pl_bank = Entry(root, width = 25)
pl_bank.grid(row = 1, column = 1, padx = 12)
p_bank_header = Label(root, text = "Bank Balance")
p_bank_header.grid(row = 1, column = 0)

pl_stat = Entry(root, width = 25)
pl_stat.grid(row = 2, column = 1, padx = 12)
p_stat_header = Label(root, text = "Gameplay Status")
p_stat_header.grid(row = 2, column = 0)


record_button = Button(root, text = "Save to Game Loads", command = record_data)
record_button.grid(row = 3, column = 0, columnspan = 2, padx = 15, ipadx = 75)

display_save = Button(root, text = "Show saves", command = open_save)
display_save.grid(row = 4, column = 0, columnspan = 2, padx = 15, ipadx = 75) 

id_header = Label(root, text = "Enter Player ID")
id_header.grid(row = 5, column = 0, padx = 15, ipadx = 75)
id_enter5 = Entry(root, width = 30)
id_enter5.grid(row = 5, column = 1)
del_button = Button(root, text = "Delete from Game Loads", command = delete_data)
del_button.grid(row = 6, column = 0, columnspan = 2, padx = 15, ipadx = 75)
update_button = Button(root, text = "Update Game Load", command = update_data)
update_button.grid(row = 7, column = 0, columnspan = 2, padx = 15, ipadx = 75)



conn.commit()
conn.close()

root.destroy()
#root.mainloop()