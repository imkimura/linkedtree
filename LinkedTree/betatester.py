listOrganized = [{'left': None, 'chave': 1, 'right': '1'}, {'left': None, 'chave': 3, 'right': '4'}, {'left': None, 'chave': 2, 'right': '2'}, {'left': None, 'chave': 4, 'right': '5'}]
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