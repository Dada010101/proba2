from tkinter import StringVar, BooleanVar
from PIL import Image, ImageTk

class TkUsers:

    def __init__(self):
        self.id = None
        self.name = StringVar()
        self.surname = StringVar()
        self.username= StringVar()
        self.password = StringVar()
        self.image = None
        self.tkImageProfile: ImageTk = None

    def loadImage(self, url):
        self.image = Image.open(url)
        self.tkImageProfile = ImageTk.PhotoImage(self.image)



    def fillFromDto(self, userDto):
        self.id = userDto.id
        self.name.set(userDto.name)
        self.surname.set(userDto.surname)
        self.username.set(userDto.username)
        self.password.set(userDto.password)