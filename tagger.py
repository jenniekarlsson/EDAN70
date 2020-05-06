import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join
import re

dicts = {}

def path_to_paper_id(path):
     return path.split("/")[-1][:-5]

def read_article(path):
     ret = []
     with open(path) as f:
          d = json.load(f)
          ret.append((d["metadata"]["title"], "title"))
          for t in d["abstract"]:
               ret.append((t["text"], "abstract"))
          for t in d["body_text"]:
               ret.append((t["text"], "body_text"))
     return ret

def read_meta(paperid, metaf):
     metafile = open(metaf, "r")
     for line in metafile:
          if paperid in line:
               metaline = line.split(",")
               cord_uid = metaline[0]
               sourcedb = metaline[2]
               sourceid = metaline[5]
               obj = metaline[-1]
               return [cord_uid, sourcedb, sourceid, obj]
     return [0,0,0,0]

def setup_dicts():
     virus_list = [line.strip() for line in open("Supplemental_file1.txt")]
     virus_list.sort(key = len)
     disease_list = [line.strip() for line in open ("Supplemental_file2.txt")]
     disease_list.sort(key = len)
     symptom_list = [line.strip() for line in open ("Supplemental_file3.txt")]
     symptom_list.sort(key = len)

     dicts["Virus_SARS-CoV-2"] = virus_list
     dicts["Disease_COVID-19"] = disease_list
     dicts["Symptom_COVID-19"] = symptom_list

def tag_article(article_path, metaf):
     article = read_article(article_path)
     denotated_sections = []
     obj = read_meta(path_to_paper_id(article_path), metaf)[3]

     for subsection in article:
          subsection = subsection[0].lower()
          denotations = []
          for id in dicts.keys():
               s = ""
               re_or = "(" + s.join([x + "|" for x in dicts[id]])[:-1] + ")"
               info = [(id, m.group(0), m.start(0), m.end(0)) for m in re.finditer(re_or, subsection)]

               if(len(info) > 0):
                    for x in info:
                         infodict = {"id": x[0], "span":{"begin":x[2], "end":x[3]}, "obj":obj}
                         denotations.append(infodict)

          denotated_sections.append(denotations)

     return denotated_sections, article

def generate_JSONs(denotated_sections, article, path, metaf):
     [cord_uid, sourcedb, sourceid, obj] = read_meta(path_to_paper_id(path), metaf)
     for i in range(len(article)):
          text = article[i][0]
          section = article[i][1]
          denot = denotated_sections[i]

          json_data = {"cord_uid":cord_uid,
                         "sourcedb":sourcedb,
                         "sourceid":sourceid,
                         "div_id":i,
                         "text":text,
                         "denotations":denot
                         }
          with open(str(cord_uid) + "-" + str(i) + "-" + section + ".json", "w") as fp:
               json.dump(json_data, fp)


def main():
     #subset_path = os.path.abspath("comm_use_subset_100") + "/"
     goldpapers_path = os.path.abspath("gold_papers") + "/"
     #comm_use_subset_100 = [f for f in listdir(subset_path) if isfile(join(subset_path, f))]
     goldpapers = [f for f in listdir(goldpapers_path) if isfile(join(goldpapers_path, f))]

     metaf = "gold_standard_subset_10.csv"

     setup_dicts()

     #for filepath in goldpapers:
     #     denot_sec, art = tag_article(goldpapers_path + filepath, metaf)
     #     generate_JSONs(denot_sec, art, filepath, metaf)

if __name__ == '__main__':
     main()
     

