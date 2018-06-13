# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:03:50 2018

@author: Nivethitha
"""

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import WordPunctTokenizer
import string
from string import punctuation
from nltk.corpus import senseval
from collections import Counter
import numpy as np
import glob
import pandas as pd

wordnet_lemmatizer = WordNetLemmatizer()
snowball_stemmer = SnowballStemmer("english")
stopwords = stopwords.words("english")

def preprocess(text, stopword_list):
   # Make lowercase
    text = text.lower()
    # Tokenize
    words = WordPunctTokenizer().tokenize(text)
    output = []
    for word in words:
        # Remove stopwords
        if word not in stopwords and not word.isdigit():
            # Lemmatize
            word = wordnet_lemmatizer.lemmatize(word)
            # Stem
            word = snowball_stemmer.stem(word)
            output.append(word)
    return output

#def sim(text, definition):
        
    
    
    
    
#if __name__ == "__main__":
#    bass_file = "wsd_data/bass.test"
#    crane_file = "wsd_data/crane.test"
#    motion_file = "wsd_data/motion.test"
#    palm_file = "wsd_data/palm.test"
#    plant_file = "wsd_data/plant.test"
#    tank_file = "wsd_data/tank.test"
#    
#    bass_definition_file = "wsd_data/bass.definition"
#    crane_definition_file = "wsd_data/crane.definition"
#    motion_definition_file = "wsd_data/motion.definition"
#    palm_definition_file = "wsd_data/palm.definition"
#    plant_definition_file = "wsd_data/plant.definition"
#    tank_definition_file = "wsd_data/tank.definition"
#    
#    files = [bass_file, crane_file, motion_file, palm_file, plant_file, tank_file]
#    definition_files = [bass_definition_file,crane_definition_file,motion_definition_file,palm_definition_file,plant_definition_file,tank_definition_file]
#    
#    for file in files:
#        with open(file) as f:
#            text = f.read()
#        text = text.replace("\n", " ")
#        print("Preprocessing", file.split("/")[-1])
#        text = preprocess(text, stopwords + list(string.punctuation) + ["\ufeff"])
#        print(len(text), "tokens\n")
#        
#    for def_file in definition_files:
#        with open(def_file) as f:
#            def_text = f.read()
#        def_text = def_text.replace("\n", " ")
#        print("Preprocessing", def_file.split("/")[-1])
#        text = preprocess(def_text, stopwords + list(string.punctuation) + ["\ufeff"])
#        print(len(def_text), "tokens\n")
#        print("def_text:",def_text)
        
def overlapcontext(definition, sentence):
#    print("definition:",definition)
#    preprocess_definition = preprocess(definition, stopwords + list(string.punctuation) + ["\ufeff"])
#    preprocess_sentence = preprocess(sentence, stopwords + list(string.punctuation) + ["\ufeff"])
##    print("preprocess_definition:",preprocess_definition)
##    print("preprocess_sentence:",preprocess_sentence)
    definition = set(definition)
    sentence = set(sentence)
##    print(len(preprocess_definition.intersection(preprocess_sentence)))
    return len(definition.intersection(sentence))
    
def lesk(word,sentence):
    bestsense = None
    maxoverlap = 0
    
    with open("wsd_data/crane.definition") as f:
        file = f.read()
    word = word.split("/")[-1]
    word = word.split(".")[0]
    for sense in file:
#        print("sense:",sense)
        overlap = overlapcontext(sense,sentence)
        for h in sense:
            overlap += overlapcontext( h, sentence )
        if overlap > maxoverlap:
                maxoverlap = overlap
                bestsense = sense
    return bestsense
    
if __name__ == "__main__":
    
    definition = "A crane is a type of machine, generally equipped with a hoist, wire ropes or chains, and sheaves, that can be used both to lift and lower materials and to move them horizontally. It is mainly used for lifting heavy things and transporting them to other places"
    word = "crane"    
    sentence = "Up until eleven o'clock everything went pretty well, When just as you start thinking to yourself that's the last one for a while, lo and behold another wagon turns up. It was quite pleasant to get a radio call at 1115 hours to say stop doing the container wagons, we're starting the Arakan.' This job consisted of picking up thirty-six containers from the jetty Where they were being unloaded from HMAV Arakan (one of the two Army Landing Craft Logistic) and moving them to the container park. Quite a job to keep up with the crane"    
    preprocess_definition = preprocess(definition, stopwords + list(string.punctuation) + ["\ufeff"])
    preprocess_sentence = preprocess(sentence, stopwords + list(string.punctuation) + ["\ufeff"])
    print("preprocess_definition:",preprocess_definition)
    print("preprocess_sentence:",preprocess_sentence)
#    preprocess_definition = set(preprocess_definition)
#    preprocess_sentence = set(preprocess_sentence)    
    a=lesk(word,sentence)
    print(a)
    