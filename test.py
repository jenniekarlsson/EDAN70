import json

#a = { "denotations": [{"id": "A2", "span": {"begin": 76, "end": 84}, "obj": "Virus_other:694009 "}, {"id": "A3", "span": {"begin": 255, "end": 296}, "obj": "Virus_SARS-CoV-2:2697049"}, {"id": "A1", "span": {"begin": 19, "end": 36}, "obj": "Virus_SARS-CoV-2:2697049"}, {"id": "A6", "span": {"begin": 38, "end": 47}, "obj": "Virus_SARS-CoV-2:2697049"}]}

a = {'a':{'a':1}, 'b':{'a':5}}

def plusa():
    a['a']['a'] += 1

def plusb():
    a['b']['a'] += 9

plusa()   
plusa()
plusb()
print(a)
