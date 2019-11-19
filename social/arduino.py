import requests


class Slots:
    def __init__(self, api_endpoint, arduino_id):
        self._api_endpoint = api_endpoint.format(arduino_id)
        self.arduino_id = arduino_id

    @property
    def all(self):
        return requests.get(self._api_endpoint).json()
        # {
        #     '0': {
        #         'botanical_name': 'Abelia chinensis',
        #         'name': 'Pimenteira',
        #         'pump': 'p1',
        #         'humidity': 'h1'
        #     },
        #     '1': {
        #         'botanical_name': 'Abelia floribunda',
        #         'name': 'Samambaia',
        #         'pump': 'p2',
        #         'humidity': 'h2'
        #     }
        # }


class Devices:
    def __init__(self, api_endpoint):
        self._api_endpoint = api_endpoint

    @property
    def all(self):
        return requests.get(self._api_endpoint).json()
        # [
        #     {
        #         "id": "arduino_1",
        #         "port": "/dev/ttyACM0",
        #         "radiation": "r",
        #         "temperature": "t"
        #     }
        # ]

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
