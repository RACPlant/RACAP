START = b"startMessage"

class Parser:
    def __init__(self):
        self._data = None

    def parse(self, data):
        logger.debug("Parsing data: \"%s\"", data)
        if data.startswith(START):
            self._data = data
            return self._parse()
        else:
            raise IOError("Data not recognized")


    def _parse(self):
        lines = data.split("\n")[1:-1]
        list_of_metrics = [
            dict(
                zip(
                    ["arduino", "sensor", "value"], line.split(",")
                    )
            ) 
            for line in lines
        ]
        return list_of_metrics
