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

print(filtrer_titres(documents, "python"))

def diviser_securise(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return None
    
print(diviser_securise(10, 2))   # doit afficher 5.0
print(diviser_securise(10, 0))   # doit afficher None


