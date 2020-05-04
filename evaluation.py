import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join
import time

def find_real_entities_retrieved(dict_gold, denotation):
    if dict_gold["text"] == denotation["text"]:
        real_entities_retrieved = 0
        for denot_gold in dict_gold["denotations"]:
            span_gold = denot_gold["span"]
            for denot in denotation["denotations"]:
                if span_gold == denot["span"]:
                    real_entities_retrieved += 1

    return real_entities_retrieved


def find_real_entities(dict_gold):
    real_entities = 0
    for denot_gold in dict_gold["denotations"]:
        real_entities += 1
    return real_entities


def find_entities_retrieved(denot):
    entities_retrieved = 0
    for denot_line in denot["denotations"]:
        entities_retrieved += 1
    return entities_retrieved


def get_recall(real_entities, real_entities_retrieved):
    if real_entities == 0:
        recall = '0 real ent'
    else:
        recall = real_entities_retrieved/real_entities
    return recall


def get_precision(real_entities_retrieved, entities_retrieved):
    if entities_retrieved == 0:
        precision = '0 ent ret'
    else:
        precision = real_entities_retrieved/entities_retrieved
    return precision


def main():
    #setting up gold dicts
    gold_std = [line for line in open('updated_gold_standard.json')]
    gold_dicts = []
    with open('updated_gold_standard.json') as f:
        for jsonObj in f:
            one_dict = json.loads(jsonObj)
            gold_dicts.append(one_dict)
    gold_dicts = sorted(gold_dicts, key=lambda i: i['text'])

    #setting up our tagged dicts
    denot_folder_path = os.path.abspath("gold_papers_tagged") + "/"
    denot_papers = [f for f in listdir(denot_folder_path) if isfile(join(denot_folder_path, f))]
    denot_dicts = []

    for filename in denot_papers:
        with open(denot_folder_path + filename) as f:
            for jsonObj in f:
                one_dict = json.loads(jsonObj)
                denot_dicts.append(one_dict)
    denot_dicts = sorted(denot_dicts, key=lambda i: i['text'])

    #start of evaluation
    evaluation_list = []
    tot_entities_retrieved = 0
    tot_real_entities = 0 
    tot_real_entities_retrieved = 0
    for dict_gold, dict_denot in zip(gold_dicts, denot_dicts):
        real_entities_retrieved = find_real_entities_retrieved(dict_gold, dict_denot)
        tot_real_entities_retrieved += real_entities_retrieved

        real_entities = find_real_entities(dict_gold)
        tot_real_entities += real_entities

        entities_retrieved = find_entities_retrieved(dict_denot)
        tot_entities_retrieved += entities_retrieved

        recall = get_recall(real_entities, real_entities_retrieved)
        precision = get_precision(real_entities_retrieved, entities_retrieved)

        evaluation_list.append({"cord_uid": dict_gold["cord_uid"], "recall":recall, "precision": precision})
    
    print(evaluation_list)
    print("tot_real_entities: " + str(tot_real_entities) + "\n"
    "tot_entities_retrieved: " + str(tot_entities_retrieved) + "\n"
    "tot_real_entities_retrieved: " + str(tot_real_entities_retrieved) + "\n"
    "total recall: " + str(get_recall(tot_real_entities, tot_real_entities_retrieved)) + "\n"
    "total precision: " + str(get_precision(tot_real_entities_retrieved, tot_entities_retrieved)) + "\n")


if __name__ == '__main__':
    main()
