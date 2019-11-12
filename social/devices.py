class Arduino:
    def __init__(self, api_endpoint):
        self._api_endpoint = api_endpoint

    @property
    def all(self):
        # mock or call jp api
        return [
            {
                "id": "0",
                "port": "/dev/ttyACM0"
            }
        ]
