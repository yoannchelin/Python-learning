def produit_scalaire(a: list, b: list) -> float:
    total = 0
    for x,y in zip(a,b):
        scalaire = x * y
        total += scalaire
    return total

def norme(vecteur: list) -> float:
    res = 0
    somme = 0
    for x in vecteur:
        carre = x ** 2
        somme += carre
    res += somme ** 0.5
    return res

def similarite_cosinus(a: list, b: list) -> float:
    produit = produit_scalaire(a, b)
    norme_a = norme(a)
    norme_b = norme(b)
    try:
        res = produit / (norme_a * norme_b)
    except ZeroDivisionError:
        return(0.0)

    return res

def produit_scalaire_dico(dico1: dict, dico2: dict) -> float:
    total = 0
    for cle in dico1:
        if cle in dico2:
            total += dico1[cle] * dico2[cle]
    return total

def norme_dico(dico: dict) -> float:
    somme_carres = 0
    for cle in dico:
        somme_carres += dico[cle] ** 2
    return somme_carres ** 0.5

def compteur_mot(phrase: str) -> dict:
    phrase = phrase.lower().split()
    compteur = {}
    for mot in phrase:
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

def similarite_texte(texte1: str, texte2: str) -> float:
    texte1_compter = compteur_mot(texte1)
    texte2_compter = compteur_mot(texte2)
    scalaire_text = produit_scalaire_dico(texte1_compter, texte2_compter)
    norme_1 = norme_dico(texte1_compter)
    norme_2 = norme_dico(texte2_compter)
    try:
        res = scalaire_text / (norme_1 * norme_2)
    except ZeroDivisionError:
        return 0.0
    return round(res, 6)

passages = [
    "python est un langage de programmation",
    "le chien mange dans le jardin",
    "le chat dort sur le canape",
    "le chat mange",
]

def meilleurs_passages(question: str, passages: list, k: int) -> list:
    score = {}
    for passage in passages:
       score[passage] = similarite_texte(question, passage)
    classement =  sorted(score, key=lambda meilleur_passage: score[meilleur_passage], reverse=True)
    return classement[:k]

def decouper(texte: str, taille: int, chevauchement: int) -> list:
    res = []
    if chevauchement >= taille:
        raise ValueError
        
    mots = texte.split()
    pas = taille - chevauchement
    for i in range(0, len(mots), pas):
        morceau = mots[i:i+taille]
        res.append(" ".join(morceau))
    return res

def preparer_morceaux(documents: list, taille: int, chevauchement: int) -> list:
    res = []
    if chevauchement >= taille:
        raise ValueError("chevauchement trop grand")
    for document in documents:
        morceaux = decouper(document["contenu"], taille, chevauchement)
        res += morceaux
    return res
        


documents = [
    {"titre": "Chats", "contenu": "le chat dort sur le canape toute la journee"},
    {"titre": "Python", "contenu": "python est un langage de programmation simple"},
]
attendu = [
    "le chat dort sur",
    "sur le canape toute",
    "toute la journee",
    "python est un langage",
    "langage de programmation simple",
    "simple",
]
res = preparer_morceaux(documents, 4, 1)
print(res == attendu)
print(res)
print(preparer_morceaux([], 4, 1) == [])

morceaux = preparer_morceaux(documents, 4, 1)
print(meilleurs_passages("chat", morceaux, 1) == ["le chat dort sur"])
print(meilleurs_passages("langage de programmation", morceaux, 1) == ["langage de programmation simple"])