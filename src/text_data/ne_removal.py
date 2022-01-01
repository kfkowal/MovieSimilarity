
import en_core_web_sm
import os
nlp = en_core_web_sm.load()
ents_count={}
destination_directory = "./text_data/preprocessed_data"


def analysis_test(nazwa):


    with open(destination_directory+"/"+nazwa, "r", encoding='utf-8') as  f:
        doc=f.readlines()
    title= doc[0]
    text="".join(doc[1:]).lower()
    doc=nlp(text)
    
    tags=[(X.text, X.label_) for X in doc.ents]

    for tag in tags:
        if ents_count.get(tag[1]) == None:
            ents_count[tag[1]] = [1,[tag[0]]]
        else :
            tmp=ents_count[tag[1]]
            tmp[0] +=1
            tmp[1].append(tag[0])
            ents_count[tag[1]]= tmp



def analysis(nazwa):
    with open(destination_directory+"/"+nazwa, "r", encoding='utf-8') as  f:
        doc=f.readlines()
    title= doc[0]
    text="".join(doc[1:]).lower()
  
    doc=nlp(text)
    tmp=[]
    for e in doc:
        if  not e.ent_type_ in ["PERSON", "DATE", "ORDINAL", "CARDINAL", "MONEY", "TIME", "GPE","LANGUAGE","PRODUCT", "LAW","QUANTITY", "PERCENT"]:
            tmp.append(e.text)
    tmp = " ".join(tmp)

    with open(f'./text_data/preprocessed_data_ne_removed/{nazwa}', "w", encoding='utf-8') as  f:
        f.write(title+"\n")
        f.write(tmp)
    print(f"zapisano {nazwa}")

    


for f in os.listdir(destination_directory):
    analysis(f)


# with open("./word_stats_named_entity.txt", "w", encoding="utf-8") as f:
#     for key, val in ents_count.items():
#         f.write("\n"+key+':'+str(val[0]) +"\n")
#         for i in val[1:]:
#             f.write(str(i)+",")



