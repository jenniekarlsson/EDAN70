

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
        span_gold = denot_gold["span"]
        real_entities += 1
return real_entities


def find_entities_retrived(denot)
    entities_retrived = 0
    for span in denot["denotations"][span]:
        entities_retrived += 1
return entities_retrived


def Recall():
    recall = real_entities_retrived/real_entities
    return recall


def Precision():
    precision = real_entities_retrived/entities_retrieved
    return precision


def main():
    


if __name__ == '__main__':
     main()