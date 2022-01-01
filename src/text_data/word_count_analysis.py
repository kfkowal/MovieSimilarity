
import os
from nltk.tokenize import word_tokenize

destination_directory = "./text_data/preprocessed_data_ne_removed"


word_data = {}
number_of_documents = 0
number_of_all_words= 0


def analysis(nazwa):
    global number_of_documents, number_of_all_words
    number_of_documents +=1
    with open(destination_directory+"/"+nazwa, "r", encoding='utf-8') as  f:
        doc=f.readlines()
    title= doc[0]
    text="".join(doc[1:]).lower()
    token_list = word_tokenize(text)

    for token in token_list:
        number_of_all_words +=1
        val = word_data.get(token)

        if val == None:
            word_data[token] = 1
        else:
            word_data[token] +=1



    


for f in os.listdir(destination_directory):
    analysis(f)


a = sorted(word_data.items(), key=lambda x: x[1])

with open('./word_count_sorted.txt','w',encoding='utf-8') as  f:
    f.write(f"Liczba wszystkich dokumentów: {number_of_documents}\n")
    f.write(f"Liczba wszystkich wyrazów {number_of_all_words}\n")
    f.write(f"Liczba unikalnych wyrazów: {len(word_data.keys())}\n")
    f.write(f"Średnia liczba wyrazów na dokument {number_of_all_words/number_of_documents}\n")
    for krotka in a:
        f.write(str(krotka[0])+","+str(krotka[1])+'\n')
