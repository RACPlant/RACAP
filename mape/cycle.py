import time
from mape.analyzer import Analyzer
from mape.planner import Planner
from controller import get_logger


class Cycle:
    def __init__(self, protocol, arduino_id,
                 analyzer=Analyzer(), planner=Planner()):
        self._arduino_id = arduino_id
        self._protocol = protocol
        self._analyzer = analyzer
        self._planner = planner

        self._logger = get_logger(self.__class__.__name__)

    def _needs_water(self):
        who_needs = self._analyzer.who_needs_water(self._arduino_id)
        self._logger.info("who_needs_water return: {}".format(who_needs))
        return who_needs

    def _how_much_water(self, who_needs):
        how_much = self._planner.how_much_water(self._arduino_id, who_needs)
        self._logger.info("how_much_water return: {}".format(how_much))
        return how_much

    def _water_plant(self, plant):
        self._protocol.water_in(plant["Pump"], plant["Water"])
        self._logger.info("Water in pump: {}, time: {}".format(
            plant["Pump"], plant["Water"]))
        time.sleep(5)

    def start(self):
        needs_water = self._needs_water()
        if needs_water:
            how_much = self._how_much_water(needs_water)
            for plant in how_much:
                self._water_plant(plant)
