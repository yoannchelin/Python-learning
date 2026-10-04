def double(liste):
    num = []
    for x in liste:
        num.append(x * 2)
    return num

def countWords(phrase):
    count = phrase.split()
    return len(count)

def age():
    personnes = {}
    personnes["Léa"] = 25
    personnes["Tom"] = 18
    personnes["Nora"] = 22
    resultat = []
    for nom in personnes:
        if personnes[nom] > 20:
            resultat.append((nom, personnes[nom]))
    return(resultat)

def compteurs_de_mot(phrase):
    phrase = phrase.lower()
    mots = phrase.split()
    compteurs = {}
    for mot in mots:
        if mot in compteurs:
            compteurs[mot] = compteurs[mot] + 1
        else:
            compteurs[mot] = 1
    return compteurs

def chunk(texte: str, taille: int, overlap: int) -> list:
    mots = texte.split()
    pas = taille - overlap
    resultat = []
    for i in range(0, len(mots), pas):
        morceau = mots[i:i+taille]
        if len(morceau) < taille:
            break
        resultat.append(" ".join(morceau))
    return resultat

class Documents:
    def __init__(self, titre: str, contenu: str):
        self.titre = titre
        self.contenu = contenu
    def contient(self, motcle: str) -> bool:
        return motcle.lower() in self.contenu.lower()
    
documents = [
    Documents("Guide Python", "Python est un langage simple"),
    Documents("Recette", "Ajouter du sel et du poivre"),
    Documents("Intro IA", "Python est utilisé en intelligence artificielle"),
]

def filtrer_titres(documents, motcle):
    res = []
    for doc in documents:
        if doc.contient(motcle):   
            res.append(doc.titre)        
    return sorted(res)


def diviser_securise(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return None
    
def inverser_mots(phrase: str) -> str:
    mots = phrase.split()
    return " ".join(mots[::-1])

def moyenne(nombres: list) -> float:
    try:
        total = sum(nombres)
        return total / len(nombres)
    except ZeroDivisionError:
        return 0

def fusionner(dico1, dico2):
    temp = dico1.copy()
    for x in dico2:
        if x in temp:
            temp[x] = temp[x] + dico2[x]
        else:
            temp[x] = 1
    return temp

class Panier:
    def __init__(self):
        self.paniers = []
    
    def ajouter(self, nom: str, prix: float):
        self.paniers.append({"nom": nom, "prix": prix})

    def total(self) -> float:
        prix_liste = []
        for article in self.paniers:
            prix_liste.append(article["prix"])
        return sum(prix_liste)
    
    def plus_cher(self) -> str:
        meilleur_prix = 0
        meilleur_nom = None
        for article in self.paniers:
            if article["prix"] > meilleur_prix:
                meilleur_prix = article["prix"]
                meilleur_nom = article["nom"]
        return meilleur_nom

def trouver_doublons(liste: list) -> list:
    compteurs = {}
    res = []
    for x in liste:
        if x in compteurs:
            compteurs[x] = compteurs[x] + 1
        else:
            compteurs[x] = 1

    for cle in compteurs:
        if compteurs[cle] >= 2:
            res.append(cle)
    return sorted(res)

def grouper_par_lettres(liste: list) -> dict:
    groupe = {}
    for mot in liste:
        if mot[0] in groupe:
            groupe[mot[0]].append(mot)
        else:
            groupe[mot[0]] = [mot]
    return groupe




print(grouper_par_lettres(["chat", "chien", "banane", "cheval", "avion"]))