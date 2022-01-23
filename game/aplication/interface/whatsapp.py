import pywhatkit
class Whatsapp():
    def __init__(self):
        self.message = ""
        self.number = ""
        self.hour = 0
        self.minutes = 0 
    def send_mesage(self):
        pywhatkit.sendwhatmsg(self.number,self.message, self.hour, self.minutes)


