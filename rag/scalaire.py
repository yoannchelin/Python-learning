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

print(produit_scalaire_dico({"le": 2, "chat": 1}, {"le": 1, "chien": 1}) )  # 2
print(produit_scalaire_dico({"chat": 1}, {"chien": 1}) )                     # 0
print(produit_scalaire_dico({}, {"chat": 1}))                                # 0