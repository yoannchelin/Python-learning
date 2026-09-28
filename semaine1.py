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

def chunk(texte, taille, overlap):
    mots = texte.split()
    pas = taille - overlap
    resultat = []
    for i in range(0, len(mots), pas):
        morceau = mots[i:i+taille]
        if len(morceau) < taille:
            break
        resultat.append(" ".join(morceau))
    return resultat

print(chunk("a b c d e f g", 4, 1))
