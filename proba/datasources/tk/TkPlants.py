from tkinter import StringVar, BooleanVar


class TkPlants:

    def __init__(self):
        self.id = None
        self.name = StringVar()



    def loadImage(self, url):
        self.image = Image.open(url)
        self.tkImageProfile = ImageTk.PhotoImage(self.image)



    def fillFromDto(self, userDto):
        self.id = plantsDto.id
        self.name.set(plantsDto.name)
