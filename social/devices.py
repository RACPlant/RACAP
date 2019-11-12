class Arduino:
    def __init__(self, api_endpoint):
        self._api_endpoint = api_endpoint

    @property
    def all(self):
        # mock or call jp api
        return [
            {
                "id": "arduino_1",
                "port": "/dev/ttyACM0",
                "radiation": "r",
                "temperature": "t"
            }
        ]
    
    def _get_radiation_fact(self):
        facts = []
        for arduino in self.all:
            tuple_value = ",".join([str(arduino["id"]),
                                    str(arduino["radiation"])
                                    ])
            facts.append("is_radiation({}).".format(tuple_value))
        return "\n".join(facts)

    def _get_temperature_fact(self):
        facts = []
        for arduino in self.all:
            tuple_value = ",".join([str(arduino["id"]),
                                    str(arduino["temperature"])
                                    ])
            facts.append("is_temperature({}).".format(tuple_value))
        return "\n".join(facts)

    def get_all_facts(self):
        facts = []
        facts.append(self._get_radiation_fact())
        facts.append(self._get_temperature_fact())
        return "\n".join(facts)
