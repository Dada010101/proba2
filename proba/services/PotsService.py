from utils.DBUtils import DBUtils
from datasources.dto.Pots import Pots


class PotsService:

    TABLE_NAME = "Posude"

    def __init__(self, sqlConnection):
        self.connection = sqlConnection
        self.createTable()
        self._createPots()


    def createTable(self):
        query = f""" CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL,
                plant name VARCHAR(60),
                temperature INTEGER,
                humidity INTEGER
                
                 ); """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def addPot(self, name):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name)
            VALUES ('{name}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def _createPots(self):
        self.addPot("Zelena")
        self.addPot("Bijela")
        self.addPot("Siva")


    def getPotByName(self, name):
        query = f"SELECT * FROM {self.TABLE_NAME} where name='{name}';"
        result = DBUtils.dohvatiPodatke(self.connection, query, one=True)
        if result is not None:
            potsDto: Pots = Pots.createFromResult(result)
            print(potsDto)
            return potsDto
        else:
            return None


    def getAllPots(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        result = DBUtils.dohvatiPodatke(self.connection, query)
        potsList = []
        if result is not None:
            for pot in result:
                potsDto = Pots.createFromResult(pot)
                # if userDto.name == 'admin':
                #     continue
                # else:
                print(potsDto)

                potsList.append(potsDto)
            return potsList
        else:
            return None

    def updatePot(self, dto: Pots):
        query = f"""
               UPDATE {self.TABLE_NAME}
               SET name='{dto.plantName}', plant name='{dto.plantName}', temperature={dto.temperature}', humidity='{dto.humidity}'
               WHERE id={dto.id};
           """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def deletePlant(self, id):
        query = f"DELETE FROM {self.TABLE_NAME} where id={id};"
        DBUtils.izvrsiIZapisi(self.connection, query)
