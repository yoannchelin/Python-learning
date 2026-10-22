import doc
import string
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
    phrase = nettoyer(phrase).split()
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

def preparer_morceaux(documents, taille, chevauchement) -> list:
    res = []
    if chevauchement >= taille:
        raise ValueError("chevauchement trop grand")
    for docs in documents:
        morceaux = decouper(docs["contenu"], taille, chevauchement)
        res += morceaux
    return res

def mots_communs(string1: str, string2: str) -> list:
    res = []
    dico1 = compteur_mot(string1)
    dico2 = compteur_mot(string2)
    for cle in dico1:
        if cle in dico2:
            res.append(cle)
    return res

def nettoyer(texte: str) -> str:
    res = ""
    texte  = texte.lower()
    for lettres in texte:
        if lettres not in string.punctuation:
            res += lettres
    return res



if __name__ == "__main__":
    score = {}
    dico = {}
    docs = doc.open_doc("docs.json")
    morceaux = preparer_morceaux(docs, 30, 5)
    print(mots_communs("Comment le RAG transforme les documents en vecteurs ?", morceaux[4]))
    print(mots_communs("Comment le RAG transforme les documents en vecteurs ?", morceaux[5]))
    print(morceaux[4][:40])
    print(mots_communs("Comment le RAG transforme les documents en vecteurs ?", morceaux[3]))
    print(nettoyer("l'utilisateur pose une question"))
    print("a b".split())

