import nltk
from nltk.corpus import wordnet as wn

for synset in wn.synsets('code'):
    print synset
    print synset.definition()
    print synset.examples()
    print synset.lemma_names()
    for lemma in synset.lemmas():
        print '    ',lemma,'\t',lemma.name(),'\t',lemma.synset()
    print

synset = wn.synset('code.n.03')
synset = wn.synset('tree.n.01')

print "Types..."
types = synset.hyponyms()
print types

print
print "Paths..."
paths = synset.hypernym_paths()
print len(paths)
for i, path in enumerate(paths):
    print "    For path",i
    print [nextup for nextup in paths[i]]

print
print "Holonyms (containers)..."
print "Parts:     ",[ph for ph in synset.part_holonyms()] 
print "Members:   ",[mh for mh in synset.member_holonyms()]
print "Substances:",[sh for sh in synset.substance_holonyms()]

print
print "Meronyms (components)..."
print [pm for pm in synset.part_meronyms()]
print [mm for mm in synset.member_meronyms()]
print [sm for sm in synset.substance_meronyms()]
