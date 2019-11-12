from mape import MAPE


class Analyzer(MAPE):
    _rules_files = ["analyzer.pl"]

    def who_needs_water(self, arduino_id):
        return self._kb.query("should_water({},Plant,Slot)".format(arduino_id))
