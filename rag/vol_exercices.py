# =============================================================================
#  EXERCICES DE VOL — sans internet, sans Claude, sans ouvrir ton dossier rag/
# =============================================================================
#
#  Comment ça marche :
#  1. Tu écris tes fonctions dans la zone « TON CODE ICI » (plus bas).
#  2. Tu lances les tests d'un bloc :   python3 vol_exercices.py 1
#                                        python3 vol_exercices.py 2
#                                        python3 vol_exercices.py 3
#  3. Chaque test affiche OK ou FAUX, ou le nom de l'erreur.
#     « pas encore écrite » = la fonction n'existe pas encore, c'est normal.
#
#  Les règles habituelles :
#  - une phrase en français (en commentaire) avant chaque fonction ;
#  - le chrono s'arrête quand tous les tests du bloc sont OK ;
#  - si tu bloques 10 minutes : indices à la fin de vol_guide.md.
#
# =============================================================================

import string
import unicodedata
import sqlite3

MOTS_VIDES = ["le", "la", "les", "un", "une", "des", "de", "du", "en", "et",
              "est", "a", "l", "d", "s", "qu"]

def nettoyer(texte: str) -> str:
    res = ""
    texte = texte.lower()
    for lettre in texte:
        if lettre in string.punctuation:
            res += " "
        else:
            res += lettre
    return res

def enlever_accents(texte: str):
    res = ""
    mot_normalize = unicodedata.normalize('NFD', texte)
    for lettre in mot_normalize:
        if unicodedata.category(lettre) != 'Mn':
            res += lettre
    return res

def enlever_mots_vides(mots: list) -> list:
    res = []
    for mot in mots:
        if mot not in MOTS_VIDES:
            res.append(mot)
    return res

def singulier(mot: str) -> str:
    if len(mot) <= 3:
        return mot
    if mot.endswith('s'):
        return mot[:-1]
    return mot

def compteur_mot(texte: str) -> dict:
    res = {}
    texte_nettoyer = nettoyer(texte)
    texte_sans_accents = enlever_accents(texte_nettoyer).split()
    texte_mot_vide = enlever_mots_vides(texte_sans_accents)
    for mot in texte_mot_vide:
        mot_singulier = singulier(mot)
        res[mot_singulier] = res.get(mot_singulier, 0) + 1
    return res

def produit_scalaire_dico(dict1: dict, dict2: dict) -> float:
    res = 0
    for cle in dict1:
        if cle in dict2:
            res += dict1[cle] * dict2[cle]
    return res

def norme_dico(dico: dict) -> float:
    res = 0
    for cle in dico:
        res += dico[cle] ** 2
    return res ** 0.5

def similarite_texte(texte_a: str, texte_b: str) -> float:
    texte_a = compteur_mot(texte_a)
    texte_b = compteur_mot(texte_b)
    norme_a = norme_dico(texte_a)
    norme_b = norme_dico(texte_b)
    produit = produit_scalaire_dico(texte_a, texte_b)
    try:
        res = produit / (norme_a * norme_b)
    except ZeroDivisionError:
        return(0.0)
    return round(res, 6)

def meilleurs_passages(question: str, passages: list, k: int) -> list:
    res = {}
    score = 0
    for passage in passages:
        score = similarite_texte(question, passage)
        if score > 0:
            res[passage] = score
    classement = sorted(res, key=lambda meilleur: res[meilleur], reverse=True)
    return classement[:k]

print(meilleurs_passages("chat", ["le chien mange", "le chat dort"], 3) == ["le chat dort"])



