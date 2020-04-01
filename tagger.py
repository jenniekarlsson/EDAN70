import sys, os, pathlib

parentpath = str(pathlib.Path(__file__).parent.absolute())

metafile = open(parentpath + "/meta_subset_100.csv")

#LOOP START
filename = os.listdir(parentpath + "/comm_use_subset_100")[0]
filepath = parentpath + "/comm_use_subset_100" + "/" + filename
f = open(filepath)

for line in metafile:
    print(filename[:-5])
    if filename[:-5] in metafile:
        cord_uid = line[:8] # assuming all cord_uid has 8 characters
        print(cord_uid)


#LOOP END



