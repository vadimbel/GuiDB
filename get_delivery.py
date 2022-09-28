from tkinter import *
from tkinter import ttk, messagebox
import db_cursor


class GetDelivery(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("450x300+550+200")
        self.title("Get Delivery")
        self.resizable(False, False)

        self.my_title = Label(self, text='Get Delivery', font='Ariel 20 bold')
        self.my_title.place(x=140, y=10)

        # by options label & combobox
        self.options_lbl = Label(self, text='By : ', font='Ariel 12 bold')
        self.options_lbl.place(x=20, y=60)

        self.options_result = StringVar()
        options = ['', 'By product id', 'By Sender id', 'By receiver id', 'By city from', 'By city to']

        self.options_combobox = ttk.Combobox(self, textvariable=self.options_result, values=options, state='readonly',
                                             width=40)
        self.options_combobox.place(x=90, y=63)

        # label for option
        self.option_lbl = Label(self, text='Value : ', font='Ariel 12 bold')
        self.option_lbl.place(x=20, y=100)

        # entry for the chosen option
        self.option_entry = ttk.Entry(self, width=43)
        self.option_entry.place(x=90, y=102)

        # get, clear, cancel buttons
        self.get_btn = Button(self, text='Get', width=40, height=1, bd=3, font='Ariel 10 bold', command=self.get)
        self.get_btn.place(x=70, y=140)
        self.clear_btn = Button(self, text='Clear', width=40, height=1, bd=3, font='Ariel 10 bold', command=self.clear)
        self.clear_btn.place(x=70, y=180)
        self.cancel_btn = Button(self, text='Cancel', width=40, height=1, bd=3, font='Ariel 10 bold',
                                 command=self.cancel)
        self.cancel_btn.place(x=70, y=220)

    def get(self):
        # check what user chose and create the right query
        if self.options_result.get() == 'By product id':
            sql = "SELECT * FROM delivery WHERE product_id = %s"
            adr = (self.option_entry.get(), )

        elif self.options_result.get() == 'By Sender id':
            sql = "SELECT * FROM delivery WHERE senders_id = %s"
            adr = (self.option_entry.get(), )

        elif self.options_result.get() == 'By receiver id':
            sql = "SELECT * FROM delivery WHERE receiver_id = %s"
            adr = (self.option_entry.get(), )

        elif self.options_result.get() == 'By city from':
            sql = "SELECT * FROM delivery WHERE senders_city = %s"
            adr = (self.option_entry.get(), )

        elif self.options_result.get() == 'By city to':
            sql = "SELECT * FROM delivery WHERE receiver_city = %s"
            adr = (self.option_entry.get(), )

        # data provided to entry box was not found in db
        else:
            messagebox.showerror("ERROR", "No values with provided data")
            return

        db_cursor.cursor.execute(sql, adr)
        result = db_cursor.cursor.fetchall()

        # create new file and write the data from query above
        with open('data', 'w') as f:
            for res in result:
                s = ""
                for r in res:
                    s += str(r)+' '
                f.write(s)
                f.write('\n')

    def clear(self):
        self.option_entry.delete(0, END)
        self.option_entry.insert(0, '')

    def cancel(self):
        self.destroy()