# =============================================================================
#  BLOC 1 — Warm-up : ta chaîne RAG, de mémoire (30 à 40 min)
# =============================================================================
#
#  Réécris, sans regarder ton ancien code :
#
#  nettoyer(texte) -> str
#      minuscules, chaque signe de ponctuation remplacé par un espace
#
#  enlever_accents(texte) -> str
#      "transformé" -> "transforme" (unicodedata, NFD, catégorie "Mn")
#
#  enlever_mots_vides(mots: list) -> list
#      garde les mots qui ne sont pas dans MOTS_VIDES
#
#  singulier(mot) -> str
#      enlève le "s" final si le mot a plus de 3 lettres
#
#  compteur_mot(texte) -> dict
#      nettoyer -> enlever_accents -> split -> enlever_mots_vides
#      -> singulier sur chaque mot, puis comptage
#
#  similarite_texte(texte_a, texte_b) -> float
#      similarité cosinus des deux compteurs, arrondie à 6 décimales,
#      0.0 si une norme vaut 0 (écris tes fonctions scalaire / norme si besoin)
#
#  meilleurs_passages(question, passages, k) -> list
#      les k passages les plus proches, en ignorant ceux dont le score vaut 0
#
# =============================================================================


# =============================================================================
#  BLOC 2 — Une classe Stock (POO), comme ton WMS de Perth (40 à 50 min)
# =============================================================================
#
#  Les offres VIE (SII notamment) demandent la programmation orientée objet.
#  Tu vas écrire une petite classe qui gère un stock, avec ce que tu as
#  automatisé chez John Building Supplies : achats et ventes.
#
#  class Stock
#
#  - à la création, le stock est vide (un dictionnaire {reference: quantite})
#
#  - ajouter(reference, quantite)
#      ajoute la quantité ; lève ValueError("...") si quantite <= 0
#
#  - retirer(reference, quantite)
#      retire la quantité ; lève ValueError("...") si quantite <= 0,
#      si la référence n'existe pas, ou si le stock est insuffisant
#      (dans ce cas, le stock ne doit PAS changer)
#
#  - quantite(reference) -> int
#      la quantité en stock, 0 si la référence est inconnue
#
#  - appliquer(mouvements: list)
#      chaque mouvement est un tuple (type, reference, quantite)
#      type "achat" -> ajouter ; type "vente" -> retirer
#      tout autre type -> ValueError
#
#  - en_rupture(seuil) -> list
#      les références dont la quantité est strictement inférieure au seuil,
#      triées par ordre alphabétique
#
#  Rappel : chaque méthode reçoit self en premier paramètre, et le
#  dictionnaire se crée dans __init__ (carnet, section 7).
#
# =============================================================================


# =============================================================================
#  BLOC 3 — SQL avec sqlite3 (inclus dans Python, marche hors ligne) (40 min)
# =============================================================================
#
#  La base est créée pour toi par creer_base() (plus bas, ne la modifie pas).
#  Tables :
#      produits(id, nom, categorie)
#      mouvements(id, produit_id, type, quantite)   type = 'achat' ou 'vente'
#
#  Pour chaque question, écris UNE requête SQL dans la variable indiquée
#  (une chaîne de caractères). Le test l'exécute et compare le résultat.
#  Pour essayer une requête : print(executer(REQUETE_1))
#
#  REQUETE_1 : le nom de tous les produits, triés par nom (A -> Z)
#  REQUETE_2 : le nom des produits de la catégorie 'bois', triés par nom
#  REQUETE_3 : pour chaque produit_id, la quantité totale ACHETÉE,
#              triée par produit_id                      (GROUP BY, SUM)
#  REQUETE_4 : la même chose, mais avec le NOM du produit au lieu de son id,
#              triée par nom                             (JOIN)
#  REQUETE_5 (bonus) : pour chaque nom de produit, le stock
#              = total acheté - total vendu, trié par nom
#              (indice : SUM(CASE WHEN ... THEN ... ELSE ... END))
#
#  C'est exactement le calcul que tu as automatisé à Perth, en SQL.
#
# =============================================================================


# ----------------------------------------------------------------------------
#  TON CODE ICI (blocs 1, 2 et 3)
# ----------------------------------------------------------------------------






REQUETE_1 = ""
REQUETE_2 = ""
REQUETE_3 = ""
REQUETE_4 = ""
REQUETE_5 = ""


# =============================================================================
#  NE PAS MODIFIER EN DESSOUS : outils de test et base SQL
# =============================================================================

