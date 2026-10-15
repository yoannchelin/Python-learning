def grouper_par_lettres(mots: list) -> dict:
    groupe = {}
    for mot in mots:
        lettres = mot[0]
        if lettres in groupe:
            groupe[lettres].append(mot)
        else:
            groupe[lettres] = [mot]
    return groupe



def positions_mot(mots: list, cible: str) -> list:
    res = []
    for position, mot in enumerate(mots):
        if mot == cible:
            res.append(position)
    return res

def compteur_mot(texte: str) -> dict:
    compteur = {}
    texte = texte.lower().split()
    for mot in texte:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

def produit_scalaire_dico(dico1: dict, dico2: dict) -> int:
    total = 0
    for cle in dico1:
        if cle in dico2:
            total += dico1[cle] * dico2[cle]
    return total

def norme_dico(dico: dict) -> float:
    calcul = 0
    for cle in dico:
        calcul += dico[cle] ** 2
    return calcul ** 0.5

print(produit_scalaire_dico({"le": 2, "chat": 1}, {"le": 1, "chien": 1}))   # attendu 2)