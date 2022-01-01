

additional_stop_words = []
with open("./word_count_sorted.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()[4:]
    

    for line in lines:
        tmp = line.strip().split(",")

        if int(tmp[1]) <=50 or  int(tmp[1]) > 450:
            additional_stop_words.append(tmp[0])

    
with open("./additional_stop_list.txt", "w", encoding="utf-8") as f:
    for word in additional_stop_words:
        f.write(word+"\n")