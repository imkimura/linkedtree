def organizeList(lword):
    listwords = []
    dicteres = dict()
    for l in lword:
        if len(listwords) > 0:
            notexist = True
            for w in range(0, len(listwords)):                        
                if l == listwords[w]["word"]:
                    notexist = False
                    listwords[w]["freq"] += 1            
            if notexist:
                listwords.append(({"word":l,"freq":1}))                
        else:        
            listwords.append(({"word":l,"freq":1}))
    return listwords

class Organization:        
    lword = list(str(input("Digite uma série de caracteres: ")))
    listwords = organizeList(lword)
    print(listwords)

if __name__ == "__main__":
    Organization()
    