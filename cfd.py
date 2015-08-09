import nltk
from nltk import ConditionalFreqDist as cfd

names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')

mycfd = cfd(
            (condition, name[0])
            for condition in names.fileids()
            for name in names.words(condition) 
        )

mycfd.plot()

