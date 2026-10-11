import json

def compteurs_mot(phrase: str) -> dict:
    phrase = phrase.lower().split()
    compteur = {}
    for mot in phrase:
        if mot in compteur:
            compteur[mot] = compteur[mot] + 1
        else:
            compteur[mot] = 1
    return compteur


def chunking(texte: str, taille: int, overlap: int) -> list:
    mots = texte.split()
    pas = taille - overlap
    res = []
    for i in range(0, len(mots), pas):
        morceau = mots[i:i +taille]
        if len(morceau) < taille:
            break
        else:
            res.append(" ".join(morceau))
    return res


def trouver_doublons(liste: list) -> list:
    res = []
    compteur = {}
    for nombre in liste:
        if nombre in compteur:
            compteur[nombre] = compteur[nombre] + 1
        else:
            compteur[nombre] = 1

    for cle in compteur:
        if compteur[cle] >= 2:
            print(compteur[cle])
            res.append(cle)
    return sorted(res)

def grouper_par_lettre(liste: list) -> dict:
    res = {}
    for mot in liste:
        lettre = mot[0]
        if lettre in res:
            res[lettre].append(mot)
        else:
            res[lettre] = [mot]
    return res

def open_doc(chemin: str) -> list:
    with open(chemin, 'r', encoding="utf-8") as f:
        charge = json.load(f)
    return charge 

def chercher_docs(doc: list, motcle: str) -> list:
    cle = motcle.lower()
    res = [document["titre"] for document in doc if cle in document["contenu"].lower()]
    return sorted(res)

def docs_par_longueur(documents: list) -> list:
    documents_trie = sorted(documents, key=lambda doc: len(doc["contenu"]), reverse=True)
    res = [doc["titre"] for doc in documents_trie]
    return res

print(docs_par_longueur(open_doc("docs.json")))

        
