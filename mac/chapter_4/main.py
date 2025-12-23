import requests

r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = r.json()

print(data)

from Bio.Seq import Seq

print("Translating DNA to protein")
dna = Seq("ATGGCTGACCTGTTCAAGGACGCTATCGAGTTCGAGCTGACCAAGTGGGACCTG")
print(dna.translate())

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
