# Carnet de pièges Python

Mes erreurs récurrentes en apprenant Python (venant de JS/TS), avec la version fausse, la version juste et le réflexe à avoir.

---

## La méthode : le tableau

Avant d'écrire une boucle, je déroule un petit exemple à la main : à chaque tour, que vaut chaque variable ?

```
mots = ["chat", "chien", "banane"]

mot = "chat"    -> lettre "c" -> "c" pas dans groupe -> groupe = {"c": ["chat"]}
mot = "chien"   -> lettre "c" -> "c" dans groupe     -> groupe = {"c": ["chat", "chien"]}
mot = "banane"  -> lettre "b" -> "b" pas dans groupe -> groupe = {"c": [...], "b": ["banane"]}
```

Quand je bloque : je fais le tableau, je lis la **dernière ligne du traceback**, et je `print(type(x))` ou `print(len(x))` pour voir ce que contient une variable.

---

## 1. Syntaxe

### 1.1 `{}` vs `[]` : liste ou set ?

```python
# Faux : des accolades sans ":" créent un set, pas une liste
res.append({nom, prix})
groupe[lettre] = {mot}

# Juste
res.append({"nom": nom, "prix": prix})   # dictionnaire (avec ":")
groupe[lettre] = [mot]                   # liste (crochets)
```

### 1.2 Parenthèses oubliées sur une méthode

```python
# Faux : on stocke la méthode elle-même, pas son résultat
mots = phrase.split
note.nombre_mots

# Juste
mots = phrase.split()
note.nombre_mots()
```

### 1.3 Crochets (dictionnaire) vs point (objet)

```python
# Dictionnaire (ex : donnée venant d'un JSON) -> crochets
doc["titre"]

# Objet d'une classe -> point
note.titre
```

### 1.4 Guillemets autour d'une variable

```python
# Faux : écrit littéralement le texte m-o-t
res.append("titre")
groupe[lettre] = ["mot"]

# Juste : la variable, sans guillemets
res.append(doc["titre"])
groupe[lettre] = [mot]
```

### 1.5 Résultat d'une méthode non stocké

Les chaînes sont immuables : `.lower()` et `.split()` renvoient un **nouveau** résultat.

```python
# Faux : le résultat part dans le vide
phrase.lower()

# Juste
phrase = phrase.lower()
```

### 1.6 `\n` et non `/n`

```python
print("ligne 1\nligne 2")   # deux lignes (backslash)
print("ligne 1/nligne 2")   # une ligne avec "/n" visible
```

### 1.7 Appeler une fonction : les parenthèses

```python
print(ma_fonction)        # affiche la fonction elle-même
print(ma_fonction(arg))   # affiche son résultat
```

### 1.8 `return` sans parenthèses

```python
return num      # juste
return(num)     # marche, mais inutile
```

### 1.9 Noms en snake_case

```python
norme_a = norme(a)     # juste
normeA = norme(a)      # style JavaScript, pas Python
```

### 1.10 Flottants : ne jamais comparer au caractère près

```python
0.1 + 0.2             # 0.30000000000000004
```

Pour afficher ou tester un résultat décimal, j'arrondis :

```python
round(0.9999999999999998, 6)   # 1.0
```

### 1.11 Enchaîner les méthodes : l'ordre compte

```python
# Faux : .split() renvoie une LISTE, et une liste n'a pas de .lower()
mots = phrase.split().lower()      # AttributeError: 'list' object has no attribute 'lower'

# Juste : .lower() sur la chaîne d'abord, .split() ensuite
mots = phrase.lower().split()
```

Je lis de gauche à droite et je me demande à chaque étape : "qu'est-ce que j'ai dans les mains ?" (une chaîne, puis une liste).

### 1.12 Carré et racine carrée

```python
3 ** 2        # 9    : au carré
25 ** 0.5     # 5.0  : racine carrée (puissance 1/2)
```

