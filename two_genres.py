import nltk
from nltk.corpus import gutenberg as gb
from nltk.corpus import brown     as br
from nltk.corpus import stopwords
import operator

blake_words = [wd.lower() for wd in gb.words('blake-poems.txt')
               if wd.isalpha()]
scifi_words = [wd.lower() for wd in br.words(categories='science_fiction')
               if wd.isalpha()]

print len(set(blake_words))/float(len(blake_words))
print len(set(scifi_words))/float(len(scifi_words))

common_words = ((set(blake_words) & set(scifi_words)) - 
                set(stopwords.words()))

cfd = nltk.FreqDist(
          wd for wd in blake_words + scifi_words
          if wd in common_words
      )

#cfd.plot()
#print cfd.max()

sorted_x = sorted(cfd.items(), key=operator.itemgetter(1))

print sorted_x[-45:]

blake_text = nltk.Text(gb.words('blake-poems.txt'))
scifi_text = nltk.Text(br.words(categories = 'science_fiction'))

blake_text.concordance('angel')
scifi_text.concordance('angel')
