import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join

def json_to_dict(json_path):
    json = open(json_path,"r")
    for line in json:
        dict.append = json.loads(line)
    return dict


def find_real_entities_retrived(dict_gold, denotation):
    if dict_gold["text"] == denotation["text"]
        real_entities_retrived = 0
        for denot_gold in dict_gold["denotations"]:
            span_gold = denot_gold["span"]
            for denot in denotation["denotations"]
                if span_gold == denot["span"]:
                    real_entities_retrived += 1

    return real_entities_retrived


def find_real_entities(dict_gold):
    real_entities = 0
    for denot_gold in dict_gold["denotations"]:
        real_entities += 1
return real_entities


def find_entities_retrived(denot)
    entities_retrived = 0
    for denot_line in denot["denotations"]:
        entities_retrived += 1
return entities_retrived


def Recall(real_entities, real_entities_retrived):
    recall = real_entities_retrived/real_entities
    return recall


def Precision(real_entities_retrived,entities_retrived):
    precision = real_entities_retrived/entities_retrived
    return precision


def main():
    subset_path_gold = os.path.abspath("gold_papers") + "/"
    gold_papers = [f for f in listdir(subset_path_gold) if isfile(join(subset_path_gold, f))]
    subset_path_denot = os.path.abspath("denot_papers") + "/"
    denot_papers = [f for f in listdir(subset_path_denot) if isfile(join(subset_path_denot, f))]

    evaluation_list = []

    for j in range(len(gold_papers))
        gold_papers_path = subset_path_gold + gold_papers[j]
        dict_gold = json_to_dict(gold_papers_path)
        denot_papers_path = subset_path_denot + denot_papers[j]
        denotation = json_to_dict(denot_papers_path)

        real_entities_retrived = find_real_entities_retrived(dict_gold, denotation)
        real_entities = find_real_entities(dict_gold)
        entities_retrived = find_entities_retrived(denot)

        recall = Recall(real_entities, real_entities_retrived)
        precision = Precision(real_entities_retrived,entities_retrived)

        evaluation_list.append = {"Article: denot_papers_path,"recall": recall, "precision": precision}
    
    print(evaluation_list)


if __name__ == '__main__':
     main()