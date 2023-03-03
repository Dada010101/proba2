from utils.JSONSerializator import JSONSerializator
import json

class ConfigDto(JSONSerializator):

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.publish = False
        self.type = None


    @staticmethod
    def createFromEntity(model: tuple):
        config = ConfigDto()
        config.type = model[1]
        config.temperature = model[2]
        config.humidity = model[3]
        config.pressure = model[4]
        config.publish = model[5]
        return config

    def getJson(self):
        model = {
            'type': self.type,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'publish': self.publish
        }
        return json.dumps(model)

    def __repr__(self):
        return str(self.__dict__)

