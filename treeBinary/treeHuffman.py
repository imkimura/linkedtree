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

    for l in range(0, len(listOrganized)):        
        if (listOrganized[l]["chave"] > listOrganized[lowposition]["chave"]) and (listOrganized[l]["chave"] < second) and (listOrganized[l]["chave"] != second):
            secondMP = l
            second = listOrganized[l]["chave"]
        if (listOrganized[lowposition]["chave"] == listOrganized[l]["chave"]) and (listOrganized[lowposition]["left"] != listOrganized[l]["left"]) and (listOrganized[l]["chave"] != chaveSame):
                sameposition = l 
                chaveSame = listOrganized[lowposition]["chave"]
    
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

def huffmanCod(listOrd ,listPilha, huffmanList, valoresHuffman):
    
    valoresHuffman = []

    if "left" in listOrd["left"]:
        listPilha.append('0')
        huffmanCod(listOrd["left"], listPilha, huffmanList, valoresHuffman)
        listPilha.pop()
    else:
        listPilha.append('0')
        valoresHuffman.append(listOrd["left"])
        valoresHuffman.append(("-".join(listPilha)))
        huffmanList.append(valoresHuffman)
        #print(listOrd["left"])
        listPilha.pop()
    
    valoresHuffman = []

    if "left" in listOrd["right"]:
        listPilha.append('1')
        huffmanCod(listOrd["right"], listPilha, huffmanList, valoresHuffman)
        listPilha.pop()
    else:
        listPilha.append('1')
        valoresHuffman.append(listOrd["right"])
        valoresHuffman.append(("-".join(listPilha)))
        huffmanList.append(valoresHuffman)
        #print(listOrd["right"])
        #print(listPilha)
        listPilha.pop()

    return huffmanList
#nao esquece

class TreeHuffman:    
    listOrd = Organization.setlistwords(list(str(input("Digite uma série de caracteres: "))))      
    while len(listOrd) != 1:    
        listOrd = buildingTree(listOrd)            

    listPilha = []
    huffmanList = []
    valoresHuffman = []
    huffmanList = huffmanCod(listOrd[0], listPilha, huffmanList, valoresHuffman)
    print(huffmanList)
    
    jsonOrd = json.dumps(listOrd)
    print(jsonOrd)

if __name__ == "__main__":
    TreeHuffman()
    