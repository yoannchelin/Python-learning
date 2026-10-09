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

print(similarite_cosinus([1, 0], [1, 0]))    # 1.0
print(similarite_cosinus([1, 0], [0, 1]))    # 0.0
print(similarite_cosinus([1, 2], [2, 4]))    # 1.0 (même direction, longueur différente)
print(similarite_cosinus([0, 0], [1, 0]))    # 0.0 (ne doit pas planter)
print(round(similarite_cosinus([1, 2], [2, 4]), 6))   # 1.0
