from tkinter import ttk, IntVar, BooleanVar, DoubleVar
import tkinter as tk
from PIL import Image, ImageTk
from datasources.tk.TkPlants import TkPlants
from datasources.dto.Plants import PlantsDTO
from services.PlantsService import PlantsService



class PlantsComponent(ttk.LabelFrame):

    def __init__(self, parent, row, column):
        super().__init__(master=parent)#, text="Plants")
        self.grid(row=row, column=column, padx=5, pady=5)
        self.welcomeWindow = parent
        self.service = PlantsService
        self.tkPlants = TkPlants()
        self.plantDTO = PlantsDTO()
        self._loadImages()
        self.setView()

    def setView(self):

        self.lblPlants = ttk.Frame(self)
        self.lblPlants.grid(row=0, column=0)

        # lblBosiljak = tk.Label(self.lblPlants, image=self.tkImgBosiljka)
        # lblBosiljak.grid(row=0, column=0, sticky=tk.E)
        # #
        # infoBosiljak = tk.Label(self.lblPlants, text="Bosiljak")
        # infoBosiljak.grid(row=0, column=1)

        infoBosiljak = tk.Button(self.lblPlants, textvariable=self.tkPlants.name, font=("Arial", 14), command=self.moreInfoPlant)
        infoBosiljak.grid(row=0, column=0, pady=5, padx=5)

        # proba = ttk.Label(self.lblPlants, textvariable=self.plantDTO.name)
        # proba.grid(row=0, column=0)
        #
        infoBosiljak["compound"] = tk.LEFT
        infoBosiljak["image"] = self.tkImgBosiljka

        infoFeferon = tk.Button(self.lblPlants, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoFeferon.grid(row=0, column=1, pady=5, padx=5)

        infoFeferon["compound"] = tk.LEFT
        infoFeferon["image"] = self.tkImgFeferon

        infoKopar = tk.Button(self.lblPlants, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoKopar.grid(row=0, column=2, pady=5, padx=5)

        infoKopar["compound"] = tk.LEFT
        infoKopar["image"] = self.tkImgKopar

        infoLovor = tk.Button(self.lblPlants, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoLovor.grid(row=1, column=0, pady=5, padx=5)

        infoLovor["compound"] = tk.LEFT
        infoLovor["image"] = self.tkImgLovor

        infoMaslina = tk.Button(self.lblPlants, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoMaslina.grid(row=1, column=1, pady=5, padx=5)

        infoMaslina["compound"] = tk.LEFT
        infoMaslina["image"] = self.tkImgMaslina

        infoOrigano = tk.Button(self.lblPlants, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoOrigano.grid(row=1, column=2, pady=5, padx=5)

        infoOrigano["compound"] = tk.LEFT
        infoOrigano["image"] = self.tkImgOrigano

        btnNext = ttk.Button(self.lblPlants, text="Next page", command=self.setView2)
        btnNext.grid(row=2, column=2, columnspan=2)

    def setView2(self):

        self.lblPlants.grid_remove()
        self.lblPlants2 = ttk.Frame(self)
        self.lblPlants2.grid(row=0, column=0)

        infoPaprika = tk.Label(self.lblPlants2, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoPaprika.grid(row=0, column=0, pady=5, padx=5)

        infoPaprika["compound"] = tk.LEFT
        infoPaprika["image"] = self.tkImgPaprika

        infoPoma = tk.Label(self.lblPlants2, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoPoma.grid(row=0, column=1, pady=5, padx=5)

        infoPoma["compound"] = tk.LEFT
        infoPoma["image"] = self.tkImgPoma

        infoRuzmarin = tk.Label(self.lblPlants2, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoRuzmarin.grid(row=0, column=2, pady=5, padx=5)

        infoRuzmarin["compound"] = tk.LEFT
        infoRuzmarin["image"] = self.tkImgRuzmarin

        infoTikvica = tk.Label(self.lblPlants2, text="Bosiljak bchabscks\n jdasjdas jsahbdjasdsa", font=("Arial", 14))
        infoTikvica.grid(row=1, column=0, pady=5, padx=5)

        infoTikvica["compound"] = tk.LEFT
        infoTikvica["image"] = self.tkImgTikvica

        btnBackToPreviousPage = ttk.Button(self.lblPlants2, text="Back to previous page", command=self.backToPrevious)
        btnBackToPreviousPage.grid(row=2, column=0, columnspan=2, sticky=tk.W)

        btnAddNewPlant = tk.Button(self.lblPlants2, text=" + \nAdd \nnew \nplant", foreground="black", font=("Arial", 14), height=10, width=18, background="white", command=self.addNewPlant)
        btnAddNewPlant.grid(row=1, column=1, sticky=tk.W)


    def backToPrevious(self):

        self.lblPlants2.grid_remove()
        self.setView()

    def addNewPlant(self):

        self.addPlant = tk.Toplevel(self)
        self.addPlant.geometry("600x600")

        self.addPlant.title("Add plant")

        #prvo kreiraj kad stisnes gumb da ti se otvori prozor s detaljima biljke pa onda logiku
        self.addPlant = ttk.Label(self.addPlant, text="Unesite ime biljke: ")
        self.addPlant.grid(row=0, column=0)

        addName = ttk.Entry(self.addPlant)
        addName.grid(row=0, column=1)
        self.service.addPlant(addName.get())

    def moreInfoPlant(self):

        self.top = tk.Toplevel(self.master)
        self.top.geometry("600x400")

        self.top.title("Details")

        self.imagePlant = tk.Button(self.top)
        self.imagePlant.grid(row=0, column=0, pady=5, padx=5)

        self.imagePlant["image"] = self.tkImgBosiljka
        #
        self.lblNamePlant = tk.Label(self.top, text="Name", font=("Vivaldi", 22), foreground="green")
        self.lblNamePlant.grid(row=0, column=1, padx=5, pady=5)

        self.lblEntryName = tk.Entry(self.top, textvariable=self.service.getPlantByName(self,"Bosiljak"))
        self.lblEntryName.grid(row=0, column=2)


        btnAzuriraj = tk.Button(self.top, text="Uredi", command=self.editInfo)
        btnAzuriraj.grid(row=2, column=2)

        btnIzbrisi = tk.Button(self.top, text="Izbrisi", command=self.deletePlant)
        btnIzbrisi.grid(row=2, column=1)

    def editInfo(self):
        # plantDTO = self.service.createFromTkModel(self.tkPlants)
        # self.service.updatePlant(plantDTO)
        # self.fetchAndSetPlantList()
        self.lblNamePlant.config(state=tk.NORMAL)
        self.lblNamePlantbase = tk.Label(self.imagePlant,text="fcsddsaxs")
        self.lblNamePlantbase.grid(row=0, column=3, pady=5, padx=5, rowspan=5, columnspan=2)

        # self.lblName = ttk.Label(self.top, text="Name:", font=("Vivaldi", 22), foreground="green")
        # self.lblName.grid(row=1, column=3, padx=5, pady=5)
        #
        # self.name = tk.StringVar()
        # self.name = ttk.Label(self.top, textvariable=self.user.name, state=DISABLED, font=("Vivaldi", 22, "bold"),
        #                       foreground="brown")
        # self.name.grid(row=1, column=4, padx=5, pady=5)
        #
        # self.lblSurname = ttk.Label(self.top, text="Surname:", font=("Vivaldi", 22), foreground="green")
        # self.lblSurname.grid(row=2, column=3, padx=5, pady=5)

    def deletePlant(self):
        self.service.deletePlant(self.tkPlants.id)
        self.plantDTO.clear()
        self.fetchAndSetPlantList()

    def clearTkPlant(self):
        self.tkPlants.clear()



    def fetchAndSetPlantList(self):
        self.plantList = self.service.getAllPlants()
        simplifiedPlanyList = []
        for plant in self.plantList:
            p: PlantsDTO = plant
            simplifiedPlantList.append(p.getInfo())

        self.tkPlantList = StringVar(value=simplifiedPlanyList)




    def _loadImages(self):
        imgBosiljak = Image.open("./images/imagesBiljke/bosiljak.jpg")
        imgFeferon = Image.open("./images/imagesBiljke/feferon.jpg")
        imgKopar = Image.open("./images/imagesBiljke/Kopar.jpg")
        imgLovor = Image.open("./images/imagesBiljke/lovor.jpg")
        imgMaslina = Image.open("./images/imagesBiljke/maslina.jpg")
        imgTikvica = Image.open("./images/imagesBiljke/tikvica.jpg")
        imgOrigano = Image.open("./images/imagesBiljke/origano.jpg")
        imgPaprika = Image.open("./images/imagesBiljke/paprika.jpg")
        imgPoma = Image.open("./images/imagesBiljke/poma.jpg")
        imgRuzmarin = Image.open("./images/imagesBiljke/ruzmarin.jpg")

        self.tkImgBosiljka = ImageTk.PhotoImage(imgBosiljak)
        self.tkImgFeferon = ImageTk.PhotoImage(imgFeferon)
        self.tkImgKopar = ImageTk.PhotoImage(imgKopar)
        self.tkImgLovor = ImageTk.PhotoImage(imgLovor)
        self.tkImgMaslina = ImageTk.PhotoImage(imgMaslina)
        self.tkImgTikvica = ImageTk.PhotoImage(imgTikvica)
        self.tkImgOrigano = ImageTk.PhotoImage(imgOrigano)
        self.tkImgPaprika = ImageTk.PhotoImage(imgPaprika)
        self.tkImgPoma = ImageTk.PhotoImage(imgPoma)
        self.tkImgRuzmarin = ImageTk.PhotoImage(imgRuzmarin)

