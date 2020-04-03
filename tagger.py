import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join

dicts = {}

def path_to_paper_id(path):
     return path.split("/")[-1][:-5] #cutting last 5 cuts ".json"

def read_article(path):
     with open(path) as f:
          d = json.load(f)
          title_data = [d["metadata"]["title"]]
          abstract_data = [a["text"] for a in d["abstract"]]
          body_text_data = [t["text"] for t in d["body_text"]] #a list of all text sections in article


     return [title_data, abstract_data, body_text_data] #

def read_meta(paperid):
     metafile = open("meta_subset_100.csv", "r")
     for line in metafile:
          if paperid in line:
               metaline = line.split(",")
               coord_uid = metaline[0]
               sourcedb = metaline[2]
               sourceid = metaline[5]
     return [coord_uid, sourcedb, sourceid]

def setup_dicts():
     covid19_list = [line for line in open ("Supplemental_file2.txt")]
     sars_list = [line for line in open("Supplemental_file1.txt")]

     dicts["covid19"] = covid19_list
     dicts["sars"] = sars_list
    

def tag_article(article_path):
     article = read_article(article_path)
     section_nr = 0
     denotated_sections = []

     for section in article:
          denotations = []
          for subsection in section:
               for id in dicts.keys():
                    for phrase in dicts[id]:
                         begin = subsection.find("virus")
                         if begin > 0:#found phrase
                              end = begin + len(phrase)
                              info = {"id": id, "span":{"begin":begin, "end":end}, "obj":"?"}
                              denotations.append(info)
               denotated_sections.append(denotations)
     return denotated_sections

def generate_JSONs(denotated_sections):
     for filenr in range(20):
          with open("result.json" + str(filenr), "w") as fp:
               json.dump(denotated_sections[filenr], fp)




def main():
     subset_path = os.path.abspath("comm_use_subset_100") + "/"
     comm_use_subset_100 = [f for f in listdir(subset_path) if isfile(join(subset_path, f))]
     fileonepath = subset_path + comm_use_subset_100[0]
     setup_dicts()

     denot_sections = tag_article(fileonepath)
     generate_JSONs(denot_sections)
          
if __name__ == '__main__':
     main()
     

