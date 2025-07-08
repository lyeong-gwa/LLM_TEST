import os
import json

def load_rule_list(language):
    rules_path = os.path.join(os.path.dirname(__file__), "data", "rules_list.json")
    lang_map = {
        "python": "Python",
        "java": "Java",
        "javascript": "JavaScript"
    }
    with open(rules_path, "r", encoding="utf-8") as f:
        rules = json.load(f)
    result = rules.get(lang_map.get(language, language), [])
    return result