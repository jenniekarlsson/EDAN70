import json

a = { "denotations": [{"id": "A2", "span": {"begin": 76, "end": 84}, "obj": "Virus_other:694009 "}, {"id": "A3", "span": {"begin": 255, "end": 296}, "obj": "Virus_SARS-CoV-2:2697049"}, {"id": "A1", "span": {"begin": 19, "end": 36}, "obj": "Virus_SARS-CoV-2:2697049"}, {"id": "A6", "span": {"begin": 38, "end": 47}, "obj": "Virus_SARS-CoV-2:2697049"}]}

out = []
with open('updated_gold_standard.json') as f:
    for jsonObj in f:
        one_dict = json.loads(jsonObj)
        out.append(one_dict)
print(out)


x = [{'name': "Alice", 'height': 24, 'age': 33},
{'name': "Oscar", 'height': 55, 'age': 12},
{'name': "Bob", 'height': 90, 'age': 22}
]

a = zip([1,2,3], [4,5,6])
for b in a:
    print(b)