import pandas as pd

class Plants:

    @property
    def pumps(self):
        return self._by_pump

    def __init__(self, pumps=["1", "2", "3", "4"]):
        self._df = None
        self._by_pump = dict()
        self._water_info = dict()
        for pump in pumps:
            self._by_pump[pump] = None
            self._water_info[pump] = None

    def __load_by_pump(self):
        # call jp API or mock self._plants
        return {
            "1": "Chinese abelia",
            "2": "yellow sand verbena",
            "3": "Bailey acacia",
            "4": "eumong/shoestring acacia"
        }

    def __load_info_dataset(self):
        return pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT-KbxCsv32_6xZfwCi-KQEUeVskm4cAomqczfHPWIYL-3Nj3D9aawaH6yPFohSzvkJaaU9VSjifk1P/pub?gid=590649384&single=true&output=csv")
    
    def set_info(self):
        if not self._df:
            self._df = self.__load_info_dataset()
        if not any(self._by_pump.values()):
            self._by_pump = self.__load_by_pump()
        if not any(self._water_info.values()):
            for pump in self._water_info:
                self._water_info[pump] = self._df[self._df["Common Name"] == self._by_pump[pump]]