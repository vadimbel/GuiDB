from tkinter import *
from tkinter import ttk, messagebox
import db_cursor


class DeleteDelivery(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+550+200")
        self.title("Delete Delivery")
        self.resizable(False, False)

        self.my_title = Label(self, text='Delete Delivery', font='Ariel 20 bold')
        self.my_title.place(x=150, y=10)

        # product id label & entry
        self.product_id_lbl = Label(self, text='Product ID :', font='Ariel 12 bold')
        self.product_id_lbl.place(x=20, y=60)

        self.product_id_entry = ttk.Entry(self, width=40)
        self.product_id_entry.place(x=145, y=60)

        # Delete , Clear , Cancel buttons
        self.delete_btn = Button(self, text='Delete', width=40, height=1, bd=3, font='Ariel 10 bold',
                                 command=self.delete)
        self.delete_btn.place(x=90, y=120)

        self.clear_btn = Button(self, text='Clear', width=40, height=1, bd=3, font='Ariel 10 bold', command=self.clear)
        self.clear_btn.place(x=90, y=160)

        self.cancel_btn = Button(self, text='Cancel', width=40, height=1, bd=3, font='Ariel 10 bold',
                                 command=self.cancel)
        self.cancel_btn.place(x=90, y=200)

    def delete(self):
        # check if text fields is not empty
        product_id = self.product_id_entry.get()
        if product_id == '':
            messagebox.showerror("ERROR", "Product ID field is empty")
            return

        # search the product id in db
        sql = "SELECT * FROM delivery WHERE product_id = %s"
        adr = (product_id, )

        # execute the query
        db_cursor.cursor.execute(sql, adr)

        # result is a list of column from db
        result = db_cursor.cursor.fetchall()

        # if the list is empty -> there is no column with 'product_id' provided by the user
        if len(result) == 0:
            messagebox.showerror('ERROR', 'No deliveries with product ID provided')
            return

        sql = "DELETE FROM delivery WHERE product_id = %s"
        adr = (product_id, )

        db_cursor.cursor.execute(sql, adr)
        db_cursor.conn.commit()

        messagebox.showinfo('INFO', 'Delivery was deleted successfully')


    def clear(self):
        self.product_id_entry.delete(0, END)
        self.product_id_entry.insert(0, '')

    def cancel(self):
        self.destroy()

