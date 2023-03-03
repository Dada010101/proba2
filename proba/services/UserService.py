from utils.DBUtils import DBUtils
from datasources.dto.Users import UsersDTO
from datasources.tk import TkUsers


class UserService:

    TABLE_NAME = "Users"

    def __init__(self, sqlConnection):
        self.connection = sqlConnection
        self.createTable()
        self._createUsers()


    def createTable(self):
        query = f""" CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL,
                surname VARCHAR(30) NOT NULL,
                username VARCHAR(30) NOT NULL,
                password VARCHAR(30) NOT NULL
                 ); """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def addUser(self, name, surname, username, password):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name, surname, username, password)
            VALUES ('{name}', '{surname}', '{username}', {password});
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def _createUsers(self):

        self.addUser("Daniela", "Perin", "Dada", "1111")
        self.addUser("Ana", "Anic", "ani", "2222")

    def getUserByUsernameAndPass(self, username, password):
        query = f"SELECT * FROM {self.TABLE_NAME} where username='{username}' AND password='{password}';"
        result = DBUtils.dohvatiPodatke(self.connection, query, one=True)
        if result is not None:
            userDto: UsersDTO = UsersDTO.createFromResult(result)
            print(userDto)
            return userDto
        else:
            return None


    def getAllUsers(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        result = DBUtils.dohvatiPodatke(self.connection, query)
        userList = []
        if result is not None:
            for user in result:
                userDto = UsersDTO.createFromResult(user)
                # if userDto.name == 'admin':
                #     continue
                # else:
                print(userDto)

                userList.append(userDto)
            return userList
        else:
            return None

    def updateUser(self, dto: UsersDTO):
        query = f"""
               UPDATE {self.TABLE_NAME}
               SET name='{dto.name}', surname='{dto.surname}', username='{dto.username}', password={dto.password}
               WHERE id={dto.id};
           """
        DBUtils.izvrsiIZapisi(self.connection, query)




