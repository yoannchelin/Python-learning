def grouper_par_lettres(mots: list) -> dict:
    groupe = {}
    for mot in mots:
        lettres = mot[0]
        if lettres in groupe:
            groupe[lettres].append(mot)
        else:
            groupe[lettres] = [mot]
    return groupe

def compteur_mot(phrase: str) -> dict:
    phrase = phrase.lower().split()
    compteur = {}
    for mot in phrase:
       compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

def positions_mot(mots: list, cible: str) -> list:
    res = []
    for position, mot in enumerate(mots):
        if mot == cible:
            res.append(position)
    return res

print(positions_mot(["le", "chat", "le", "chien"], "le"))
# [0, 2]

print(positions_mot(["le", "chat"], "chien"))
# []