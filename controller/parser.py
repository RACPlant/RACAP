

class Parser:
    def __init__(self):
        self._data = None

    def __call__(self, data):
        self._data = data
        return self

    def metric(self):
        return (
            "metric",
            {

            }
        )

    def water(self):
        return (
            "water",
            {

            }
        )
