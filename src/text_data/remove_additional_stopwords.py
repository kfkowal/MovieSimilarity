import os
from nltk.tokenize import word_tokenize


stop_words = []
with open("./additional_stop_list.txt", "r", encoding="utf-8") as f:
    words = f.readlines()
    for word in words:
        stop_words.append(str(word).strip())


destination_directory = "./text_data/preprocessed_data_ne_removed"


def remove_stop_wrods(text):
    token_list = word_tokenize(text)
    new_doc= [word for word in token_list if word not in stop_words]
    return " ".join(new_doc)


def pre_process(nazwa):
    doc=None
    with open(destination_directory+"/"+nazwa, "r", encoding='utf-8') as  f:
        doc=f.readlines()
    title= doc[0]
    doc="".join(doc[1:]).lower()
    
    doc=remove_stop_wrods(doc)


    with open(f'./text_data/preprocessed_data_all_done/{nazwa}', "w", encoding='utf-8') as  f:
        f.write(title+"\n")
        f.write(doc)
    print(f"zapisano {nazwa}")


for f in os.listdir(destination_directory):
    pre_process(f)

