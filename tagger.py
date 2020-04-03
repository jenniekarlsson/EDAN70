import sys, os, pathlib, json
from os import listdir
from os.path import isfile, join


def path_to_paper_id(path):
     return path.split("/")[-1][:-5] #cutting last 5 cuts ".json"

def read_article(path):
     with open(path) as f:
          d = json.load(f)
          title_data = d["metadata"]["title"]
          abstract_data = d["abstract"]
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
     print(coord_uid, sourcedb, sourceid)
     return [coord_uid, sourcedb, sourceid]

def setup_dicts():
     global dicts
     covid19_dict = [line for line in open ("Supplemental_file2.txt")]
     sars_dict = [line for line in open("Supplemental_file1.txt")]

     dicts.append(covid19_dict)
     dicts.append(sars_dict)

def tag_article(article_path):
     [title_data, abstract_data, body_text_data] = read_article(article_path)

     #time complexity = ouff



def generate_json():
     #title
     #abstract (if it exists)
     #body_text
     return

def main():
     subset_path = os.path.abspath("comm_use_subset_100") + "/"
     comm_use_subset_100 = [f for f in listdir(subset_path) if isfile(join(subset_path, f))]
     fileone = subset_path + comm_use_subset_100[0]

     setup_dicts()
          
if __name__ == '__main__':
     main()
     

