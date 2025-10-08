from dotenv import dotenv_values

# Класс для настроек программы
class Settings:

    def __init__(self):
        self.__set_values()


    def __set_values(self):

        values = dotenv_values(".env")

        self.__language = values['LANGUAGE']
        self.__units = values['UNITS']

    @property
    def language(self):
        return self.__language

    @property
    def units(self):
        return self.__units