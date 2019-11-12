import pandas as pd

MAX_SLOTS = 10


class Plants:

    def __init__(self, arduino_id):
        self._df = None
        self._arduino = arduino_id
        self._by_slot = dict()
        self._water_info = dict()
        for slot in range(MAX_SLOTS):
            self._by_slot[str(slot)] = None

    def get_all_facts(self):
        facts = self._get_slot_facts()
        facts.append(self._get_eto_facts())
        facts.append(self._get_plant_facts())
        return "\n".join(facts)

    def _get_slot_facts(self):
        facts = []
        for slot in self._by_slot:
            tuple_value = ",".join([self._arduino,
                                    slot,
                                    self._by_slot[slot]["humidity"],
                                    self._by_slot[slot]["pump"]
                                    ])
            facts.append("slot({}).".format(tuple_value))
        return "\n".join(facts)

    def _get_plant_facts(self):
        facts = []
        for slot in self._by_slot.keys():
            for water_info in self._water_info[slot]:
                tuple_value = ",".join([self._arduino,
                                        slot,
                                        water_info["botanical_name"].lower()
                                        ])
                facts.append("plant({}).".format(tuple_value))
        return "\n".join(facts)

    def _get_eto_facts(self):
        facts = []
        for slot in self._by_slot:
            for water_info in self._water_info[slot]:
                tuple_value = ",".join([water_info["botanical_name"].lower(),
                                        str(water_info["eto"]),
                                        str(water_info["predicted"]),
                                        str(water_info["water"])
                                        ])
                facts.append("eto_water({}).".format(tuple_value))
        return "\n".join(facts)

    def __load_by_arduino(self):
        # call jp API or mock
        return {
            '0': {
                'botanical_name': 'Abelia chinensis',
                'name': 'Pimenteira',
                'pump': 'p1',
                'humidity': 'h1'
            },
            '1': {
                'botanical_name': 'Abelia floribunda',
                'name': 'Samambaia',
                'pump': 'p2',
                'humidity': 'h2'
            }
        }

    def __load_info_dataset(self):
        df = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vT-KbxCsv32_6xZfwCi-KQEUeVskm4cAomqczfHPWIYL-3Nj3D9aawaH6yPFohSzvkJaaU9VSjifk1P/pub?gid=590649384&single=true&output=csv")
        cropped_df = df[["Botanical Name", "Eto", "Predicted", "Water"]]
        cropped_df.columns = ["botanical_name", "eto", "predicted", "water"]
        return cropped_df

    def set_info(self):
        if not self._df:
            self._df = self.__load_info_dataset()
        if not any(self._by_slot.values()):
            self._by_slot = self.__load_by_arduino()
            for slot in self._by_slot:
                self._water_info[slot] = self._df[self._df["botanical_name"]
                                                  == self._by_slot[slot]["botanical_name"]].to_dict('records')
