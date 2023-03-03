from tkinter import ttk, IntVar, BooleanVar, DoubleVar, StringVar
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from datasources.dto.Users import UsersDTO
from components.PlantsComponent import PlantsComponent
from components.PotsComponent import PotsComponent
from services.UserService import UserService
from services.PotsService import PotsService
from datasources.tk.TkUsers import TkUsers



class WelcomeScreen(ttk.LabelFrame):

    def __init__(self, parent, row, column, service: UserService, potsService: PotsService):
        super().__init__(master=parent, text="Welcome to PyFlora")
        self.grid(row=row, column=column, padx=5, pady=5)
        self.loginWindow = parent
        self.service = service
        self.potsService = potsService
        self.user = UsersDTO()
        self.tkUser = TkUsers()
        #self._loadImages()

        self.setView()

    def setView(self):

        self.b = ttk.Frame(self)
        self.b.grid(row=0, column=0)
        btnMyProfile = tk.Button(self.b, text="My profile", background="yellowgreen",anchor=tk.E, command=self.loginWindow.detailsProfile)
        btnMyProfile.grid(row=0, column=9, sticky=tk.E)

        self.name = StringVar()
        self.name = ttk.Label(self.b, textvariable=self.user.getInfo() , font=("Vivaldi", 20, "bold"))
        self.name.grid(row=0, column=8, sticky=tk.E)

        menub = Menubutton(self.b, text='Menu',  background="green", font=("Arial", 12))
        menub.grid(row=0, column=1)
        menub.menu = Menu(menub, tearoff=0)
        menub["menu"] = menub.menu
        pots = IntVar()
        plants = IntVar()
        menub.menu.add_command(label='Plants',  command=self.openPlantComponents)
        menub.menu.add_command(label='Pots', command=self.openPotsComponents)#, c=plants)
        menub.menu.add_command(label="Log out", command=self.master.quit)

        self.canvas = Canvas(self.b, width=1050, height=500)
        self.canvas.grid(row=2, column=8)
        self.canvas.bind("<Configure>", self.resize_image2)

    def resize_image2(self, e):
        global image3, resized, image4
        image3 = Image.open(r"C:\Users\Fujitsu\PycharmProjects\pythonProject2\.idea\PyFlora\images\slika2.jpg")
        resized = image3.resize((e.width, e.height), Image.Resampling.LANCZOS)
        image4 = ImageTk.PhotoImage(resized)

        self.canvas.create_image(0, 0, image=image4, anchor='nw')
        #self.canvas.create_text(950, 20, text=f"Dobrodosli, {self.user.name}", fill="white", font=("Vivaldi", 20, "bold"))

    # def getConfiguration(self):
    #     config = ConfigDto()
    #     config.temperature = int(self.temperature.get())
    #     config.humidity = int(self.humidity.get())
    #     config.pressure = int(self.pressure.get())
    #     config.publish = self.simulate.get()
    #     return config
    #
    #
    # def setConfiguration(self, configDto: ConfigDto):
    #     if configDto is not None:
    #         self.temperature.set(configDto.temperature)
    #         self.humidity.set(configDto.humidity)
    #         self.pressure.set(configDto.pressure)
    #         self.simulate.set(configDto.publish)

    def openPlantComponents(self):

        self.canvas.grid_remove()
        PlantsComponent(self, 1, 0)

    def openPotsComponents(self):

        self.canvas.grid_remove()
        PotsComponent(self, 1, 0, self.potsService)

    # def detailsProfile(self):
    #
    #     self.top = Toplevel(self.master)
    #     self.top.geometry("1200x600")
    #
    #     self.top.title("My profile")
    #
    #     self.lblprofilePicture = ttk.Label(self.top, text="Profile picture", font=("Vivaldi", 22), foreground="green")
    #     self.lblprofilePicture.grid(row=0, column=0, padx=5, pady=5)
    #
    #     self.labelPhoto = tk.Label(self.top, image=self.tkImgBosiljka)
    #     self.labelPhoto.grid(row=1, column=0, pady=5, padx=5, rowspan=5, columnspan=2)
    #
    #     self.lblName = ttk.Label(self.top, text="Name:", font=("Vivaldi", 22), foreground="green")
    #     self.lblName.grid(row=1, column=3, padx=5, pady=5)
    #
    #     self.name = tk.StringVar()
    #     self.name = ttk.Label(self.top, textvariable=self.tkUser.name, state=DISABLED, font=("Vivaldi", 22, "bold"), foreground="brown")
    #     self.name.grid(row=1, column=4, padx=5, pady=5)
    #
    #     self.lblSurname = ttk.Label(self.top, text="Surname:", font=("Vivaldi", 22), foreground="green")
    #     self.lblSurname.grid(row=2, column=3, padx=5, pady=5)
    #
    #     self.surname = tk.StringVar()
    #     self.surname = ttk.Label(self.top, textvariable=self.tkUser.surname, state=DISABLED, font=("Vivaldi", 22, "bold"), foreground="brown")
    #     self.surname.grid(row=2, column=4, padx=5, pady=5)
    #
    #     self.lblUsername = ttk.Label(self.top, text="Username:", font=("Vivaldi", 22), foreground="green")
    #     self.lblUsername.grid(row=3, column=3, padx=5, pady=5)
    #
    #     self.username = tk.StringVar()
    #     self.username = ttk.Label(self.top, textvariable=self.tkUser.username, font=("Vivaldi", 22, "bold"), foreground="brown")
    #     self.username.grid(row=3, column=4, padx=5, pady=5)
    #
    #     self.lblPassword = ttk.Label(self.top, text="Password:", font=("Vivaldi", 22), foreground="green")
    #     self.lblPassword.grid(row=4, column=3, padx=5, pady=5)
    #
    #     self.password = tk.StringVar()
    #     self.password = ttk.Label(self.top, textvariable=self.tkUser.password, font=("Vivaldi", 22, "bold"), foreground="brown")
    #     self.password.grid(row=4, column=4, padx=5, pady=5)
    #
    #     btnChangePass = Button(self.top, text="Edit password", background="green", command=self.editPassWindow)
    #     btnChangePass.grid(row=4, column=5)
    #
    #     btnBack = Button(self.top, text="   Close   ", background="green", command=self.top.destroy)
    #     btnBack.grid(row=11, column=12, sticky=tk.SW)  # pomakni malo, vidi da je scalable s screenom, ne samo ovaj nego svi widgeti
    #
    # def editPassWindow(self):
    #
    #     self.top1 = Toplevel(self)
    #     self.top1.geometry("300x200")
    #     self.top1.title("Change password")
    #     Label(self.top1, text="New password: ", font=("Vivaldi", 18, "bold"), foreground="green").place(x=20, y=20)
    #     Entry(self.top1, textvariable=self.user.password, font=('Vivaldi', 20)).place(x=20, y=60)
    #     Button(self.top1, text="Save and exit", font=("Courier", 10), foreground="white", background="green", command=self.editPass).place(x=20, y=100)
    #     BtnCancel = Button(self.top1, text="Cancel", font=("Courier", 10), background="green", foreground="white", command=self.top1.destroy).place(x=200, y=100)
    #
    #
    #
    # def editPass(self):
    #
    #     userDto = UsersDTO.createFromTkModel(self.tkUser)
    #     self.service.updateUser(userDto)
    #     self.fetchAndSetUserList()
    #     self.top1.destroy()
    #
    # def _loadImages(self):
    #     imgBosiljak = Image.open("./images/imagesBiljke/bosiljak.jpg")
    #     imgFeferon = Image.open("./images/imagesBiljke/feferon.jpg")
    #     imgKopar = Image.open("./images/imagesBiljke/Kopar.jpg")
    #
    #     self.tkImgBosiljka = ImageTk.PhotoImage(imgBosiljak)
    #     self.tkImgFeferon = ImageTk.PhotoImage(imgFeferon)
    #     self.tkImgKopar = ImageTk.PhotoImage(imgKopar)
    #
    # def profilePhoto(self):
    #
    #     if self.tkUser.name.get() == "Andreas":
    #         self.labelPhoto.config(image=self.tkImgBosiljka)
    #     elif self.tkUser.name.get() == "Daniela":
    #         self.labelPhoto.config(image=self.tkImgKopar)
    #     elif self.user.name == "Ani":
    #         self.labelPhoto.config(image=self.tkImgFeferon)



    # def fetchAndSetUserList(self):
    #     self.userList = self.service.getAllUsers()
    #     simplifiedUserList = []
    #     for user in self.userList:
    #         u: UsersDTO = user
    #         simplifiedUserList.append(u.getInfo())
    #
    #     self.tkUserList = StringVar(value=simplifiedUserList)







