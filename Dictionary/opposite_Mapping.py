
"""Given a dictionary x={'k1':'v1',k2':'v2', k3':'v3'),
    create a dictionary with opposite mapping."""


x = {'k1':'v1','k2':'v2','k3':'v3'}
opposite = {}

for k,v in x.items():
    opposite[v] = k
print("\nDictionary with opposite mapping : ")
print(opposite)
