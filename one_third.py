import nltk
import operator
from nltk.corpus import webtext  as wt
from nltk.corpus import nps_chat as nc
from nltk.corpus import brown    as bn

#all_words = [wd.lower() for wd in wt.words() + nc.words() if wd.isalpha()]
all_words = [wd.lower() for wd in bn.words(categories='lore') if wd.isalpha()]

cfd = nltk.FreqDist(all_words)

print cfd.max()

sorted_x = sorted(cfd.items(), key=operator.itemgetter(1))

print len(all_words), len(cfd), len(sorted_x)
print sum(cfd.values())


total = 0.
index = -1

while total < 0.33333333*sum(cfd.values()):
    print sorted_x[index][0]
    total += sorted_x[index][1]
    index -= 1
print abs(index)
