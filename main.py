
from tkinter import *
from tkinter import ttk, messagebox
from add_delivery import AddDelivery
from delete_delivery import DeleteDelivery
from get_delivery import GetDelivery


class App:

    def __init__(self, master):
        self.master = master

        self.my_title = Label(text="MY DATA BASE", font="Ariel 20")
        self.my_title.pack(pady=10)

        self.get_btn = Button(self.master, text="Get Delivery", width=40, height=2, font="Ariel 10 bold", bd=4,
                              command=self.get)
        self.get_btn.pack(pady=10)

        self.add_btn = Button(self.master, text="Add Delivery", width=40, height=2, font="Ariel 10 bold", bd=4,
                              command=self.add_delivery)
        self.add_btn.pack(pady=10)

        self.delete_btn = Button(self.master, text="Delete Delivery", width=40, height=2, font="Ariel 10 bold", bd=4,
                                 command=self.delete_delivery)
        self.delete_btn.pack(pady=10)

        self.info_btn = Button(self.master, text="Info", width=40, height=2, font="Ariel 10 bold", bd=4,
                               command=self.info)
        self.info_btn.pack(pady=10)

    def get(self):
        get = GetDelivery()

    def add_delivery(self):
        add = AddDelivery()

    def delete_delivery(self):
        delete = DeleteDelivery()

    def info(self):
        messagebox.showinfo('INFO', 'This is a small Gui created by vadim beletsker')


def main():
    root = Tk()
    app = App(root)
    root.title("GuiDB")
    root.geometry("550x450+150+200")
    root.resizable(False, False)
    root.mainloop()


main()
