import pandas as pd

MAX_SLOTS = 10

class Plants:

    def __init__(self, arduino):
        self._df = None
        self._arduino = arduino
        self._by_slot = dict()
        self._water_info = dict()
        for slot in range(MAX_SLOTS):
            self._by_slot[str(slot)] = None


    def get_all_facts(self):
        facts = []
        for slot in self._by_slot.keys():
            facts.append(self._get_facts(slot))
        return "\n".join(facts)

    def _get_facts(self, slot):
        facts = []
        for water_info in self._water_info[slot]:
            tuple_value = ",".join([self._arduino,
                                    slot,
                                    self._water_info[slot]["botanical_name"],
                                    self._water_info[slot]["eto"],
                                    self._water_info[slot]["predicted"],
                                    self._water_info[slot]["water"])
            facts.append("plant({}).".format(tuple_value))
        return "\n".join(facts)

    def __load_by_arduino(self):
        # call jp API or mock
        return {
                '0': {
                    'botanical_name': 'Capsicum frutescens',
                    'name': 'Pimenteira'
                },
                '1': {
                    'botanical_name': 'Nephrolepis Exaltata',
                    'name': 'Samambaia'
                }
            }

    def __load_info_dataset(self):
        df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT-KbxCsv32_6xZfwCi-KQEUeVskm4cAomqczfHPWIYL-3Nj3D9aawaH6yPFohSzvkJaaU9VSjifk1P/pub?gid=590649384&single=true&output=csv")
        cropped_df = df[["Botanical Name", "Eto", "Predicted", "Water"]]
        cropped_df.columns = ["botanical_name", "eto", "predicted", "water"]
        return cropped_df

    def set_info(self):
        if not self._df:
            self._df = self.__load_info_dataset()
        if not any(self._by_slot.values()):
            self._by_slot = self.__load_by_arduino()
            for slot in self._by_slot:
                self._water_info[slot] = self._df[self._df["Botanical Name"]
                                                  == self._by_slot[slot]["botanical_name"]].to_dict('records')
