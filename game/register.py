from tkinter import *
from user import User


class Regitration():

    def __init__(self, game):
        self.screen = None
        self.connection = game

        self.username_info = None
        self.password_info = None

        self.username_entry = None
        self.password_entry = None

        self.username = None
        self.password = None

        

    def register_user(self):
        self.username_info = self.username.get()
        self.password_info = self.password.get()
        if self.connection.user.verificar_usuario(self.username_info) and self.connection.user.ver_phone(self.password_info):
            self.connection.user.name = self.username_info
            self.connection.user.lastname = "lastnameprotected"
            self.connection.user.phone =  self.password_info
            print(self.connection.user.phone )
            self.connection.user.points = self.connection.user.buscar(self.username_info)
            
            Label(self.screen, text = "Ingreso exitoso", fg = "green", font = ("calibri", 11)).pack()
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.screen.destroy()
            
        elif self.connection.user.verificar_usuario(self.username_info) == False and self.connection.user.ver_phone(self.password_info):
            self.connection.user.id = self.connection.user.insertar(self.username_info,"-", self.password_info, 0)
            self.connection.user.name = self.username_info
            self.connection.user.lastname = ""
            self.connection.user.phone = self.password_info
            self.connection.user.points = 80
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            Label(self.screen, text = "Registro exitoso, cierre esta ventana", fg = "green", font = ("calibri", 11)).pack()
        else:
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            Label(self.screen, text = "Número de celular iválido", fg = "red", font = ("calibri", 11)).pack()
        

    def on_closing(self):
            self.screen.destroy()

    def main_screen(self):     
        self.screen = Tk()
        self.screen.geometry("300x200")
        self.screen.title("Resgistro")
        self.username = StringVar()
        self.lastname = StringVar()
        self.password = StringVar()

        Label(self.screen, text = "Nombre").pack()
        self.username_entry = Entry(self.screen, textvariable = self.username)
        self.username_entry.pack()

        Label(self.screen, text = "Celular ").pack()
        self.password_entry = Entry(self.screen, textvariable = self.password)
        self.password_entry.pack()

        Label(self.screen, text = "").pack()
        Button(self.screen, text = "Ingresar", width = 10, height = 1, command = self.register_user).pack()
        

        self.screen.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.screen.mainloop()