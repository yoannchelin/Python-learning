import json

documents = [
    {"titre": "Guide Python", "contenu": "Python est un langage simple"},
    {"titre": "Recette", "contenu": "Ajouter du sel"},
    {"titre": "Intro Ia", "contenu": "Ia est en marche"},
]

with open("docs.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, ensure_ascii=False, indent=2)

with open("docs.json", "r", encoding="utf-8") as f:
    charges = json.load(f)

print(charges[0]["titre"])