- Le résultat d'une racine est un **float** : `-> float`, pas `-> int`.
- La racine se calcule **une fois, après la boucle** (sur la somme complète), jamais dedans :

```python
# Faux : la racine est recalculée à chaque tour (le résultat final est juste, le code est confus)
for cle in dico:
    carre += dico[cle] ** 2
    total = carre ** 0.5

# Juste : une seule variable, la racine à la fin
somme_carres = 0
for cle in dico:
    somme_carres += dico[cle] ** 2
return somme_carres ** 0.5
```

Version une ligne : `return sum(valeur ** 2 for valeur in dico.values()) ** 0.5`

---

## 2. Boucles

### 2.1 Ce que donne `for x in ...`

Le nom de la variable ne dit rien, c'est ce qu'il y a après `in` qui décide.

| Boucle | La variable vaut |
|---|---|
| `for c in "abc"` | un **caractère** |
| `for mot in ["ab", "cd"]` | un **élément** |
| `for i in range(0, 7, 3)` | une **position** (0, 3, 6) |
| `for cle in {"a": 1}` | une **clé** |

Boucler sur une chaîne donne des caractères : il faut d'abord `.split()` pour avoir des mots.

### 2.2 Bien nommer la variable de boucle

`i` seulement pour `range`. Sinon, un nom qui dit ce que je reçois :

```python
for mot in mots:
for doc in documents:
for note in notes:
for cle in compteur:
```

### 2.3 Besoin de l'élément ou de la position ?

```python
# Pas besoin de la position -> boucle directe
for x in liste:
    res.append(x * 2)

# Besoin de la position (avancer par sauts) -> range
for i in range(0, len(mots), pas):
    morceau = mots[i:i+taille]
```

### 2.4 `range(debut, fin, pas)` : `fin` est exclu

```python
list(range(0, 7, 3))   # [0, 3, 6], jamais 7
```

Pas de `-1` à ajouter : `range(0, len(mots), pas)` suffit.

### 2.5 Slice : le deuxième nombre est exclu

```python
lettres = ["a", "b", "c", "d", "e", "f", "g"]
lettres[0:4]    # ['a', 'b', 'c', 'd']
lettres[3:7]    # ['d', 'e', 'f', 'g']
lettres[6:10]   # ['g'] (Python ne plante pas, il donne ce qu'il reste)
lettres[::-1]   # liste inversée
```

### 2.6 Fenêtre : `mots[i:i+taille]`

```python
# Faux : toujours le début de la liste après le premier tour
morceau = mots[i:taille]

# Juste : à partir de i, sur "taille" éléments
morceau = mots[i:i+taille]
```

Je vérifie avec i = 0 puis i = 3 : la fenêtre doit glisser.

### 2.7 `enumerate` : la position ET l'élément

```python
for position, mot in enumerate(["le", "chat", "le"]):
    ...                       # 0 "le" / 1 "chat" / 2 "le"
```

- La virgule va **avant** le `in`, pas après (`for position in cible, enumerate(...)` crée un couple).
- Deux noms avant le `in`, un pour chaque information.

### 2.8 Compréhension de liste

```python
# boucle classique
res = []
for document in documents:
    res.append(document["titre"])

# compréhension : [ce que je garde  for  élément  in  source  if  condition]
res = [document["titre"] for document in documents]
res = [document["titre"] for document in documents if cle in document["contenu"].lower()]
```

- Pas de virgule entre l'expression et le `for`.
- Elle remplace une boucle `for ... append` simple. Dès qu'il y a un `if/else` avec deux actions différentes (comme le groupement), je garde la boucle.

### 2.9 Une variable de boucle ne porte jamais le nom d'un paramètre

```python
# Faux : "cible" est écrasée à chaque tour, je ne sais plus ce que je cherchais
def positions_mot(mots, cible):
    for position, cible in enumerate(mots):
        ...

# Juste : un nom différent, qui dit ce que la variable contient
    for position, mot in enumerate(mots):
```

### 2.10 `join` : une liste de chaînes devient une chaîne

