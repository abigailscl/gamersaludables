from tkinter import *
from dataBaseConnection import Connection


class Regitration():

    def __init__(self):
        self.screen = None
        self.connection = Connection()

        self.username_info = None
        self.lastname_info = None
        self.password_info = None

        self.username_entry = None
        self.lastname_entry = None
        self.password_entry = None

        self.username = None
        self.lastname = None
        self.password = None

        

    def register_user(self):
        self.username_info = self.username.get()
        self.lastname_info = self.lastname.get()
        self.password_info = self.password.get()

        self.connection.insert_user(self.username_info, self.username_info, self.password_info)

        file = open(self.username_info+".text", "w")
        file.write(self.username_info +"\n")
        file.write(self.password_info)
        file.close()

        self.username_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.password_entry.delete(0, END)

        Label(self.screen, text = "Registro exitoso", fg = "green", font = ("calibri", 11)).pack()

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

        Label(self.screen, text = "Apellido").pack()
        self.lastname_entry = Entry(self.screen, textvariable = self.lastname)
        self.lastname_entry.pack()

        Label(self.screen, text = "Celular ").pack()
        self.password_entry = Entry(self.screen, textvariable = self.password)
        self.password_entry.pack()

        Label(self.screen, text = "").pack()
        Button(self.screen, text = "Registrar", width = 10, height = 1, command = self.register_user).pack()
        

        self.screen.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.screen.mainloop()