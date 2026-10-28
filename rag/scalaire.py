import string
import unicodedata


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

def compteur_mot(texte: str) -> dict:
    res = {}
    texte_sans_ponctuation = nettoyer(texte)
    texte_sans_accent = enlever_accents(texte_sans_ponctuation).split()
    texte_cleaned = enlever_mots_vides(texte_sans_accent)
    for mot in texte_cleaned:
        mot_singulier = singulier(mot)
        res[mot_singulier] = res.get(mot_singulier, 0) + 1
    return res

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
    classement = []
    for passage in passages:
       score[passage] = similarite_texte(question, passage)
       if score[passage] > 0:
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
    for lettre in texte:
        if lettre not in string.punctuation:
            res += lettre
        else:
            res += " "
    return res

MOTS_VIDES = ["le", "la", "les", "un", "une", "des", "de", "du", "en", "et", "est", "a", "l", "d", "s", "qu"]

def enlever_mots_vides(mots: list) -> list:
    res = []
    for mot in mots:
        if mot not in MOTS_VIDES:
            res.append(mot)
    return res

def enlever_accents(texte: str) -> str:
    res = ""
    texte = texte.lower()
    texte_decomposer = unicodedata.normalize('NFD', texte)
    for lettre in texte_decomposer:
        if unicodedata.category(lettre) != 'Mn':
            res += lettre
    return res

def singulier(mot: str) -> str:
    if len(mot) <= 3:
        return(mot)
    if mot.endswith("s"):
        return(mot[:-1])
    return(mot)

def construire_prompt(question: str, passages: list) -> str:
    res = "\n".join(passages)
    return f"Réponds uniquement à partir des passages ci-dessous.\nSi la réponse n'y est pas, réponds : je ne sais pas.\n   Passages:\n{res}\n\nQuestion: {question}"