```python
mots = ["le", "chat", "dort"]
" ".join(mots)        # "le chat dort" : ce qui est avant le point sépare les mots

# Faux : .append renvoie None, et res[morceau] = ... utilise une liste comme numéro de case
res[morceau] = " ".join(res.append(morceau))

# Juste : deux lignes séparées, dans l'ordre
texte_morceau = " ".join(morceau)
res.append(texte_morceau)
```

- `join` prend une **liste de chaînes** et renvoie **une seule chaîne**.
- Je n'imbrique jamais `.append` dans un autre appel : il renvoie `None`.
- Une liste s'indexe avec un nombre (`res[0]`), jamais avec une autre liste.

---

## 3. Return, print et accumulation

### 3.1 `return` arrête la fonction immédiatement

```python
# Faux : renvoie au premier élément trouvé
for nom in personnes:
    if personnes[nom] > 20:
        return nom

# Juste : j'accumule, puis je renvoie APRÈS la boucle
res = []
for nom in personnes:
    if personnes[nom] > 20:
        res.append(nom)
return res          # désindenté, au niveau du for
```

### 3.2 `print` affiche, `return` renvoie

Une fonction qui renvoie un résultat n'a pas de `print` à l'intérieur. Sinon on affiche deux fois, ou on obtient `None`.

### 3.3 `.append()` renvoie `None`

```python
# Faux
return res.append(x)

# Juste
res.append(x)
return res
```

### 3.4 `.append()` prend UN seul argument

```python
# Faux
liste.append(nom, prix)

# Juste : un seul élément qui regroupe les deux
liste.append({"nom": nom, "prix": prix})
```

### 3.5 Ne pas écraser l'accumulateur

```python
# Faux : res devient une chaîne, plus une liste
res = " ".join(morceau)

# Juste
res.append(" ".join(morceau))
```

### 3.6 `sorted` renvoie une nouvelle liste : je la stocke

```python
# Faux : le résultat part dans le vide
sorted(documents, key=lambda doc: len(doc["contenu"]))

# Juste
documents_tries = sorted(documents, key=lambda doc: len(doc["contenu"]), reverse=True)
```

- `key=` prend une fonction qui dit **sur quoi comparer** : je ne cherche pas la position moi-même.
- `reverse=True` pour l'ordre décroissant.
- `len(un_dictionnaire)` compte les **clés**, pas le texte d'un champ : j'écris `len(doc["contenu"])`.

### 3.7 `key=lambda` et `reverse=True`

Un `lambda` est une mini-fonction sans nom : `lambda <ce que je reçois> : <ce que je renvoie>`. `sorted` l'appelle une fois par élément et trie selon le nombre renvoyé.

```python
mots = ["chat", "elephant", "a"]
sorted(mots, key=lambda mot: len(mot))                 # ['a', 'chat', 'elephant']
sorted(mots, key=lambda mot: len(mot), reverse=True)   # ['elephant', 'chat', 'a']
```

- Par défaut `sorted` va du plus petit au plus grand. `reverse=True` inverse l'ordre.
- Sans `reverse=True`, `[:k]` garderait les `k` **plus mauvais** éléments.
- Le nom du paramètre du lambda dit ce qu'il **reçoit** (un passage, un mot), pas ce qu'il renvoie.

### 3.8 Trier un dictionnaire selon ses valeurs (passage = clé, score = valeur)

```python
# Faux : "score" est écrasé à chaque tour, il ne reste que le dernier
for passage in passages:
    score = similarite_texte(question, passage)

# Juste : un contenant créé AVANT la boucle, une entrée par passage
scores = {}
for passage in passages:
    scores[passage] = similarite_texte(question, passage)
classement = sorted(scores, key=lambda passage: scores[passage], reverse=True)
return classement[:k]
```

- `sorted(dico)` trie les **clés** et renvoie une **liste**.
- Le passage est la clé car il est **unique** : deux passages différents peuvent avoir le même score, et deux scores identiques se seraient écrasés.
- `liste[:k]` garde les `k` premiers et ne plante pas si `k` dépasse la taille.
- Un paramètre jamais utilisé (ici `k`) est presque toujours un oubli.

