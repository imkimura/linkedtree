listwords = []
dicteres = dict()
lword = list(str(input("Digite uma série de caracteres: ")))

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
print(listwords)