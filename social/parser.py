from controller import get_logger


START = "startMessage"


class Parser:

    logger = get_logger("Parser")

    def __init__(self):
        self._data = None

    def parse(self, data):
        self.logger.debug("Parsing data: \"%s\"", data)
        if data.startswith(START):
            self._data = data
            return self._parse()
        else:
            raise IOError("Data not recognized: {}".format(data))

    def _parse(self):
        lines = self._data.split(";")[1:-1]
        list_of_metrics = [
            dict(
                zip(
                    ["arduino", "sensor", "value"], line.split(",")
                )
            )
            for line in lines
        ]
        return list_of_metrics
