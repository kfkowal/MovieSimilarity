from gensim.parsing.preprocessing import (
strip_multiple_whitespaces,
strip_numeric,
strip_short)
import regex as re
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from gensim.parsing.porter     import PorterStemmer
from nltk.stem import WordNetLemmatizer
import os


import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()




lemmatizer = WordNetLemmatizer()
#lemmatizer.lemmatize("rocks")
stop_words = set(stopwords.words('english'))

destination_directory = "./text_data/raw_data/"


def ne_removal(text):
    token_list = word_tokenize(text)
    

def remove_punctuation(text):
    return re.sub("\p{P}+", " ", text)

def remove_stopwords(text):
    token_list = word_tokenize(text)
    tokens_without_sw = [word for word in token_list if not word in stop_words]
    return " ".join(tokens_without_sw)

def lemmatyze(text):
    token_list = word_tokenize(text)
    tmp=[lemmatizer.lemmatize(x) for x in token_list]
    return " ".join(tmp)

def pre_process(nazwa):
    doc=None
    with open(destination_directory+"/"+nazwa, "r", encoding='utf-8') as  f:
        doc=f.readlines()
    title= doc[0]
    doc="".join(doc[1:]).lower()
    

    doc=remove_stopwords(doc)
    doc=remove_punctuation(doc)
    doc=strip_numeric(doc)
    doc=remove_stopwords(doc)
    doc=strip_short(doc)
    doc=strip_multiple_whitespaces(doc)
    doc = lemmatyze(doc)
    doc=doc.lower()

    with open(f'./text_data/preprocessed_data/{nazwa}', "w", encoding='utf-8') as  f:
        f.write(title+"\n")
        f.write(doc)
    print(f"zapisano {nazwa}")


for f in os.listdir(destination_directory):
    pre_process(f)

