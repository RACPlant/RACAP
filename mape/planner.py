from mape import MAPE

class Planner(MAPE):
    _rules_files = ["planner.pl"]

    def how_much_water(self, who_needs):
        how_much = []
        for plant in who_needs:
            how_much = self._kb.query("{},{},{}".format(**plant))
        return how_much