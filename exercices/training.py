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
    res = {}
    texte = texte.lower().split()
    for mot in texte:
        res[mot] = res.get(mot, 0) + 1
    return res

def scalaire_dico(dico1: dict, dico2: dict) -> int:
    res = 0
    for cle in dico1:
        if cle in dico2:
            res += dico1[cle] * dico2[cle]
    return res

def norme_dico(dico: dict) -> float:
    total = 0
    for cle in dico:
        total += dico[cle] ** 2
    return total ** 0.5

def similarite_texte(texte_a: str, texte_b: str) -> float:
    texte_compte_a = compteur_mot(texte_a)
    texte_compte_b = compteur_mot(texte_b)
    value_scalaire = scalaire_dico(texte_compte_a, texte_compte_b)
    norme_a = norme_dico(texte_compte_a)
    norme_b = norme_dico(texte_compte_b)
    try:
        similarite = value_scalaire / (norme_a * norme_b)
    except ZeroDivisionError:
        return 0.0
    return round(similarite, 6)


def decouper(texte: str, taille: int, chevauchement: int) -> list:
    res = []
    if taille <= chevauchement:
        raise ValueError("argument incorrect")
    mots = texte.split()
    pas = taille - chevauchement
    for i in range(0, len(mots), pas):
        morceau = mots[i:i + taille]
        res.append(" ".join(morceau))
    return res

def meilleurs_passages(question: str, passages: list, k: int) -> list:
    score = {}
    for passage in passages:
        score[passage] = similarite_texte(question, passage)
    classement = sorted(score, key=lambda meilleur_passage: score[meilleur_passage], reverse=True)
    return classement[:k]

        

texte = "a b c d e f g h"
print(decouper(texte, 4, 1) == ["a b c d", "d e f g", "g h"])
print(decouper(texte, 4, 0) == ["a b c d", "e f g h"])
print(decouper("a b c", 10, 2) == ["a b c"])
print(decouper("", 4, 1) == [])
for cheva in (4, 6):
    try:
        decouper("a b c", 4, cheva)
        print(False)
    except ValueError:
        print(True)

passages = [
    "python est un langage de programmation",
    "le chien mange dans le jardin",
    "le chat dort sur le canape",
    "le chat mange",
]
print(meilleurs_passages("le chat dort", passages, 2) == ["le chat dort sur le canape", "le chat mange"])
print(meilleurs_passages("un langage pour programmer en python", passages, 1) == ["python est un langage de programmation"])
print(meilleurs_passages("le chat dort", passages, 4) == ["le chat dort sur le canape", "le chat mange", "le chien mange dans le jardin", "python est un langage de programmation"])
print(meilleurs_passages("le chat dort", passages, 10) == meilleurs_passages("le chat dort", passages, 4))