from utils.DBUtils import DBUtils
from datasources.dto.Plants import PlantsDTO



class PlantsService:

    TABLE_NAME = "Plants"

    def __init__(self, sqlConnection):
        self.connection = sqlConnection
        self.createTable()
        self._createPlants()


    def createTable(self):
        query = f""" CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL
                 ); """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def addPlant(self, name):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name)
            VALUES ('{name}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def _createPlants(self):
        self.addPlant("Origano")
        self.addPlant("Bosiljak")
        self.addPlant("Lovor")
        self.addPlant("Ruzmarin")
        self.addPlant("Kopar")
        self.addPlant("Paprika")
        self.addPlant("Rajcica")
        self.addPlant("Tikvica")
        self.addPlant("Feferon")
        self.addPlant("Maslina")


    def getPlantByName(self, name):
        query = f"SELECT * FROM {self.TABLE_NAME} where name='{name}';"
        result = DBUtils.dohvatiPodatke(self.connection, query, one=True)
        if result is not None:
            plantDto: PlantsDTO = PlantsDTO.createFromResult(result)
            print(plantDto)
            return plantDto
        else:
            return None


    def getAllPlants(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        result = DBUtils.dohvatiPodatke(self.connection, query)
        plantList = []
        if result is not None:
            for plant in result:
                plantDto = PlantsDTO.createFromResult(plant)
                # if userDto.name == 'admin':
                #     continue
                # else:
                print(plantDto)

                plantList.append(plantDto)
            return plantList
        else:
            return None

    def updatePlant(self, dto: PlantsDTO):
        query = f"""
               UPDATE {self.TABLE_NAME}
               SET name='{dto.name}'
               WHERE id={dto.id};
           """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def deletePlant(self, id):
        query = f"DELETE FROM {self.TABLE_NAME} where id={id};"
        DBUtils.izvrsiIZapisi(self.connection, query)

