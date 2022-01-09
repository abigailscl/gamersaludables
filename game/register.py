from tkinter import *

class Regitration():

    def __init__(self):
        self.screen = None
        self.screen1 = None
        self.username = ""
        self.password = ""
        self.username_entry = None
        self.password_entry = None
        

    def register_user(self):
        self.username_info = self.username.get()
        self.password_info = self.password.get()

        file = open(self.username_info+".text", "w")
        file.write(self.username_info +"\n")
        file.write(self.password_info)
        file.close()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        Label(self.screen1, text = "Registration success", fg = "green", font = ("calibri", 11)).pack()


    def register(self):
        self.screen1 = Toplevel(self.screen)
        self.screen1.title("Register")
        self.screen1.geometry("300x250") 

        Label(self.screen1, text = "Username * ").pack()
        self.username_entry = Entry(self.screen1, textvariable = self.username)
        self.username_entry.pack()

        Label(self.screen1, text = "Password * ").pack()
        self.password_entry = Entry(self.screen1, textvariable = self.password)
        self.password_entry.pack()

        Label(self.screen1, text = "").pack()
        Button(self.screen1, text = "Register", width = 10, height = 1, command = self.register_user).pack()


    def login(self):
        print("Login session started")


    def main_screen(self):     
        self.screen = Tk()
        self.screen.geometry("300x250")
        self.screen.title("Notes 1.0")
        Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri, 13")).pack()
        Label(text = "").pack()
        Button(text = "Login", height = "2", width = "30", command = self.login).pack()
        Label(text = "").pack()
        Button(text = "Register", height = "2", width = "30", command = self.register).pack()
        self.screen.mainloop()


r = Regitration()
r.main_screen()