

class Pots:

    def __init__(self):
        self.id = None
        self.name = None
        self.plantName = None
        self.temperature = None
        self.humidity = None

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.plantName}, {self.temperature}, {self.humidity}"

    def getInfo(self):
        return f"{self.name}"



    @staticmethod
    def createFromResult(result: tuple):
        potsDto = Pots()
        potsDto.id = result[0]
        potsDto.name = result[1]
        potsDto.plantName = result[2]
        potsDto.temperature = result[3]
        potsDto.humidity = result[4]
        return potsDto

    @staticmethod
    def createFromTkModel(tkModel):
        potsDto = Pots()
        potsDto.id = tkModel.id
        potsDto.name = tkModel.name.get()
        potsDto.plantName = tkModel.plantName.get()
        potsDto.temperature = tkModel.temperature.get()
        potsDto.humidity = tkModel.humidity.get()

        return potsDto


