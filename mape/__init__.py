from os import path
from database.knowledge_base import KnowledgeBase

class MAPE:
    _rules_files = []

    def __init__(self):
        rules_files = self._get_rules()
        self._kb = KnowledgeBase(rules_files)
    
    def _get_rules(self):
        base_folder = "./rules/"
        rules_files = []

        for rule_file in self._rules_files:
            rules_files.append(path.join(base_folder, rule_file))
        return rules_files