def creer_base():
    con = sqlite3.connect(":memory:")
    con.executescript("""
        CREATE TABLE produits (id INTEGER PRIMARY KEY, nom TEXT, categorie TEXT);
        CREATE TABLE mouvements (id INTEGER PRIMARY KEY, produit_id INTEGER,
                                 type TEXT, quantite INTEGER);
        INSERT INTO produits VALUES (1, 'Vis inox 5mm', 'quincaillerie');
        INSERT INTO produits VALUES (2, 'Planche pin 2m', 'bois');
        INSERT INTO produits VALUES (3, 'Ciment 25kg', 'maconnerie');
        INSERT INTO produits VALUES (4, 'Contreplaque 10mm', 'bois');
        INSERT INTO mouvements VALUES (1, 1, 'achat', 500);
        INSERT INTO mouvements VALUES (2, 1, 'vente', 120);
        INSERT INTO mouvements VALUES (3, 2, 'achat', 40);
        INSERT INTO mouvements VALUES (4, 2, 'vente', 15);
        INSERT INTO mouvements VALUES (5, 2, 'vente', 10);
        INSERT INTO mouvements VALUES (6, 3, 'achat', 60);
        INSERT INTO mouvements VALUES (7, 1, 'achat', 100);
        INSERT INTO mouvements VALUES (8, 4, 'achat', 20);
        INSERT INTO mouvements VALUES (9, 4, 'vente', 20);
    """)
    return con


def executer(requete):
    con = creer_base()
    try:
        return con.execute(requete).fetchall()
    finally:
        con.close()


def check(label, test):
    try:
        resultat = test()
        print(("OK    " if resultat else "FAUX  ") + label)
    except NameError as e:
        print("----  " + label + "  (nom inconnu : " + str(e).split("'")[1]
              + " -> pas encore écrite, ou faute de nom dans ton code)")
    except Exception as e:
        print("ERR   " + label + "  (" + type(e).__name__ + ": " + str(e) + ")")


def leve(exception, fonction):
    try:
        fonction()
    except exception:
        return True
    return False


def bloc1():
    check("nettoyer ponctuation", lambda: nettoyer("Le RAG, pour Retrieval!").split() == ["le", "rag", "pour", "retrieval"])
    check("nettoyer apostrophe", lambda: nettoyer("l'utilisateur pose").split() == ["l", "utilisateur", "pose"])
    check("nettoyer vide", lambda: nettoyer("") == "")
    check("accents", lambda: enlever_accents("où ça à été") == "ou ca a ete")
    check("accents vide", lambda: enlever_accents("") == "")
    check("mots vides", lambda: enlever_mots_vides(["le", "chat", "dort"]) == ["chat", "dort"])
    check("mots vides tous", lambda: enlever_mots_vides(["le", "les"]) == [])
    check("singulier pluriel", lambda: singulier("documents") == "document")
    check("singulier court", lambda: singulier("pas") == "pas")
    check("singulier vide", lambda: singulier("") == "")
    check("compteur chaîne complète", lambda: compteur_mot("Transformé en vecteurs") == {"transforme": 1, "vecteur": 1})
    check("compteur ponctuation + mots vides", lambda: compteur_mot("Le chat, le!") == {"chat": 1})
    check("compteur pluriel cumulé", lambda: compteur_mot("Documents document") == {"document": 2})
    check("compteur vide", lambda: compteur_mot("") == {})
    check("similarité identique", lambda: similarite_texte("le chat dort", "le chat dort") == 1.0)
    check("similarité aucun mot commun", lambda: similarite_texte("chat", "chien") == 0.0)
    check("similarité texte vide", lambda: similarite_texte("", "chat") == 0.0)
    check("similarité arrondie", lambda: similarite_texte("python chat", "python est un langage") == 0.5)
    passages = ["le chat dort sur le canape", "python est un langage", "le chien mange"]
    check("meilleurs k=3 un seul utile", lambda: meilleurs_passages("chat", passages, 3) == ["le chat dort sur le canape"])
    check("meilleurs rien de pertinent", lambda: meilleurs_passages("xyz", passages, 3) == [])
    check("meilleurs k=1", lambda: meilleurs_passages("python chat", passages, 1) == ["python est un langage"])
    check("meilleurs ordre", lambda: meilleurs_passages("python chat", passages, 3) == ["python est un langage", "le chat dort sur le canape"])


