from knowledge_module import KnowledgeBase

class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def infer(self, query):
        # Простий механізм логічного виведення: шукаємо правило, яке може бути застосоване
        for rule in self.knowledge_base.get_rules():
            if query in rule:
                return f"Rule matched: {rule}"
        return "No applicable rule found"

# Приклад використання
kb = KnowledgeBase()
kb.add_fact("Resistor(r)")
kb.add_fact("Current(i)")
kb.add_rule("Voltage(v) = Current(i) * Resistor(r)")

engine = InferenceEngine(kb)
result = engine.infer("Voltage(v)")
print(result)
