

class PlantsDTO:

    def __init__(self):
        self.id = None
        self.name = None
        self.photo = None

    def __repr__(self):
        return f"{self.id}, {self.name}"

    def getInfo(self):
        return f"{self.name}"

    def clear(self):
        self.id = None
        self.name.set("")
        self.surname.set("")
        self.pin.set("")
        self.active.set(False)

    @staticmethod
    def createFromResult(result: tuple):
        plantsDto = PlantsDTO()
        plantsDto.id = result[0]
        plantsDto.name = result[1]
        return plantsDto

    @staticmethod
    def createFromTkModel(tkModel):
        plantsDto = PlantsDTO()
        plantsDto.id = tkModel.id
        plantsDto.name = tkModel.name.get()

        return plantsDto
