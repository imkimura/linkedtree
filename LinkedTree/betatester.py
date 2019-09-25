listOrganized = [{'right': None, 'left': 'a', 'chave': 1}, {'right': None, 'left': 'b', 'chave': 1}, {'right': None, 'left': 'c', 'chave': 1}, {'right': None, 'left': 'd', 'chave': 3}, {'right': None, 'left': 'e', 'chave': 6}, {'right': None, 'left': 'f', 'chave': 6}, {'right': None, 'left': 'j', 'chave': 12}, {'right': None, 'left': 'z', 'chave': 30}]
sameposition = None
lowposition = 0
secondMP = (len(listOrganized) - 1)
for l in range(0, len(listOrganized)):
    if listOrganized[lowposition]["chave"] > listOrganized[l]["chave"]:
        lowposition = l    
    else:
        if (listOrganized[lowposition]["chave"] == listOrganized[l]["chave"]) and (listOrganized[lowposition]["right"] != listOrganized[l]["right"]):
            sameposition = l        
        else:
            if (listOrganized[l]["chave"] > listOrganized[lowposition]["chave"]) and (listOrganized[l]["chave"] < listOrganized[secondMP]["chave"]):
                secondMP = l

print(lowposition, " ", secondMP)

if sameposition:
    freq = listOrganized[lowposition]["chave"] + listOrganized[sameposition]["chave"]
    del listOrganized[sameposition]
    del listOrganized[lowposition]
    listOrganized.append({
        "left": listOrganized[lowposition]["right"],
        "chave": freq,
        "right": listOrganized[sameposition]["right"]
    })

print(listOrganized)