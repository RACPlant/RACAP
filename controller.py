import pandas as pd

class Controller:

    def __init__(self):
        self._df = None
        self._plants = {
            "1": None,
            "2": None,
            "3": None,
            "4": None
        }
        self._plants_info = {
            "1": None,
            "2": None,
            "3": None,
            "4": None
        }
    def __load_plants(self):
        # call jp API or mock self._plants
        return {
            "1": "Chinese abelia",
            "2": "yellow sand verbena",
            "3": "Bailey acacia",
            "4": "eumong/shoestring acacia"
        }

    def __load_dataset(self):
        return pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT-KbxCsv32_6xZfwCi-KQEUeVskm4cAomqczfHPWIYL-3Nj3D9aawaH6yPFohSzvkJaaU9VSjifk1P/pub?gid=590649384&single=true&output=csv")
    
    def set_plants_info(self):
        if not self._df:
            self._df = self.__load_dataset()
        if not any(self._plants.values()):
            self._plants = self.__load_plants()
        if not any(self._plants_info.values()):
            for pump in self._plants_info:
                self._plants_info[pump] = self._df[self._df["Common Name"] == self._plants[pump]]

controller = Controller()
controller.set_plants_info()