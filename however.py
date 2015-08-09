import nltk
from nltk.corpus import gutenberg as gb
from nltk.corpus import brown     as bn

gbwords = gb.words('austen-emma.txt')

gbtext = nltk.Text(gbwords)

#gbtext.concordance('however', lines = 40)

gbindx = nltk.text.ConcordanceIndex(gbwords)
mid = len(gbindx.offsets('however'))
beg = len(gbindx.offsets('However'))
denom = 100./len(gbwords)
print beg/float(mid), beg*denom, mid*denom


bnwords = bn.words(categories='news')

bntext = nltk.Text(bnwords)

#bntext.concordance('however', lines = 40)

bnindx = nltk.text.ConcordanceIndex(bnwords)
mid = len(bnindx.offsets('however'))
beg = len(bnindx.offsets('However'))
denom = 100./len(bnwords)
print beg/float(mid), beg*denom, mid*denom

