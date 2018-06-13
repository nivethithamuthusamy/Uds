#Author: Nurendra Choudhary.
#Algorithm Reference: http://en.wikipedia.org/wiki/Lesk_algorithm

from nltk.corpus import wordnet 
#from nltk.tokenize.punkt import sent_tokenize
#from nltk import wordpunct_tokenize
from nltk.tokenize import WordPunctTokenizer

functionwords = ['about', 'across', 'against', 'along', 'around', 'at',
                 'behind', 'beside', 'besides', 'by', 'despite', 'down',
                 'during', 'for', 'from', 'in', 'inside', 'into', 'near', 'of',
                 'off', 'on', 'onto', 'over', 'through', 'to', 'toward',
                 'with', 'within', 'without', 'anything', 'everything',
                 'anyone', 'everyone', 'ones', 'such', 'it', 'itself',
                 'something', 'nothing', 'someone', 'the', 'some', 'this',
                 'that', 'every', 'all', 'both', 'one', 'first', 'other',
                 'next', 'many', 'much', 'more', 'most', 'several', 'no', 'a',
                 'an', 'any', 'each', 'no', 'half', 'twice', 'two', 'second',
                 'another', 'last', 'few', 'little', 'less', 'least', 'own',
                 'and', 'but', 'after', 'when', 'as', 'because', 'if', 'what',
                 'where', 'which', 'how', 'than', 'or', 'so', 'before', 'since',
                 'while', 'although', 'though', 'who', 'whose', 'can', 'may',
                 'will', 'shall', 'could', 'be', 'do', 'have', 'might', 'would',
                 'should', 'must', 'here', 'there', 'now', 'then', 'always',
                 'never', 'sometimes', 'usually', 'often', 'therefore',
                 'however', 'besides', 'moreover', 'though', 'otherwise',
                 'else', 'instead', 'anyway', 'incidentally', 'meanwhile']

def overlapcontext( synset, sentence ):
    gloss = set(WordPunctTokenizer().tokenize(synset.definition()))
#    print("gloss",gloss)
#    for i in synset.examples():
#         gloss.union(i)
    gloss = gloss.difference( functionwords )
    if isinstance(sentence, str):
        sentence = set(sentence.split(" "))
    elif isinstance(sentence, list):
        sentence = set(sentence)
    elif isinstance(sentence, set):
        pass
    else:
        return
    sentence = sentence.difference( functionwords )
    return len( gloss.intersection(sentence) )

def lesk( word, sentence ):
    bestsense = None
    maxoverlap = 0
    word=wordnet.morphy(word) if wordnet.morphy(word) is not None else word
#    print("word:",word)
    for sense in wordnet.synsets(word):
        print("sense:",sense)
        overlap = overlapcontext(sense,sentence)
        for h in sense.hyponyms():
            overlap += overlapcontext( h, sentence )
        if overlap > maxoverlap:
                maxoverlap = overlap
                bestsense = sense
    return bestsense

    
sentence = "And so am I, whether I smoke or no. And not alone in habit and device, Exterior form, outward accoutrement, But from the inward motion to deliver"
word = "motion"

a = lesk(word,sentence)
print("\n\nSynset:",a)
if a is not None:
    print("Meaning:",a.definition())
    num=0
    print("\nExamples:")
    for i in a.examples():
        num=num+1
        print(str(num)+'.'+')',i)