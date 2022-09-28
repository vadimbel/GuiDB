from tkinter import *
from tkinter import ttk, messagebox
import db_cursor
import util


class AddDelivery(Toplevel):
    """
    This file contains all elements of 'add delivery' window
    """

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x430+550+200")
        self.title("Add Delivery")
        self.resizable(False, False)

        self.my_title = Label(self, text='Add Delivery', font='Ariel 20 bold')
        self.my_title.place(x=150, y=10)

        # product id label & entry
        self.product_id_lbl = Label(self, text='Product ID :', font='Ariel 12 bold')
        self.product_id_lbl.place(x=20, y=60)

        self.product_id_entry = ttk.Entry(self, width=40)
        self.product_id_entry.place(x=145, y=60)

        # senders id label & entry
        self.senders_id_label = Label(self, text='Senders ID :', font='Ariel 12 bold')
        self.senders_id_label.place(x=20, y=100)

        self.senders_id_entry = ttk.Entry(self, width=40)
        self.senders_id_entry.place(x=145, y=100)

        # receiver id label & entry
        self.receiver_id_label = Label(self, text='Receiver ID :', font='Ariel 12 bold')
        self.receiver_id_label.place(x=20, y=140)

        self.receiver_id_entry = ttk.Entry(self, width=40)
        self.receiver_id_entry.place(x=145, y=140)

        # values for combo boxes
        senders_value = StringVar()
        receiver_value = StringVar()
        cities = ['Haifa', 'Tel Aviv', 'Eilat', 'Bear Sheva']

        # senders city label & combobox
        self.senders_city_label = Label(self, text='Senders City :', font='Ariel 12 bold')
        self.senders_city_label.place(x=20, y=180)

        self.senders_city_combobox = ttk.Combobox(self, textvariable=senders_value, values=cities, state='readonly')
        self.senders_city_combobox.place(x=145, y=180)

        # receiver city label & combobox
        self.receiver_city_label = Label(self, text='Receiver City :', font='Ariel 12 bold')
        self.receiver_city_label.place(x=20, y=220)

        self.receiver_city_combobox = ttk.Combobox(self, textvariable=receiver_value, values=cities, state='readonly')
        self.receiver_city_combobox.place(x=145, y=220)

        # Add , Clear , Cancel buttons
        self.add_btn = Button(self, text='Add', width=40, height=1, bd=3, font='Ariel 10 bold', command=self.add)
        self.add_btn.place(x=90, y=270)

        self.clear_btn = Button(self, text='Clear', width=40, height=1, bd=3, font='Ariel 10 bold', command=self.clear)
        self.clear_btn.place(x=90, y=310)

        self.cancel_btn = Button(self, text='Cancel', width=40, height=1, bd=3, font='Ariel 10 bold',
                                 command=self.cancel)
        self.cancel_btn.place(x=90, y=350)

    def add(self):
        """
        This function will be activated when user clicks on 'Add' button on 'Add delivery' window .
        All text filed (entry) must be filled , if on eof the fields is empty -> send error message to user .
        :return:
        """
        # get all values from elements
        product_id = self.product_id_entry.get()
        senders_id = self.senders_id_entry.get()
        receiver_id = self.receiver_id_entry.get()
        senders_city = self.senders_city_combobox.get()
        receiver_city = self.receiver_city_combobox.get()

        # create list to check if all of them have values
        data_lst = [product_id, senders_id, receiver_id, senders_city, receiver_city]

        # check the values , if some fields don't have value -> send error message then end function
        for i in data_lst:
            if i == '':
                messagebox.showerror('ERROR', 'ALL FIELDS MUST BE FILLED')
                return

        # id must be an integer
        if not (util.check_id(product_id) and util.check_id(senders_id) and util.check_id(receiver_id)):
            messagebox.showerror('ERROR', 'ID MUST BE AN INTEGER')
            return

        # if all fields are filed -> add new delivery to db
        sql = 'INSERT INTO delivery (product_id, senders_id, receiver_id, senders_city, receiver_city) VALUES ' \
              '(%s, %s, %s, %s, %s)'
        val = (product_id, senders_id, receiver_id, senders_city, receiver_city)
        db_cursor.cursor.execute(sql, val)

        db_cursor.conn.commit()

        messagebox.showinfo('SUCCESS', 'New value was added successfully')

    def clear(self):
        """
        This function will be activated when user click on 'Clear' button on 'Add delivery' window .
        clear all fields .
        :return:
        """
        self.product_id_entry.delete(0, END)
        self.product_id_entry.insert(0, '')
        self.senders_id_entry.delete(0, END)
        self.senders_id_entry.insert(0, '')
        self.receiver_id_entry.delete(0, END)
        self.receiver_id_entry.insert(0, '')
        self.senders_city_combobox.set('')
        self.receiver_city_combobox.set('')

    def cancel(self):
        """
        This function will be activated when user click on 'Cancel' button on 'Add delivery' window .
        exit the window .
        :return:
        """
        self.destroy()
