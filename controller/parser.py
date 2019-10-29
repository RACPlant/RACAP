

class Parser:
    def __init__(self):
        self._data = None

    def __call__(self, data):
        self._data = data
        return self

    def metrics(self):
        return (
            "metric",
            {
                "data": self._data
            }
        )

    def water(self):
        return (
            "water",
            {

            }
        )
