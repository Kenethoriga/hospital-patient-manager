import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import Page_after_login

def add_patient():
    # Database connection
    def connection():
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='Kababa99#',
                db='PATIENTS_DB',
            )
            return conn
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
            return None

    def refreshTable():
        for data in my_tree.get_children():
            my_tree.delete(data)

        data = read()
        if data:
            for array in data:
                my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
            my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
            my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

    root = Tk()
    root.title("Agakhan University Hospital Management System")
    root.geometry("1166x718")
    root.resizable(0, 0)
    root.state('zoomed')

    my_tree = ttk.Treeview(root)

    # Placeholder variables
    ph1, ph2, ph3, ph4, ph5 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

    def setph(word, num):
        placeholders = [ph1, ph2, ph3, ph4, ph5]
        placeholders[num - 1].set(word)

    def read():
        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM patients")
                results = cursor.fetchall()
                conn.close()
                return results
            except Exception as e:
                messagebox.showerror("Error", f"Error reading data: {e}")
                return []

    def add():
        MOBILE, NAME, DOB, HISTORY, MEDICINES = (
            MOBILEEntry.get(),
            NAMEEntry.get(),
            DOBEntry.get(),
            HISTORYEntry.get(),
            MEDICINESEntry.get(),
        )

        if not all([MOBILE, NAME, DOB, HISTORY, MEDICINES]):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return

        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO patients VALUES (%s, %s, %s, %s, %s)",
                    (MOBILE, NAME, DOB, HISTORY, MEDICINES),
                )
                conn.commit()
                conn.close()
                refreshTable()
            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Error adding patient: {e}")

    def reset():
        if messagebox.askquestion("Warning", "Delete all data?") == "yes":
            conn = connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM patients")
                    conn.commit()
                    conn.close()
                    refreshTable()
                except pymysql.MySQLError as e:
                    messagebox.showerror("Error", f"Error resetting data: {e}")

    def delete():
        if messagebox.askquestion("Warning", "Delete the selected data?") == "yes":
            selected_item = my_tree.selection()
            if not selected_item:
                messagebox.showinfo("Error", "Please select a data row to delete")
                return
            deleteData = str(my_tree.item(selected_item[0])['values'][0])
            conn = connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM patients WHERE MOBILE=%s", (deleteData,))
                    conn.commit()
                    conn.close()
                    refreshTable()
                except pymysql.MySQLError as e:
                    messagebox.showerror("Error", f"Error deleting patient: {e}")

    def search():
        search_params = {
            "MOBILE": MOBILEEntry.get(),
            "NAME": NAMEEntry.get(),
            "DOB": DOBEntry.get(),
            "HISTORY": HISTORYEntry.get(),
            "MEDICINES": MEDICINESEntry.get(),
        }
        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM patients WHERE " + " OR ".join(
                    f"{key} LIKE %s" for key in search_params if search_params[key]
                )
                values = tuple(f"%{value}%" for value in search_params.values() if value)
                cursor.execute(query, values)
                results = cursor.fetchall()
                conn.close()
                if results:
                    refreshTable()
                else:
                    messagebox.showinfo("Error", "No data found")
            except pymysql.MySQLError as e:
                messagebox.showerror("Error", f"Error searching patient: {e}")

    # GUI Components
    Label(root, text="PATIENT DATA MANAGEMENT", font=('Arial Bold', 30)).grid(row=0, column=0, columnspan=8, padx=50, pady=40)

    labels = ["MOBILE No", "First Name", "DOB", "Medical History", "Medicines"]
    entries = [ph1, ph2, ph3, ph4, ph5]
    for i, (label_text, placeholder) in enumerate(zip(labels, entries)):
        Label(root, text=label_text, font=('Arial', 15)).grid(row=i + 3, column=0, padx=50, pady=5)
        Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=placeholder).grid(row=i + 3, column=1, columnspan=4)

    # Buttons
    Button(root, text="Add", command=add).grid(row=3, column=10)
    Button(root, text="Delete", command=delete).grid(row=5, column=10)
    Button(root, text="Search", command=search).grid(row=7, column=10)
    Button(root, text="Reset", command=reset).grid(row=9, column=10)

    # Treeview Table
    my_tree['columns'] = ("Mobile", "Name", "Date_of_Birth", "History", "Medicines")
    for column in my_tree['columns']:
        my_tree.heading(column, text=column)
        my_tree.column(column, anchor=W, width=150)
    my_tree.grid(row=8, column=0, columnspan=5, padx=10, pady=20)

    refreshTable()
    root.mainloop()