def bloc2():
    def nouveau():
        s = Stock()
        s.ajouter("VIS", 100)
        return s
    check("stock vide au départ", lambda: Stock().quantite("VIS") == 0)
    check("ajouter", lambda: nouveau().quantite("VIS") == 100)
    def ajouter_deux_fois():
        s = nouveau()
        s.ajouter("VIS", 50)
        return s.quantite("VIS") == 150
    check("ajouter cumule", ajouter_deux_fois)
    check("ajouter quantité nulle -> ValueError", lambda: leve(ValueError, lambda: Stock().ajouter("VIS", 0)))
    def retirer_ok():
        s = nouveau()
        s.retirer("VIS", 30)
        return s.quantite("VIS") == 70
    check("retirer", retirer_ok)
    check("retirer référence inconnue -> ValueError", lambda: leve(ValueError, lambda: Stock().retirer("CLOU", 1)))
    check("retirer trop -> ValueError", lambda: leve(ValueError, lambda: nouveau().retirer("VIS", 101)))
    def stock_intact():
        s = nouveau()
        try:
            s.retirer("VIS", 101)
        except ValueError:
            pass
        return s.quantite("VIS") == 100
    check("retirer trop : stock inchangé", stock_intact)
    check("retirer négatif -> ValueError", lambda: leve(ValueError, lambda: nouveau().retirer("VIS", -5)))
    def appliquer_ok():
        s = Stock()
        s.appliquer([("achat", "VIS", 500), ("vente", "VIS", 120), ("achat", "PIN", 40),
                     ("vente", "PIN", 25), ("achat", "VIS", 100)])
        return s.quantite("VIS") == 480 and s.quantite("PIN") == 15
    check("appliquer achats et ventes", appliquer_ok)
    check("appliquer type inconnu -> ValueError", lambda: leve(ValueError, lambda: Stock().appliquer([("vol", "VIS", 1)])))
    def rupture():
        s = Stock()
        s.appliquer([("achat", "VIS", 480), ("achat", "PIN", 15), ("achat", "CIMENT", 60),
                     ("achat", "CP", 20), ("vente", "CP", 20)])
        return s.en_rupture(20) == ["CP", "PIN"]
    check("en_rupture triée", rupture)
    check("en_rupture stock vide", lambda: Stock().en_rupture(10) == [])


def bloc3():
    check("REQUETE_1 tri par nom", lambda: executer(REQUETE_1) == [
        ("Ciment 25kg",), ("Contreplaque 10mm",), ("Planche pin 2m",), ("Vis inox 5mm",)])
    check("REQUETE_2 catégorie bois", lambda: executer(REQUETE_2) == [
        ("Contreplaque 10mm",), ("Planche pin 2m",)])
    check("REQUETE_3 total acheté par id", lambda: executer(REQUETE_3) == [
        (1, 600), (2, 40), (3, 60), (4, 20)])
    check("REQUETE_4 total acheté par nom", lambda: executer(REQUETE_4) == [
        ("Ciment 25kg", 60), ("Contreplaque 10mm", 20), ("Planche pin 2m", 40), ("Vis inox 5mm", 600)])
    check("REQUETE_5 stock (bonus)", lambda: executer(REQUETE_5) == [
        ("Ciment 25kg", 60), ("Contreplaque 10mm", 0), ("Planche pin 2m", 15), ("Vis inox 5mm", 480)])


if __name__ == "__main__":
    import sys
    blocs = {"1": bloc1, "2": bloc2, "3": bloc3}
    choix = sys.argv[1:] or ["1", "2", "3"]
    for numero in choix:
        print(f"\n===== BLOC {numero} =====")
        blocs[numero]()
