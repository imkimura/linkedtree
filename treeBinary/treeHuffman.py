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
    chaveSame = 10000000000000000000
    secondMP = len(listOrganized) - 1
    second = 100000000000000000
    for l in range(0, len(listOrganized)):
        if listOrganized[lowposition]["chave"] > listOrganized[l]["chave"]:
            lowposition = l    
        else:
            if (listOrganized[lowposition]["chave"] == listOrganized[l]["chave"]) and (listOrganized[lowposition]["left"] != listOrganized[l]["left"]) and (listOrganized[l]["chave"] != chaveSame):
                sameposition = l 
                chaveSame = listOrganized[lowposition]["chave"]                  
    for l in range(0, len(listOrganized)):        
        if (listOrganized[l]["chave"] > listOrganized[lowposition]["chave"]) and (listOrganized[l]["chave"] < second) and (listOrganized[l]["chave"] != second):
            secondMP = l
            second = listOrganized[l]["chave"]
    print(lowposition, " ", sameposition, " ", secondMP)
    if sameposition is not None:        
        listOrd = compressTree(lowposition, sameposition, listOrganized)
        del listOrd[sameposition]
        del listOrd[lowposition]  
    else:
        if lowposition > secondMP:
            aux = secondMP
            secondMP = lowposition
            lowposition = aux
        listOrd = compressTree(lowposition, secondMP, listOrganized)
        del listOrd[secondMP]
        del listOrd[lowposition]
    return listOrd

class TreeHuffman:    
    listOrd = Organization.setlistwords(list(str(input("Digite uma série de caracteres: "))))  

    while len(listOrd) != 1:    
        listOrd = buildingTree(listOrd)
        print(listOrd)    

    jsonOrd = json.dumps(listOrd)
    pprint.pprint(jsonOrd)

if __name__ == "__main__":
    TreeHuffman()
    