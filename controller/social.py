class Social:
    def __init__(self, api_endpoint):
        self._api_endpoint = api_endpoint

    @property
    def arduinos(self):
        # mock or call jp api
        return ["0"]
