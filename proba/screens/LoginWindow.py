from tkinter import Frame
import tkinter as tk
from tkinter import ttk
from time import sleep as delay
from tkinter import *
import sv_ttk
from PIL import Image, ImageTk
from services.UserService import UserService
from services.PlantsService import PlantsService
from services.PotsService import PotsService, Pots
from components.PlantsComponent import PlantsComponent, PlantsDTO
from datasources.tk.TkUsers import TkUsers
from datasources.dto.Users import UsersDTO
#from images.ImagesDTO import ImagesDTO
from screens.WelcomeScreen import WelcomeScreen



class LoginWindow(Frame):

    def __init__(self, mainWindow, service: UserService, plantS: PlantsService, potS: PotsService):
        super().__init__(master=mainWindow)
        self.grid()
        sv_ttk.use_dark_theme()
        self.service = service
        self.plantS = plantS
        self.potS = potS
        self._loadImages()
        self.user = UsersDTO()
        self.toggleVisibility = False
        self.tkUser = TkUsers()
        #self.LoginScreen()
        self.pyFloraScreen()
        #self.setView()


    def LoginScreen(self):

        self.canvas = Canvas(self, width=1100, height=600)
        #self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.grid(row=1, column=1)

        self.canvas.bind("<Configure>", self.resize_image)

        self.username = tk.StringVar()
        self.username = Entry(self.canvas, font=("Vivaldi", 33), width=14, bd=0, fg="white", background="darkgreen")
        self.windowUsername = self.canvas.create_window(88, 290, anchor="nw", window=self.username)

        self.password = tk.StringVar()
        self.password = Entry(self.canvas, font=("Vivaldi", 33), width=14, bd=0, fg="green", show="*")
        self.windowPassword = self.canvas.create_window( 88, 400, anchor="nw", window=self.password)

        login_btn = Button(self.canvas, text="Login", font=("Vivaldi", 18), width=8, fg="white", bg="darkgreen", command=self.login)
        login_btn_window = self.canvas.create_window(88, 520, anchor="nw", window=login_btn)

        imgShow = Image.open(r"C:\Users\Fujitsu\PycharmProjects\pythonProject2\.idea\PyFlora\images\show.png")
        imgHide = Image.open(r"C:\Users\Fujitsu\PycharmProjects\pythonProject2\.idea\PyFlora\images\hide.png")

        self.tkImgShow = ImageTk.PhotoImage(imgShow)
        self.tkImgHide = ImageTk.PhotoImage(imgHide)
        self.btnShowPhoto = Button(self.canvas, image=self.tkImgHide, background="green", command=self.changeVisibility)
        self.windowShowPhoto = self.canvas.create_window(340, 417, window=self.btnShowPhoto)

    def changeVisibility(self):
        if not self.toggleVisibility:
            self.password.config(show="")
            self.btnShowPhoto.config(image=self.tkImgShow)
            self.toggleVisibility = True
        else:
            self.password.config(show="*")
            self.btnShowPhoto.config(image=self.tkImgHide)
            self.toggleVisibility = False


    def resize_image(self, e):
        global image, resized, image2
        image = Image.open(r"C:\Users\Fujitsu\PycharmProjects\pythonProject2\.idea\PyFlora\images\hands-holding-plant2.jpg")
        resized = image.resize((e.width, e.height), Image.Resampling.LANCZOS)
        image2 = ImageTk.PhotoImage(resized)

        self.canvas.create_image(0, 0, image=image2, anchor='nw')
        self.canvas.create_text(300, 150, text="PyFlora", font=("Vivaldi", 100, "bold"), fill="green", anchor="center", activefill="greenyellow")
        #self.canvas.create_text(300, 50, text="Welcome", font=("Vivaldi", 66, "italic"), fill="brown")
        self.canvas.create_text(130, 270, text="Username:", font=("Vivaldi", 22, "bold"), fill="darkgreen")
        self.canvas.create_text(130, 380, text="Password:", font=("Vivaldi", 22, "bold"), fill="darkgreen")

    def login(self):
        username = self.username.get()
        password = self.password.get()
        userDto: UsersDTO = self.service.getUserByUsernameAndPass(username, password)
        if userDto is not None:
            self.canvas.grid_remove()
            self.pyFloraScreen()
            self.tkUser.id = userDto.id
            self.tkUser.name.set(userDto.name)
            self.tkUser.surname.set(userDto.surname)
            self.tkUser.username.set(userDto.username)
            print(userDto.username)
            print(self.tkUser.surname.get())
            self.tkUser.password.set(userDto.password)
        else:
            self.canvas.create_text(280, 470, text="Username or password are not match! Please try again!", font=("Vivaldi", 22, "bold"), fill="darkgreen")


    def pyFloraScreen(self):

        self.welcomeScreen = WelcomeScreen(self, 0, 0, self.service, self.potS)

    def detailsProfile(self):

        self.top = Toplevel(self.master)
        self.top.geometry("1200x600")

        self.top.title("My profile")

        self.labelPhoto = ttk.Label(self.top, image=None)
        self.labelPhoto.grid(row=1, column=0, pady=5, padx=5, rowspan=5, columnspan=2)

        username = self.username.get()
        if username == "profa":
            self.labelPhoto.config(image=self.tkImgAndreas)
        elif username == "Dada":
            self.labelPhoto.config(image=self.tkImgDaniela)
        elif username == "Ana":
            self.labelPhoto.config(image=self.tkImgAna)
        else:
            print("No profile photo")

        self.lblName = ttk.Label(self.top, text="Name:", font=("Vivaldi", 22), foreground="green")
        self.lblName.grid(row=1, column=3, padx=5, pady=5)

        self.name = tk.StringVar()
        self.name = ttk.Label(self.top, textvariable=self.tkUser.name, state=DISABLED, font=("Vivaldi", 22, "bold"), foreground="brown")
        self.name.grid(row=1, column=4, padx=5, pady=5)

        self.lblSurname = ttk.Label(self.top, text="Surname:", font=("Vivaldi", 22), foreground="green")
        self.lblSurname.grid(row=2, column=3, padx=5, pady=5)

        self.surname = tk.StringVar()
        self.surname = ttk.Label(self.top, textvariable=self.tkUser.surname, state=DISABLED, font=("Vivaldi", 22, "bold"), foreground="brown")
        self.surname.grid(row=2, column=4, padx=5, pady=5)

        self.lblUsername = ttk.Label(self.top, text="Username:", font=("Vivaldi", 22), foreground="green")
        self.lblUsername.grid(row=3, column=3, padx=5, pady=5)

        self.username = tk.StringVar()
        self.username = ttk.Label(self.top, textvariable=self.tkUser.username, font=("Vivaldi", 22, "bold"), foreground="brown")
        self.username.grid(row=3, column=4, padx=5, pady=5)

        self.lblPassword = ttk.Label(self.top, text="Password:", font=("Vivaldi", 22), foreground="green")
        self.lblPassword.grid(row=4, column=3, padx=5, pady=5)

        self.password = tk.StringVar()
        self.password = ttk.Label(self.top, textvariable=self.tkUser.password, font=("Vivaldi", 22, "bold"), foreground="brown")
        self.password.grid(row=4, column=4, padx=5, pady=5)

        btnChangePass = Button(self.top, text="Edit password", background="green", command=self.editPassWindow)
        btnChangePass.grid(row=4, column=5)

        btnLogOut = Button(self.top, text="   Log out   ", background="green", command=self.master.destroy)
        btnLogOut.grid(row=11, column=11, sticky=tk.SW) #pomakni malo

        btnBack = Button(self.top, text="   Back   ", background="green", command=self.top.destroy)
        btnBack.grid(row=11, column=12, sticky=tk.SW)  # pomakni malo, vidi da je scalable s screenom, ne samo ovaj nego svi widgeti

    def editPassWindow(self):

        self.top1 = Toplevel(self.master)
        self.top1.geometry("300x200")
        self.top1.title("Change password")
        Label(self.top1, text="New password: ", font=("Vivaldi", 18, "bold"), foreground="green").place(x=20, y=20)
        Entry(self.top1, textvariable=self.tkUser.password, font=('Vivaldi', 20)).place(x=20, y=60)
        Button(self.top1, text="Save and exit", font=("Courier", 10), foreground="white", background="green", command=self.editPass).place(x=20, y=100)
        BtnCancel = Button(self.top1, text="Cancel", font=("Courier", 10), background="green", foreground="white", command=self.top1.destroy).place(x=200, y=100)



    def editPass(self):

        userDto = UsersDTO.createFromTkModel(self.tkUser)
        self.service.updateUser(userDto)
        self.fetchAndSetUserList()
        self.top1.destroy()

    def _loadImages(self):
        imgAndreas = Image.open("./images/profileImg/andreas.jpg")
        imgDaniela = Image.open("./images/profileImg/Daniela.jpg")
        imgAna = Image.open("./images/profileImg/Ani2.jpg")

        self.tkImgAndreas = ImageTk.PhotoImage(imgAndreas)
        self.tkImgDaniela = ImageTk.PhotoImage(imgDaniela)
        self.tkImgAna = ImageTk.PhotoImage(imgAna)





    # def resize_image2(self, e):
    #     global image3, resized, image4
    #     image3 = Image.open(r"C:\Users\Fujitsu\PycharmProjects\pythonProject2\.idea\PyFlora\images\slika2.jpg")
    #     resized = image3.resize((e.width, e.height), Image.Resampling.LANCZOS)
    #     image4 = ImageTk.PhotoImage(resized)
    #
    #     self.canvas.create_image(0, 0, image=image4, anchor='nw')
    #     self.canvas.create_text(950, 20, text=f"Dobrodosli, {self.user.name}", fill="white", font=("Vivaldi", 20, "bold"))


    def fetchAndSetUserList(self):
        self.userList = self.service.getAllUsers()
        simplifiedUserList = []
        for user in self.userList:
            u: UsersDTO = user
            simplifiedUserList.append(u.getInfo())

        self.tkUserList = StringVar(value=simplifiedUserList)


