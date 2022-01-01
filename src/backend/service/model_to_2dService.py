
from .model_class import LdaModel
from sklearn.manifold import MDS

class ModelTo2D:
    def __init__(self, number_of_topics):
        self.number_of_topics = number_of_topics
        self.sparse_vectors=[]
        self.model=None

    def _load_data_from_file(self):
        with open('./rozklady.txt', 'r', encoding='utf-8') as f:
            for line in f:
                tmp_line = []
                for krotka_str in line.split(',')[0:-1]:
                    krotka = krotka_str.split("-")
                    topic = int(krotka[0].strip())
                    v = float(krotka[1].strip())
                    tmp = [topic, v]
                    tmp_line.append(tmp)
                self.sparse_vectors.append(tmp_line)

    def _load_data(self):
        self.model = LdaModel(self.number_of_topics)
        self.sparse_vectors = self.model.get_topic_distribution()


    def get_2d_coordinates(self):

        self._load_data()

        max_val = -1
        min_val = 1000000000000000000
        max_val_top = -1

        for wek in self.sparse_vectors:
            for krotka in wek:
                if krotka[1] > max_val:
                    max_val = krotka[1]
                if krotka[1] < min_val:
                    min_val=krotka[1]
                if krotka[0] > max_val_top:
                    max_val_top = krotka[0]


        wektory = [] 
        zerowy = [0 for j in range(0, max_val_top+1)]
        for i in range(0, len(self.sparse_vectors)):
            wektory.append([0 for j in range(0, max_val_top+1)])

        for i in range(0, len(self.sparse_vectors)):
            for krotka in self.sparse_vectors[i]:
                if krotka[1] < 0.05:
                    wektory[i][krotka[0]] = krotka[1]
                    #wektory[i][krotka[0]] = 0
                else:
                    wektory[i][krotka[0]] = krotka[1]

        mds= MDS(2,random_state=0)


        wek2d = mds.fit_transform(wektory)

        minX, maxX, minY, maxY = 1000, -1000, 1000, -1000

        for tuple in wek2d:
            if tuple[0] > maxX: maxX = tuple[0]
            if tuple[0] < minX: minX = tuple[0]

            if tuple[1] > maxY: maxY = tuple[1]
            if tuple[1] < minY: minY = tuple[1]


            
            
        with open("./wiz_wek.txt", 'w', encoding='utf-8') as f:
            for k in wek2d:
                f.write(str(k[0]))
                f.write(",")
                f.write(str(k[1]))
                f.write(":")

        regualr_list = []

        for tup in wek2d:
            x1 = tup[0]
            x2 = tup[1]
            regualr_list.append([x1,x2])

        odp = {
            "minX" : minX,
            'maxX' :maxX,
            'minY' : minY,
            'maxY' :maxY,
            'coordinates' : regualr_list

        }
        return odp



