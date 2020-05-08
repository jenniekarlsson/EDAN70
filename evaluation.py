import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join
import time

def find_real_entities_retrieved(dict_gold, dict_denot, cats):
    real_entities_retrieved = 0
    if dict_gold["text"] == dict_denot["text"]:
        for denot_gold in dict_gold["denotations"]:
            span_gold = denot_gold["span"]
            this_cat = denot_gold["id"]
            if this_cat in cats:
                for denot in dict_denot["denotations"]:
                    if span_gold == denot["span"]:
                        real_entities_retrieved += 1

    return real_entities_retrieved


def find_real_entities(dict_gold, cats):
    real_entities = 0
    for match_gold in dict_gold["denotations"]:
        if match_gold["id"] in cats:
            real_entities += 1
    return real_entities


def find_entities_retrieved(dict_denot):
    return len(dict_denot["denotations"])


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

def get_dicts(folder_path):
    papers = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    dicts = []

    for filename in papers:
        with open(folder_path + filename, 'r') as f:
            one_dict = json.load(f)
            dicts.append(one_dict)
    print(dicts)
    dicts = sorted(dicts, key=lambda i: i['text'])
    return dicts

def main():
    #setting up gold dicts
    gold_folder_path = os.path.abspath("gold_standard_corpus_splitted_title_abstract") + "/"
    gold_dicts = get_dicts(gold_folder_path)

    #setting up our dicts
    denot_folder_path = os.path.abspath("gold_standard_subset_10") + "/"
    denot_dicts = get_dicts(denot_folder_path)

    #setting up used categories (should be automated if muchos categories)
    cats = ["Virus_SARS-CoV-2", "Disease_COVID-19", "Symptom_COVID-19"]

    #evaluation
    evaluation_list = []
    tot_entities_retrieved = 0
    tot_real_entities = 0 
    tot_real_entities_retrieved = 0
    for dict_gold, dict_denot in zip(gold_dicts, denot_dicts):

        real_entities_retrieved = find_real_entities_retrieved(dict_gold, dict_denot, cats)
        tot_real_entities_retrieved += real_entities_retrieved

        real_entities = find_real_entities(dict_gold, cats)
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
