from mape import MAPE


class Planner(MAPE):
    _rules_files = ["planner.pl"]

    def how_much_water(self, arduino_id, who_needs):
        how_much = []
        for plant in who_needs:
            plant["arduino_id"] = arduino_id
            how_much = self._kb.query("{},{},{}".format(**plant))
        return how_much
