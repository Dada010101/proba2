from tkinter import DoubleVar, BooleanVar, StringVar, IntVar


class TkPotsSimulatedValues:

    def __init__(self):
        self.id = None
        self.name = StringVar()
        self.plantName = StringVar()
        self.temperature = DoubleVar()
        self.humidity = DoubleVar()
        # self.simulated = BooleanVar()
        # self.simulated.set(False)

    def fillFromDto(self, potsDto):
        self.id = potsDto.id
        self.name.set(potsDto.name)
        self.plantName.set(potsDto.plantName)
        self.temperature.set(potsDto.temperature)
        self.humidity.set(potsDto.humidity)