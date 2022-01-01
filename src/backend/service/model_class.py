from gensim.models.ldamodel import LdaModel
import pandas as pd
import os
import gensim

from gensim.utils              import tokenize
from gensim.parsing.porter     import PorterStemmer
from gensim.corpora.dictionary import Dictionary
from gensim.models             import HdpModel
from nltk.stem import WordNetLemmatizer
from gensim.test.utils import datapath 
#import pyLDAvis.gensim
import pyLDAvis.gensim_models as gensimvis
import pickle 
import pyLDAvis
from gensim.models import HdpModel
from os.path import exists

class LdaModel:


    def _doc_tokenize(self,doc):
        return list(tokenize(doc))




    def _get_topic_distribution(self, n_topics, corpus_bow, corpus, id2word):
        lda_model = gensim.models.LdaModel(corpus=corpus_bow,
                                            id2word=id2word,
                                            num_topics=n_topics,
                                            alpha='auto',
                                            eta='auto', 
                                            chunksize=100,
                                            random_state=1,
                                            passes=10,
                                            per_word_topics=True)


        
        topics={}
        for i in range(0, lda_model.num_topics):
            topics[i]=[]
            for token, score in lda_model.show_topic(i, topn=n_topics):
                topics[i].append(token)
        
        rozklad =[]
        with open(f'rozklady.txt', 'w', encoding='utf-8') as f:    
            licznik = 1
            for doc in corpus_bow:
                
                
                data_to_save = ""
                roz = lda_model.get_document_topics(doc)
                rozklad.append(roz)
                for krotka in roz:
                    f.write(str(krotka[0]))
                    
                    f.write("-")
                    f.write(str(krotka[1]))
                    f.write(",")
                    licznik += 1
                f.write("\n")

        with open('./topics.txt', 'a', encoding='utf-8') as f:
            for topic, tokens in topics.items():
                f.write(str(topic)+" ###\n")
                for token in tokens:
                    f.write(str(token)+', ')
                f.write("\n")
        return rozklad

    def __init__(self, num_of_topics):
        self.num_of_topics = num_of_topics
        self.orzeczenia =[]
        titles=[]

        destination_directory = "./text_data/preprocessed_data_all_done"
        for f in os.listdir(destination_directory):
            with open(destination_directory+"/"+f, "r", encoding="utf-8") as f:
                lines = f .readlines()
                titles.append(lines[0])
                self.orzeczenia.append("".join(lines[1:]).lower())
        if not exists("./tytuly.txt"):
            with open("tytuly.txt", "w", encoding="utf-8") as f:
                for title in titles:
                    f.write(title+"\n")
        
        self.orzeczenia=[self._doc_tokenize(doc) for doc in self.orzeczenia]    # tokenizacja
        self.orzeczenia_int=Dictionary(self.orzeczenia) # przypisanie wyrazo id
        self.orzeczenia_bow=[self.orzeczenia_int.doc2bow(text) for text in self.orzeczenia]

    
    def get_topic_distribution(self):
        return self._get_topic_distribution(self.num_of_topics, self.orzeczenia_bow, self.orzeczenia, self.orzeczenia_int)





