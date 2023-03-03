import tkinter as tk
from tkinter import ttk, LabelFrame
from PIL import ImageTk, Image
from datasources.tk.TkUsers import TkUsers


class ProfileDetail(LabelFrame):

    def __init__(self, parent):
        super().__init__(master=parent, text="RPi")
        self.grid(pady=5, padx=5)

        self._loadImages()

        self.createProfilePanel()

    def createProfilePanel(self):

        self.top = Toplevel(self.master)
        self.top.geometry("1200x600")

        self.top.title("My profile")

        self.lblprofilePicture = ttk.Label(self.top, text="Profile picture", font=("Vivaldi", 22), foreground="green")
        self.lblprofilePicture.grid(row=0, column=0, padx=5, pady=5)

        label = tk.Label(self.top, image=self.tkphotoProfile)
        label.grid(row=1, column=0, pady=5, padx=5, rowspan=5, columnspan=2)

        self.lblName = ttk.Label(self.top, text="Name:", font=("Vivaldi", 22), foreground="green")
        self.lblName.grid(row=1, column=3, padx=5, pady=5)

        self.name = tk.StringVar()
        self.name = ttk.Label(self.top, textvariable=self.tkUser.name, state=DISABLED, font=("Vivaldi", 22, "bold"),
                              foreground="brown")
        self.name.grid(row=1, column=4, padx=5, pady=5)

        self.lblSurname = ttk.Label(self.top, text="Surname:", font=("Vivaldi", 22), foreground="green")
        self.lblSurname.grid(row=2, column=3, padx=5, pady=5)

        self.surname = tk.StringVar()
        self.surname = ttk.Label(self.top, textvariable=self.tkUser.surname, state=DISABLED, font=("Vivaldi", 22, "bold"),
                                 foreground="brown")
        self.surname.grid(row=2, column=4, padx=5, pady=5)

        self.lblUsername = ttk.Label(self.top, text="Username:", font=("Vivaldi", 22), foreground="green")
        self.lblUsername.grid(row=3, column=3, padx=5, pady=5)

        self.username = tk.StringVar()
        self.username = ttk.Label(self.top, textvariable=self.tkUser.username, font=("Vivaldi", 22, "bold"),
                                  foreground="brown")
        self.username.grid(row=3, column=4, padx=5, pady=5)

        self.lblPassword = ttk.Label(self.top, text="Password:", font=("Vivaldi", 22), foreground="green")
        self.lblPassword.grid(row=4, column=3, padx=5, pady=5)

        self.password = tk.StringVar()
        self.password = ttk.Label(self.top, textvariable=self.tkUser.password, font=("Vivaldi", 22, "bold"),
                                  foreground="brown")
        self.password.grid(row=4, column=4, padx=5, pady=5)

        btnChangePass = Button(self.top, text="Edit password", background="green", command=self.editPassWindow)
        btnChangePass.grid(row=4, column=5)

        btnLogOut = Button(self.top, text="   Log out   ", background="green", command=self.master.destroy)
        btnLogOut.grid(row=11, column=11, sticky=tk.SW)  # pomakni malo

        btnBack = Button(self.top, text="   Back   ", background="green", command=self.top.destroy)
        btnBack.grid(row=11, column=12,
                     sticky=tk.SW)  # pomakni malo, vidi da je scalable s screenom, ne samo ovaj nego svi widgeti


    def editPassWindow(self):
        self.top1 = Toplevel(self.master)
        self.top1.geometry("300x200")
        self.top1.title("Change password")
        Label(self.top1, text="New password: ", font=("Vivaldi", 18, "bold"), foreground="green").place(x=20, y=20)
        Entry(self.top1, textvariable=self.tkUser.password, font=('Vivaldi', 20)).place(x=20, y=60)
        Button(self.top1, text="Save and exit", font=("Courier", 10), foreground="white", background="green",
               command=self.editPass).place(x=20, y=100)
        BtnCancel = Button(self.top1, text="Cancel", font=("Courier", 10), background="green", foreground="white",
                           command=self.top1.destroy).place(x=200, y=100)


    def editPass(self):
        userDto = UsersDTO.createFromTkModel(self.tkUser)
        self.service.updateUser(userDto)
        self.fetchAndSetUserList()
        self.top1.destroy()


    # def resize_image2(self, e):
    #     global image3, resized, image4
    #     image3 = Image.open(r"C:\Users\Fujitsu\PycharmProjects\pythonProject2\.idea\PyFlora\images\slika2.jpg")
    #     resized = image3.resize((e.width, e.height), Image.Resampling.LANCZOS)
    #     image4 = ImageTk.PhotoImage(resized)
    #
    #     self.canvas.create_image(0, 0, image=image4, anchor='nw')

    def _loadImages(self):
        imgAndreas = Image.open("./images/profileImg/andreas.jpg")
        imgDaniela = Image.open("./images/profileImg/Daniela.jpg")
        imgAni = Image.open("./images/profileImg/aniiii.jpg")


        self.tkImgAndreas = ImageTk.PhotoImage(imgAndreas)
        self.tkImgDaniela = ImageTk.PhotoImage(imgDaniela)
        self.tkImgAni = ImageTk.PhotoImage(imgAni)



