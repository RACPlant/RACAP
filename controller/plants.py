from controller.config import PLANTS_ENDPOINT
import pandas as pd

MAX_SLOTS = 10

class Plants:

    def __init__(self, arduino_slots):
        self._df = None
        self._arduino_slots = arduino_slots
        self._by_slot = dict()
        self._water_info = dict()
        for slot in range(MAX_SLOTS):
            self._by_slot[str(slot)] = None

    def get_all_facts(self):
        facts = []
        facts.append(self._get_slot_facts())
        facts.append(self._get_eto_facts())
        facts.append(self._get_plant_facts())
        return "\n".join(facts)

    def _get_slot_facts(self):
        facts = []
        for slot in self._by_slot:
            tuple_value = ",".join([str(self._arduino_slots.arduino_id),
                                    str(slot),
                                    str(self._by_slot[slot]["humidity"]),
                                    str(self._by_slot[slot]["pump"])
                                    ])
            facts.append("slot({}).".format(tuple_value))
        return "\n".join(facts)

    def _get_plant_facts(self):
        facts = []
        for slot, plant in self._by_slot.items():
            tuple_value = ",".join([str(self._arduino_slots.arduino_id),
                                    str(slot),
                                    str(plant["botanical_name"]
                                        ).lower().replace(" ", "_")
                                    ])
            facts.append("plant({}).".format(tuple_value))
        return "\n".join(facts)

    def _get_eto_facts(self):
        facts = []
        for slot in self._by_slot:
            for water_info in self._water_info[slot]:
                tuple_value = ",".join([str(water_info["botanical_name"]).lower().replace(" ", "_"),
                                        str(water_info["eto"]),
                                        str(water_info["predicted"]),
                                        str(water_info["water"])
                                        ])
                facts.append("eto_water({}).".format(tuple_value))
        return "\n".join(facts)

    def __load_info_dataset(self):
        df = pd.read_csv(PLANTS_ENDPOINT)
        cropped_df = df[["Botanical Name", "Eto", "Predicted", "Water"]]
        cropped_df.columns = ["botanical_name", "eto", "predicted", "water"]
        return cropped_df

    def set_info(self):
        if not self._df:
            self._df = self.__load_info_dataset()
        if not any(self._by_slot.values()):
            self._by_slot = self._arduino_slots.all
            for slot in self._by_slot:
                self._water_info[slot] = self._df[self._df["botanical_name"]
                                                  == self._by_slot[slot]["botanical_name"]].to_dict('records')
