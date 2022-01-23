from tkinter import *


class Regitration():

    def __init__(self, game):
        self.screen = None
        self.connection = game

        self.username_info = None
        self.phone_info = None

        self.username_entry = None
        self.phone_entry = None

        self.username = None
        self.phone = None

    def register_user(self):
        self.username_info = self.username.get()
        self.phone_info = self.phone.get()
        if self.connection.user.check_user(self.username_info) and self.connection.user.check_phone(self.phone_info):
            player = self.connection.user.get_user(self.username_info)
            self.connection.set_user(player)
            Label(self.screen, text = "Ingreso exitoso", fg = "green", font = ("calibri", 11)).pack()
            self.username_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.screen.destroy()
            
        elif (self.connection.user.check_user(self.username_info) == False) and self.connection.user.check_phone(self.phone_info):
            _id = self.connection.user.insert(self.username_info, self.phone_info, 0)
            self.connection.set_new_user(_id, self.username_info, self.phone_info, 0)
            Label(self.screen, text = "Registro exitoso", fg = "green", font = ("calibri", 11)).pack()
            self.username_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.screen.destroy()
        else:
            self.username_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            Label(self.screen, text = "Número de celular iválido", fg = "red", font = ("calibri", 11)).pack()

    def main_screen(self):     
        self.screen = Tk()
        self.screen.geometry("300x200")
        self.screen.title("Resgistro")
        self.username = StringVar()
        self.lastname = StringVar()
        self.phone = StringVar()

        Label(self.screen, text = "Nombre").pack()
        self.username_entry = Entry(self.screen, textvariable = self.username)
        self.username_entry.pack()

        Label(self.screen, text = "Celular ").pack()
        self.phone_entry = Entry(self.screen, textvariable = self.phone)
        self.phone_entry.pack()

        Label(self.screen, text = "").pack()
        Button(self.screen, text = "Ingresar", width = 10, height = 1, command = self.register_user).pack()
        
        self.screen.mainloop()