---

## 4. Dictionnaires

### 4.1 Boucle sur un dico = je reçois les clés

```python
compteur = {5: 3, 1: 2, 6: 1}

for cle in compteur:
    if compteur[cle] >= 2:    # la condition regarde la VALEUR
        res.append(cle)       # le résultat prend la CLÉ
```

Règle : **la condition regarde `compteur[cle]`, le `append` prend `cle`.**

### 4.2 Ajouter une clé sans écraser le dico

```python
# Faux : le dictionnaire est remplacé par le nombre 1
else:
    compteur = 1

# Juste
else:
    compteur[mot] = 1
```

### 4.3 Le pattern compteur

```python
compteur = {}
for mot in mots:
    if mot in compteur:
        compteur[mot] = compteur[mot] + 1
    else:
        compteur[mot] = 1
```

`if mot in compteur` teste le **dictionnaire**, jamais la liste d'origine (le mot y est toujours).

### 4.4 Le pattern groupement (valeur = liste qui grandit)

```python
groupes = {}
for mot in mots:
    lettre = mot[0]
    if lettre in groupes:
        groupes[lettre].append(mot)   # la liste existe : elle grandit
    else:
        groupes[lettre] = [mot]       # nouvelle liste, avec CROCHETS
```

Règle : **si la valeur doit pouvoir grandir avec `.append`, je la crée avec des crochets dès le départ.**

### 4.5 Copier un dictionnaire ou une liste

```python
temp = dico1          # Faux : même objet, deux noms
temp = dico1.copy()   # Juste : vraie copie
```

### 4.6 Fusionner : prendre la valeur de l'AUTRE dico

```python
for cle in dico2:
    if cle in temp:
        temp[cle] = temp[cle] + dico2[cle]
    else:
        temp[cle] = dico2[cle]
```

### 4.7 `.get(cle, defaut)` : lire sans plantage

```python
prix = {"stylo": 3}
prix["livre"]            # KeyError
prix.get("livre", 0)     # 0 : pas d'erreur, valeur de repli
```

Le compteur sans `if/else` :

```python
compteur[mot] = compteur.get(mot, 0) + 1
```

- `.get()` **lit**, il ne modifie jamais le dictionnaire : je stocke le résultat dans `compteur[mot]`.
- L'ordre des arguments : d'abord la **clé** qu'on cherche, ensuite la **valeur de repli** : `.get(cle, defaut)`.
- La valeur par défaut est celle d'**avant** le premier passage (0 pour un compteur, pas 1).
- Pour le groupement (valeur = liste), je garde le `if/else` : `.get(lettre, []).append(mot)` perd la liste, qui n'est jamais stockée.

### 4.8 `=` écrase, `+=` accumule

```python
# Faux : chaque clé commune REMPLACE le total, il ne garde que la dernière
total = 0
for cle in dico1:
    if cle in dico2:
        total = dico1[cle] * dico2[cle]

# Juste : on AJOUTE au total à chaque clé commune
        total += dico1[cle] * dico2[cle]
```

Le bug est invisible avec **une seule** clé commune. Test qui le révèle : `{"a": 2, "b": 3}` et `{"a": 1, "b": 4}` → attendu `14` (2 + 12), le code faux renvoie `12`.

#### Variante : lire l'autre dico sans vérifier

```python
# Faux : "chat" existe dans dico1 mais pas dans dico2
for cle in dico1:
    total += dico1[cle] * dico2[cle]       # KeyError: 'chat'

# Juste : je teste AVANT de lire
for cle in dico1:
    if cle in dico2:
        total += dico1[cle] * dico2[cle]
```

Règle : quand je boucle sur un dico et que je lis un **autre** dico avec `[]`, je teste d'abord `if cle in autre_dico`. Test qui le révèle : `({"le": 2, "chat": 1}, {"le": 1, "chien": 1})` → attendu `2`.

