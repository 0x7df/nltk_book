from __future__ import division
import nltk

def lexical_diversity(text):
    return len(text) / len(set(text))

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

def target_puzzle(puzzle_letters, obligatory):
    puzzle_letters = nltk.FreqDist(puzzle_letters)
    wordlist = nltk.corpus.words.words()
    solutions = [w for w in wordlist if len(w) >= 4
                                    and obligatory in w
                                    and nltk.FreqDist(w) <= puzzle_letters]
    return solutions 
