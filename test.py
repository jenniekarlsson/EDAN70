import re
t = "once upon a time sars 2 infection sars 2019"

viruslist = [line.strip() for line in open("Supplemental_file1.txt")]
sort_viruslist = sorted(viruslist, key=len)[::-1]

or_viruslist = ""
re_or = "(" + or_viruslist.join([x + "|" for x in sort_viruslist])[:-1] + ")"

#print([(m.group(0), m.start(0), m.end(0)) for m in re.finditer(re_or, t)])


ret = [(m.group(0), m.start(0), m.end(0)) for m in re.finditer("abc|ab", "aljsdnskj abc asodji ab")]
print( ret)
