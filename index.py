
import requests
import matplotlib.pyplot as plt
import matplotlib.image as img

pokemon = input("Enter name of pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200:
    print("pokemon not found")
    exit()


originalArt = img.imread(res.json()['sprites']['other']['official-artwork']['front_default'])

plt.title(res.json()['name'])
imgplot = plt.imshow(originalArt)
plt.show()