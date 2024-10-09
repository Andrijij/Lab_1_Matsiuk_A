class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_facts(self):
        return self.facts

    def get_rules(self):
        return self.rules

    def __str__(self):
        return f"Facts: {self.facts}\nRules: {self.rules}"
