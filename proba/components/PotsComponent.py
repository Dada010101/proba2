import tkinter as tk
from tkinter import ttk, StringVar
from datasources.dto.Pots import Pots
from datasources.tk.TkPotsSimulatedValues import TkPotsSimulatedValues
from PIL import Image, ImageTk
from services.PotsService import PotsService


class PotsComponent(ttk.LabelFrame):

    def __init__(self, parent, row, column, service: PotsService):
        super().__init__(master=parent)
        self.config(text="Posude")
        self.grid(row=row, column=column, padx=5, pady=5)
        self.welcomeWindow = parent
        self.service = service
        self.tkPots = TkPotsSimulatedValues()
        self.potsDto = Pots()
        self._loadImages()
        self.setView()

    def setView(self):

        self.pots = ttk.Frame(self)
        self.pots.grid(row=0, column=0)

        self.lbPots = tk.Listbox(self.pots)
        self.lbPots.grid(row=0, column=0, pady=5, padx=5, rowspan=5)
        self.lbPots.bind("<Double-1>", self.selectPotFromList)

        self.fetchAndSetPotsList()

        lblname = ttk.Label(self.pots, text="Name:")
        lblname.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        name = ttk.Entry(self.pots, textvariable=self.tkPots.name)
        name.grid(row=0, column=2, padx=5, pady=5, sticky=tk.EW)

        lblPlantName = ttk.Label(self.pots, text="Plant name:")
        lblPlantName.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

        plantName = ttk.Entry(self.pots, textvariable=self.tkPots.plantName)
        plantName.grid(row=1, column=2, padx=5, pady=5, sticky=tk.EW)

        lblTemperature = ttk.Label(self.pots, text="Temperature:")
        lblTemperature.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        temperature = ttk.Entry(self.pots, textvariable=self.tkPots.temperature)
        temperature.grid(row=2, column=2, padx=5, pady=5)

        lblHunmidity = ttk.Label(self.pots, text="Humidity:")
        lblHunmidity.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        humidity = ttk.Entry(self.pots, textvariable=self.tkPots.humidity)
        humidity.grid(row=3, column=2, pady=5, padx=5)

        lblSimulate = ttk.Label(self.pots, text="\nSimulate values\n", font=("Arial", 14))
        lblSimulate.grid(row=5, column=0)

        lblTemperature = ttk.Label(self.pots, text="Temperature: ")
        lblTemperature.grid(row=6, column=0, pady=5, padx=5, sticky=tk.NW)
        scaleTemperature = ttk.Scale(self.pots, from_=-30, to=60, variable=self.tkPots.temperature)
        scaleTemperature.grid(row=6, column=1, pady=5, padx=5, sticky=tk.W)
        lblSimTemp = ttk.Label(self.pots, textvariable=self.tkPots.temperature)
        lblSimTemp.grid(row=6, column=2, padx=5, pady=5)
        # lblTemperatureValue = ttk.Label(self, textvariable=self.rpiValues.temperature)
        # lblTemperatureValue.grid(row=1, column=1, pady=5, padx=5)
        #
        lblHumidity = ttk.Label(self.pots, text="Humidity: ")
        lblHumidity.grid(row=7, column=0, pady=5, padx=5, sticky=tk.NW)



        scaleHumidity = ttk.Scale(self.pots, from_=0, to=100, variable=self.tkPots.humidity)
        scaleHumidity.grid(row=7, column=1, pady=5, padx=5, sticky=tk.W)
        lblSimHumidity = ttk.Label(self.pots, textvariable=self.tkPots.humidity)
        lblSimHumidity.grid(row=7, column=2, padx=5, pady=5)

        btnSave = ttk.Button(self.pots, text="Save simulated values", command=self.saveSimValues)
        btnSave.grid(row=9, column=0, padx=10, pady=10, columnspan=3)

    def saveSimValues(self):

        self.potsDto.createFromTkModel(self.tkPots)
        self.service.updatePot(self.potsDto)
        self.fetchAndSetPotsList()
        # lblHumidityValue = ttk.Label(self, textvariable=self.rpiValues.humidity)
        # lblHumidityValue.grid(row=2, column=1, pady=5, padx=5)

        # surname = ttk.Entry(adminPanel, textvariable=self.tkUser.surname)
        # surname.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW, columnspan=3)
        #
        # pin = ttk.Entry(adminPanel, textvariable=self.tkUser.pin)
        # pin.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW, columnspan=3)
        #
        # isActive = ttk.Checkbutton(adminPanel, text="Active", variable=self.tkUser.active)
        # isActive.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW, columnspan=3)

        # surname = ttk.Entry(adminPanel, textvariable=self.tkUser.surname)
        # surname.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW, columnspan=3)
        #
        # pin = ttk.Entry(adminPanel, textvariable=self.tkUser.pin)
        # pin.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW, columnspan=3)
        #
        # isActive = ttk.Checkbutton(adminPanel, text="Active", variable=self.tkUser.active)
        # isActive.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW, columnspan=3)
        #
        # btnSave = ttk.Button(adminPanel, text="Spremi", command=self.btnSaveClicked)
        # self.setComponent(btnSave, 4, 1)
        #
        # btnCancel = ttk.Button(adminPanel, text="Odustani", command=self.btnCancelClicked)
        # self.setComponent(btnCancel, 4, 2)
        #
        # btnDelete = ttk.Button(adminPanel, text="Obrisi", command=self.btnDeleteClicked)
        # self.setComponent(btnDelete, 4, 3)

        # posuda1 = ttk.Label(self.pots, image=self.tkImgPosuda1)
        # posuda1.grid(row=0, column=0)

    def selectPotFromList(self, event):
        selectedIndex = event.widget.curselection()
        potsDto: Pots = self.potsList[selectedIndex[0]]
        print(potsDto)
        self.tkPots.fillFromDto(potsDto)

    def fetchAndSetPotsList(self):
        self.potsList = self.service.getAllPots()
        simplifiedPotsList = []
        for pot in self.potsList:
            p: Pots = pot
            simplifiedPotsList.append(p.getInfo())

        self.tkPotsList = StringVar(value=simplifiedPotsList)
        self.lbPots.config(listvariable=self.tkPotsList)

    def _loadImages(self):

        imgPosuda1 = Image.open("./images/imagesBiljke/ruzmarin.jpg")

        self.tkImgPosuda1 = ImageTk.PhotoImage(imgPosuda1)