Piège de fond (vu 2 fois dans la semaine) : j'implémente la partie « multiplier » de l'énoncé et j'oublie la condition « uniquement les clés présentes dans les deux ». Je relis l'énoncé en cochant chaque mot-condition (« uniquement », « sauf », « seulement si »).

### 4.9 Brique validée, brique retapée : je la retesterai

```python
# Faux : le défaut est 1, donc chaque mot est compté un de trop
compteur[mot] = compteur.get(mot, 1) + 1

# Juste : 0 avant le premier passage
compteur[mot] = compteur.get(mot, 0) + 1
```

Piège vécu : `compteur_mot` était juste le matin, puis retapée de mémoire le soir avec `1`. Les tests où **chaque mot apparaît une fois** passaient quand même (tous les comptes sont gonflés pareil, l'erreur s'annule dans la division du cosinus). Seuls les tests avec un **mot répété** donnaient un mauvais résultat (`0.98058` au lieu de `0.948683`).

Règle : avant d'assembler des briques, je teste chaque brique seule avec un cas où un élément se répète : `compteur_mot("le chat le")` doit donner `{"le": 2, "chat": 1}`.

---

## 5. Conditions

| JS | Python |
|---|---|
| `\|\|` | `or` |
| `&&` | `and` |
| `!` | `not` |
| `null` | `None` |
| `true` / `false` | `True` / `False` |
| `.length` | `len(...)` |
| `.push()` | `.append()` |

### 5.1 `>` ou `>=` : tester sur les valeurs

"Au moins 2 fois" = `>= 2`. Je teste mentalement sur `2` et `1` pour choisir l'opérateur.

### 5.2 Liste vide

```python
if not ma_liste:
    ...    # liste vide
```

### 5.3 Où va chaque ligne dans la boucle ?

Je me demande : cette ligne va-t-elle **dans le `if`**, **après le `if`**, ou **après la boucle** ?

```python
for i in range(0, len(mots), pas):
    morceau = mots[i:i+taille]
    if len(morceau) < taille:      # trop court ?
        break                      # dans le if : on arrête
    resultat.append(" ".join(morceau))   # après le if, dans la boucle
return resultat                    # après la boucle
```

### 5.4 `in` ou `==` ?

| Question | Opérateur |
|---|---|
| Cette valeur est-elle **égale** à celle-là ? | `mot == cible` |
| Cette valeur **appartient**-elle à cette collection ? | `lettre in groupe`, `cle in texte` |

---

## 6. Erreurs et exceptions

### 6.1 `except` attend un nom d'exception

```python
# Faux
except a or b == 0:

# Juste
except ZeroDivisionError:
```

### 6.2 Les exceptions courantes

| Exception | Quand |
|---|---|
| `ZeroDivisionError` | division par zéro |
| `KeyError` | clé de dictionnaire inexistante |
| `IndexError` | index de liste inexistant |
| `TypeError` | types incompatibles |
| `ValueError` | bon type, valeur invalide |
| `FileNotFoundError` | fichier introuvable |
| `AttributeError` | méthode ou attribut inexistant (ex : `.append` sur une chaîne) |

Je lis toujours la **dernière ligne du traceback** : `NomException: message`.

### 6.3 `raise` vs `try/except`

- `raise ValueError("...")` : je **provoque** une erreur volontairement.
- `try / except` : j'**attrape** une erreur qui s'est produite.

### 6.4 Attraper ou laisser remonter ?

- **Attraper** s'il existe un vrai repli qui ne fausse rien (fichier de préférences optionnel).
- **Laisser remonter** si continuer donnerait un résultat faux qui a l'air normal (docs introuvables -> `[]` -> "aucun résultat").

Règle : **une erreur qui plante tout de suite et clairement vaut mieux qu'une réponse fausse qui a l'air normale.**

### 6.5 `raise` : avec le mot-clé, avec un message, avant la boucle

