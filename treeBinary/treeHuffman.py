import json
import pprint
from node import Node
from organization import Organization
"""
 Detalhes:
    Aqui importamos a classe Nó para popularmos nossa Árvore.
"""

def compressTree(lower, higher, listOrd):
    if (listOrd[lower]["right"] is not None) or (listOrd[higher]["right"] is not None):
        if (listOrd[lower]["right"] is not None) and (listOrd[higher]["right"] is not None):
            freq = listOrd[lower]["chave"] + listOrd[higher]["chave"]
            listOrd.append({
                "chave": freq,
                "left":  listOrd[lower],                
                "right": listOrd[higher] 
            })
        else:
            if listOrd[higher]["right"] is not None:
                freq = listOrd[lower]["chave"] + listOrd[higher]["chave"]
                listOrd.append({
                    "chave": freq,
                    "left":  listOrd[lower]["left"],                    
                    "right": listOrd[higher] 
                })
            else:
                freq = listOrd[lower]["chave"] + listOrd[higher]["chave"]
                listOrd.append({
                    "chave": freq,
                    "left":  listOrd[higher]["left"],                    
                    "right": listOrd[lower] 
                })
    else:
        freq = listOrd[lower]["chave"] + listOrd[higher]["chave"]
        listOrd.append({
            "left":  listOrd[lower]["left"],
            "chave": freq,
            "right": listOrd[higher]["left"]
        })
    return listOrd

def buildingTree(listOrganized):
    sameposition = None
    lowposition = 0
    secondMP = (len(listOrganized) - 1)

    for l in range(0, len(listOrganized)):
        if listOrganized[lowposition]["chave"] > listOrganized[l]["chave"]:
            lowposition = l    
        else:
            if (listOrganized[lowposition]["chave"] == listOrganized[l]["chave"]) and (listOrganized[lowposition]["left"] != listOrganized[l]["left"]):
                sameposition = l        
            else:
                if (listOrganized[l]["chave"] > listOrganized[lowposition]["chave"]) and (listOrganized[l]["chave"] < listOrganized[secondMP]["chave"]) and (listOrganized[l]["chave"] != listOrganized[secondMP]["chave"]):
                    secondMP = l
    print(lowposition, " ", sameposition)
    if sameposition is not None:
        listOrd = compressTree(lowposition, sameposition, listOrganized)
        del listOrd[sameposition]
        del listOrd[lowposition]  
    else:
        listOrd = compressTree(lowposition, secondMP, listOrganized)
        del listOrd[secondMP]
        del listOrd[lowposition]
    return listOrd

class TreeHuffman:    
    listOrd = Organization.setlistwords(list(str(input("Digite uma série de caracteres: "))))  

    while len(listOrd) != 1:    
        listOrd = buildingTree(listOrd)
        print(listOrd)    

    # jsonOrd = json.dumps(listOrd)
    # pprint.pprint(jsonOrd)

if __name__ == "__main__":
    TreeHuffman()
    