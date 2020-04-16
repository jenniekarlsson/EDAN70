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

     return [title_data, abstract_data, body_text_data]

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
     virus_list = [line.strip() for line in open("Supplemental_file1.txt")]
     disease_list = [line.strip() for line in open ("Supplemental_file2.txt")]

     dicts["Virus_SARS-CoV-2"] = virus_list
     dicts["Disease_COVID-19"] = disease_list

def get_longest_match(subsection, d):
     longestmatch = ""
     longestbegin = -1
     longestend = -1
     for phrase in d:
          begin = subsection.find(phrase)
          end = begin + len(phrase)
          if begin > 0:
               if is_overlapping(begin, end, longestbegin, longestend):
                    if len(longestmatch) < len(phrase):
                         longestmatch = phrase
                         longestbegin = begin
                         longestend = begin + len(longestmatch)
               elif longestmatch == "":
                    longestmatch = phrase
                    longestbegin = begin
                    longestend = begin + len(longestmatch)

     if not longestmatch == "":
          return longestbegin, longestmatch, longestend
     else:
          return None, None, None

def is_overlapping(b1, e1, b2, e2):
     return not (e2<b1 or e1<b2)
     

def tag_article(article_path):
     article = read_article(article_path)
     section_nr = 0
     denotated_sections = []

     for section in article:
          for subsection in section:
               subsection = subsection.lower()
               denotations = []
               longestmatch = ""
               for id in dicts.keys():
                    longestbegin, longestmatch, longestend = get_longest_match(subsection, dicts[id])
                    info = {"id": id, "span":{"begin":longestbegin, "end":longestend}, "obj":"?"}
                    if not longestmatch == None:
                         denotations.append(info)
                         print("found", longestmatch)
                              
               denotated_sections.append(denotations)
     return denotated_sections

def generate_JSONs(denotated_sections, j):
     for i, f in enumerate(denotated_sections):
          with open("result.json" + str(i) +str(j), "w") as fp:
               json.dump(f, fp)


def main():
     subset_path = os.path.abspath("comm_use_subset_100") + "/"
     comm_use_subset_100 = [f for f in listdir(subset_path) if isfile(join(subset_path, f))]
     fileonepath = subset_path + comm_use_subset_100[1]
     #fileonepath = "/home/jesper/EDAN70/comm_use_subset_100/comm_use_subset_100/04d02a37dcbb17916d2a5c03288cb9b59000ebba.json"
     
     setup_dicts()

     denot_sections = tag_article("/home/jesper/EDAN70/fa16032841f11e0924b539d21444915e3bcc9a0e.json")
     print(denot_sections)

     #for j in range(100):
          #print(comm_use_subset_100[i])
          #print(read_meta(comm_use_subset_100[i][:-5]))

          #denot_sections = tag_article(subset_path + comm_use_subset_100[j])
          #print(denot_sections)
          #generate_JSONs(denot_sections, j)

if __name__ == '__main__':
     main()
     

