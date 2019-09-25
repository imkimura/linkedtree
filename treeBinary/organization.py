class Organization:
    def __init__(self, lword):                      
        self.listwords = None
            
    def setlistwords(lword):
        listwords = []
        dicteres = dict()
        for l in lword:
            if len(listwords) > 0:
                notexist = True
                for w in range(0, len(listwords)):                        
                    if l == listwords[w]["left"]:
                        notexist = False
                        listwords[w]["chave"] += 1            
                if notexist:
                    listwords.append(({"chave":1, "left": l, "right":None}))                
            else:        
                listwords.append(({"chave":1, "left": l, "right":None}))
        return listwords       