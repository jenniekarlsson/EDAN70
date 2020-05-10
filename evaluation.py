import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join
import time


def find_real_entities_retrieved(dict_gold, dict_denot, scoredict):
    cats = list(scoredict.keys())
    if dict_gold["text"] == dict_denot["text"]:
        for denot_gold in dict_gold["denotations"]:
            span_gold = denot_gold["span"]
            this_cat = denot_gold["id"]
            if this_cat in cats:
                for denot in dict_denot["denotations"]:
                    if span_gold == denot["span"]:
                        scoredict[this_cat]["real_ent_ret"] += 1

    return scoredict

def find_real_entities(dict_gold, scoredict):
    cats = list(scoredict.keys())
    for match_gold in dict_gold["denotations"]:
        this_cat = match_gold["id"]
        if this_cat in cats:
            scoredict[this_cat]["real_ent"] += 1
    return scoredict

def find_entities_retrieved(dict_denot, scoredict):
    cats = list(scoredict.keys())
    for denot in dict_denot["denotations"]:
        this_cat = denot["id"]
        if this_cat in cats:
            scoredict[this_cat]["ent_ret"] += 1
    return scoredict

def update_scoredict(scoredict, dict_denot, dict_gold):
    cats = list(scoredict.keys())
    for denot in dict_denot["denotations"]:
        this_cat = denot["id"]
        if this_cat in cats:
            scoredict[this_cat]["ent_ret"] += 1
            
            if denot["span"] in dict_gold["denotations"]:
                scoredict[this_cat]["real_ent_ret"] += 1

    for gold_denot in dict_gold["denotations"]:
        this_cat = gold_denot["id"]
        if this_cat in cats:
            scoredict[this_cat]["real_ent"] += 1
    
    return scoredict

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
    dicts = sorted(dicts, key=lambda i: i['text'])
    return dicts

def main():
    #setting up gold dicts
    gold_folder_path = os.path.abspath("gold_standard_corpus_splitted_title_abstract") + "/"
    gold_dicts = get_dicts(gold_folder_path)

    #setting up our dicts
    denot_folder_path = os.path.abspath("gold_papers_tagged") + "/"
    denot_dicts = get_dicts(denot_folder_path)

    #setting up cats and dict for separate class scoring
    cats = ["Virus_SARS-CoV-2", "Disease_COVID-19", "Symptom_COVID-19"]
    entlist = ["real_ent_ret","real_ent","ent_ret"]
    entdict = dict(zip(entlist, [0 for i in range(len(cats))]))
    scoredict = dict(zip(cats, [entdict for i in range(len(cats))]))

    #evaluation
    for dict_gold, dict_denot in zip(gold_dicts, denot_dicts):

        scoredict = update_scoredict(scoredict, dict_denot, dict_gold)

    print(str(scoredict) + "\n")

    rec_prec = ["recall", "precision"]
    rec_prec_init = dict(zip(rec_prec, [0 for i in range(len(rec_prec))]))
    rec_prec_dict = dict(zip(cats, [rec_prec_init for i in range(len(cats))]))
    for cat in scoredict:
        rec_prec_dict[cat]["recall"] = get_recall(scoredict[cat]["real_ent"], scoredict[cat]["real_ent_ret"])
        rec_prec_dict[cat]["precision"] = get_precision(scoredict[cat]["real_ent_ret"], scoredict[cat]["ent_ret"])

   
    #print(rec_prec_dict)
    

if __name__ == '__main__':
    main()
