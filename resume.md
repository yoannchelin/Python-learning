## Mon carnet de pièges Python (version courte)

Je note chaque erreur que j'ai faite, avec la version fausse et la version juste. Le carnet complet est dans `carnet-pieges-python.md`.

| Piège | Faux | Juste |
|---|---|---|
| Résultat d'une méthode perdu | `phrase.lower()` | `phrase = phrase.lower()` |
| Ordre des méthodes | `phrase.split().lower()` | `phrase.lower().split()` |
| `return` trop tôt | `return` dans la boucle | `return` après la boucle |
| `.append` renvoie `None` | `res = res.append(x)` | `res.append(x)` |
| Écraser au lieu d'accumuler | `total = a * b` | `total += a * b` |
| Compteur avec `.get` | `.get(mot, 1) + 1` | `compteur[mot] = compteur.get(mot, 0) + 1` |
| Lire une clé absente | `dico2[cle]` | `if cle in dico2: ...` |
| Groupement | `groupe[lettre] = mot` | `groupe[lettre] = [mot]` |
| Variable qui masque un paramètre | `for cible in ...` | `for mot in ...` |
| `join` | `" ".join(res.append(x))` | `texte = " ".join(liste)` puis `res.append(texte)` |
| Plusieurs morceaux à ajouter | `res.append(" ".join(morceaux))` | `res += morceaux` |
| Premier élément d'une liste | `docs[:1]` (une liste) | `docs[0]` (l'élément) |
| Liste de dicts | `docs["titre"]` | `docs[0]["titre"]` : position, puis clé |
| Trier un dico par valeur | `sorted(scores)` | `sorted(scores, key=lambda p: scores[p], reverse=True)` |
| `raise` | `ValueError` ou `ValueError(print(...))` | `raise ValueError("message")`, avant la boucle |
| Paramètre jamais utilisé | `k` oublié, tout est renvoyé | `classement[:k]` |
| Arrondi oublié | `return resultat` | `return round(resultat, 6)` |

**Ma méthode :** une phrase en français avant le code, un tableau pour tracer la boucle, puis je lance les tests et je lis la sortie avant de montrer quoi que ce soit.

**Ma checklist :** j'ai coché chaque exigence de l'énoncé, testé l'exemple et le cas limite, testé chaque brique seule (avec un élément répété), et chaque paramètre est utilisé quelque part.