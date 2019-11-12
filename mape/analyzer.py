from mape import MAPE


class Analyzer(MAPE):
    _rules_files = ["analyser.pl"]

    def who_needs_water(self):
        return self._kb.query("")