```python
# Faux 1 : "ValueError" seul est juste un nom, rien n'est levé
if chevauchement >= taille:
    ValueError

# Faux 2 : print affiche puis renvoie None, donc le message de l'erreur est None
raise ValueError(print("chevauchement trop grand"))

# Juste : vérifier les paramètres tout en haut, avec une chaîne comme message
def decouper(texte, taille, chevauchement):
    if chevauchement >= taille:
        raise ValueError("le chevauchement doit être plus petit que la taille")
    ...
```

- Sans le mot `raise`, rien n'est levé.
- Le message est une **chaîne** entre guillemets, jamais un `print(...)`.
- Une vérification écrite **dans** la boucle ne s'exécute que si la boucle fait un tour : `range` avec un pas nul ou négatif n'en fait aucun. Je vérifie les paramètres avant de les utiliser.

---

## 7. Classes

```python
class Note:
    def __init__(self, titre: str, contenu: str):
        self.titre = titre
        self.contenu = contenu

    def contient(self, motcle: str) -> bool:
        return motcle.lower() in self.contenu.lower()
```

- `self` est toujours le premier paramètre d'une méthode, jamais passé à l'appel.
- Les attributs se posent dans `__init__`, pas dans les autres méthodes.
- Accès avec le point : `note.titre`.

---

## 8. Fichiers, JSON et API

### 8.1 Lire un JSON

```python
import json

def open_doc(chemin: str) -> list:
    with open(chemin, "r", encoding="utf-8") as f:
        doc = json.load(f)       # load/dump = fichier ; loads/dumps = chaîne
    return doc                   # APRÈS le with, désindenté
```

Après `json.load`, ce sont de vrais dictionnaires et listes Python : crochets pour accéder aux champs.

### 8.2 `import` exécute tout le fichier

Un `import doc` lance toutes les lignes de `doc.py`, y compris les tests laissés en bas. Je garde seulement les définitions de fonctions (plus tard : `if __name__ == "__main__":`).

### 8.3 Clé d'API

Jamais dans le code : `export ANTHROPIC_API_KEY="..."` dans le terminal, et la librairie la lit toute seule.

### 8.4 Appeler un LLM

```python
import anthropic

def resumer(texte: str) -> str:
    client = anthropic.Anthropic()
    reponse = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{"role": "user", "content": f"..."}],   # seulement "role" et "content"
    )
    return reponse.content[0].text    # objet -> point, liste -> [0], objet -> point
```

Le prompt doit préciser le format exact, ce qu'il ne faut **pas** faire, limiter le contenu au texte fourni, et séparer clairement la consigne du texte.

---

## 9. Checklist avant de dire "c'est fini"

- [ ] J'ai relu l'énoncé ligne par ligne et coché chaque exigence (tri, casse, cas vide, ce que la fonction renvoie)
- [ ] J'ai coché chaque mot-condition de l'énoncé (« uniquement », « sauf », « seulement si »)
- [ ] Chaque paramètre de la fonction est utilisé quelque part (sinon j'ai oublié une exigence)
- [ ] Je vérifie les paramètres (`raise ValueError("message")`) au début de la fonction, avant la boucle
- [ ] J'ai testé avec l'exemple de l'énoncé
- [ ] J'ai testé le cas limite (liste vide, un seul élément, fichier absent)
- [ ] J'ai testé chaque brique réutilisée seule, avec un élément répété et deux clés communes (pas seulement un cas simple)
- [ ] Si l'énoncé demande un arrondi (`round(x, 6)`), il est appliqué au `return`
- [ ] Pas de `print` de debug oublié dans la fonction
- [ ] `return` désindenté après la boucle
- [ ] Les noms de variables disent ce qu'elles contiennent (et aucun ne masque un paramètre)
- [ ] Le résultat de chaque méthode (`.lower()`, `.split()`, `sorted()`, `.get()`) est stocké ou utilisé
- [ ] Une seule version du code dans le fichier (pas de doublon collé)