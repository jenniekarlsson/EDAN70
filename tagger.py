import sys, os, pathlib, json

filename = os.listdir(parentpath + "/comm_use_subset_100")[0]
filepath = parentpath + "/comm_use_subset_100" + "/" + filename

get_cord_uid(filename)

suffix_counter = 0

with open(filepath) as f:
    d = json.load(f)

    title_file_name = cord_uid + '-' + str(suffix_counter) + '-' + 'title'
    title_data = d["metadata"]["title"]
    
with open('title_file_name.txt', 'w') as outfile:
     json.dump(data, outfile)



def get_cord_uid(filename):
     for line in metafile:
          if filename[:-5] in line:
               cord_uid = line[:8]
               return cord_uid

if __name__ == '__main-__':
     parentpath = str(pathlib.Path(__file__).parent.absolute())
     metafile = open(parentpath + "/meta_subset_100.csv")

