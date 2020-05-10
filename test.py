import json

#a = { "denotations": [{"id": "A2", "span": {"begin": 76, "end": 84}, "obj": "Virus_other:694009 "}, {"id": "A3", "span": {"begin": 255, "end": 296}, "obj": "Virus_SARS-CoV-2:2697049"}, {"id": "A1", "span": {"begin": 19, "end": 36}, "obj": "Virus_SARS-CoV-2:2697049"}, {"id": "A6", "span": {"begin": 38, "end": 47}, "obj": "Virus_SARS-CoV-2:2697049"}]}

a = ["Virus_SARS-CoV-2", "Disease_COVID-19", "Symptom_COVID-19"]
b = ["real_ent_ret","real_ent","ent_ret"]

entities = dict(zip(b, [0 for i in range(len(a))]))
scoredict = dict(zip(a, [entities for i in range(len(a))]))
print(scoredict)

print(list(scoredict.keys()))