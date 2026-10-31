# Pack de vol (5 h, sans internet)

## Avant d'embarquer (5 min, avec internet)

- [ ] Télécharge les 3 fichiers : `vol_exercices.py`, `test_api_vol.py`, `vol_guide.md`.
- [ ] Mets `test_api_vol.py` dans ton dossier `rag/`, à côté de `api.py`.
- [ ] Lance `python3 vol_exercices.py` : tu dois voir des lignes `----` et `FAUX`. C'est normal, rien n'est écrit.
- [ ] Dans `rag/`, avec ton `.venv` activé : `python3 -c "import fastapi, httpx"` ne doit afficher aucune erreur.
- [ ] Ordinateur chargé, et ton carnet de pièges sur le disque.

Pas d'internet en vol, donc **aucun appel à l'API Claude**. Le bloc 4 s'arrête aux passages ; tu brancheras la réponse de Claude à l'atterrissage.

---

## Plan de vol

| Temps | Bloc | Durée |
|---|---|---|
| 0:00 | Installation, décollage, souffle | 20 min |
| 0:20 | **Bloc 1** : warm-up, ta chaîne RAG de mémoire | 40 min |
| 1:00 | **Bloc 2** : la classe `Stock` (POO) | 50 min |
| 1:50 | *Pause : film, marcher, manger* | 20 min |
| 2:10 | **Bloc 3** : SQL avec sqlite3 | 40 min |
| 2:50 | **Bloc 4** : FastAPI, route `POST /question` | 45 min |
| 3:35 | *Pause* | 15 min |
| 3:50 | **Bloc 5** : préparation d'entretien en anglais | 40 min |
| 4:30 | Repos, relecture du carnet | 30 min |

**Si tu fatigues :** coupe le bloc 3 ou le 4, mais garde le 1 (réflexes) et le 5 (entretiens). Deux erreurs d'inattention de suite = pause de 10 minutes.

**Les règles :** une phrase en français avant chaque fonction, et le chrono s'arrête quand les tests passent. Tu n'ouvres les indices qu'après 10 minutes bloqué.

---

## Blocs 1, 2 et 3

Les énoncés et les tests sont dans `vol_exercices.py`. Tu écris ton code dans la zone « TON CODE ICI », puis :

```
python3 vol_exercices.py 1
python3 vol_exercices.py 2
python3 vol_exercices.py 3
```

### Mémo SQL (bloc 3)

La syntaxe, sur **d'autres tables** que celles de l'exercice : `eleves(id, nom, classe)` et `notes(id, eleve_id, matiere, note)`.

```sql
-- choisir des colonnes, trier
SELECT nom FROM eleves ORDER BY nom;

-- filtrer (les chaînes entre apostrophes simples)
SELECT nom FROM eleves WHERE classe = 'CM2';

-- regrouper et additionner : une ligne par élève
SELECT eleve_id, SUM(note) FROM notes GROUP BY eleve_id;

-- filtrer AVANT de regrouper : WHERE vient avant GROUP BY
SELECT eleve_id, COUNT(*) FROM notes WHERE matiere = 'maths' GROUP BY eleve_id;

-- relier deux tables
SELECT e.nom, n.note FROM notes n JOIN eleves e ON e.id = n.eleve_id;

-- une valeur qui dépend d'une condition
SELECT CASE WHEN note >= 10 THEN 'admis' ELSE 'refusé' END FROM notes;
```

L'ordre des mots-clés est toujours : `SELECT … FROM … JOIN … ON … WHERE … GROUP BY … ORDER BY …`

---

## Bloc 4 : FastAPI, route `POST /question` (45 min)

### Énoncé
Dans ton `api.py`, à côté de `/ping`, ajoute une route `POST /question` :
- elle reçoit un JSON `{"question": "..."}` ;
- elle renvoie `{"question": "...", "passages": [...]}` avec au plus 3 passages, trouvés par ta chaîne RAG sur `docs.json` ;
- elle n'appelle pas Claude (pas de réseau en vol).

### Étapes (une sortie à chaque étape)
1. Une phrase en français : qu'est-ce qui est fait **une seule fois** au démarrage, et qu'est-ce qui est fait **à chaque requête** ? C'était la question de la dernière séance.
2. Décris le JSON d'entrée avec une classe Pydantic (mémo ci-dessous).
3. Écris la route, et renvoie d'abord seulement la question, pour vérifier que ça marche.
4. Ajoute les passages.
5. Lance `python3 test_api_vol.py` : 4 `OK` et le chrono s'arrête.

Pour tester à la main : `fastapi dev api.py`, puis, dans un autre terminal :

```
curl -X POST http://127.0.0.1:8000/question -H "Content-Type: application/json" -d '{"question": "Comment écrire un bon prompt ?"}'
```

La page `/docs` risque de ne pas s'afficher hors ligne : elle charge son interface depuis internet. Utilise curl ou le fichier de test.

### Mémo FastAPI (exemple de la doc officielle, sur un autre sujet)

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):      # décrit le JSON reçu : {"name": "...", "price": 9.5}
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):            # FastAPI lit le JSON et le valide
    return {"name": item.name, "total": item.price * 2}   # dict -> JSON
```

Si le JSON reçu ne correspond pas à la classe (un champ manque), FastAPI répond **422** tout seul, sans que tu écrives quoi que ce soit.

---

## Bloc 5 : préparation d'entretien en anglais (40 min)

Pour chaque question, écris 3 à 5 **mots-clés ou puces**, pas un texte entier. Puis réponds à voix basse en 60 à 90 secondes. L'objectif est d'avoir déjà dit chaque histoire une fois avant le vrai entretien.

1. **Tell me about yourself.** (Epitech → France full-stack → Perth → Python et IA → pourquoi le VIE)
2. **Walk me through the warehouse system you built at John Building Supplies.** (le problème, ta stack, ce que tu as livré en premier, et pourquoi)
3. **How did you migrate the Excel data? What problems did you find?** (produits mal saisis, mauvais emplacements, références de 2006)
4. **How does the stock calculation work? What happens if a sale exceeds the stock?** (tu viens de coder la réponse dans le bloc 2)
5. **How does the handwritten form feature work? What if Claude misreads a form?** (scan → API Claude → validation humaine → stock)
6. **Why did you build a RAG from scratch instead of using a framework?** (ce que tu as appris : score 0 pour le bon passage, accents, pluriels, mots vides, puis 0.179)
7. **Explain RAG to a non-technical person in three sentences.**
8. **What is a REST API? What is the difference between GET and POST?** (tu viens d'en écrire un dans le bloc 4)
9. **Tell me about a mistake you made and what you learned.** (exemples : `if type == "text"` toujours faux, ou le prompt réécrit sans consigne qui a répondu « Tokyo »)
10. **Why a V.I.E.? Why our company?** Une réponse par entreprise :
    - The Revenue Architects : construire des systèmes qui servent un objectif business, avec l'IA au cœur du travail ;
    - Enlaye : l'IA pour la construction, et tes projets dans les matériaux ;
    - SII : une équipe structurée pour progresser, et l'international.
11. **Do you speak Spanish?** (pour SII : une réponse honnête, et ce que tu es prêt à faire)
12. **When can you start?** (retour fin janvier : prépare une phrase claire)

---

## Indices (seulement après 10 minutes bloqué)

### Bloc 1
- Ton carnet : sections 9.2 (ponctuation → espace), 9.3 (accents, `NFD` et `"Mn"`), 9.4 (pluriel), 4.3 (compteur), 3.8 (trier un dico par valeur).
- `meilleurs_passages` : le filtre « score > 0 » se place au moment de remplir le dictionnaire.
- `similarite_texte("", "chat")` : quelle opération plante quand une norme vaut 0 ?

### Bloc 2
- Le dictionnaire du stock est un attribut : il s'écrit `self.quelque_chose`, et il se crée dans `__init__`.
- Toutes les méthodes reçoivent `self` en premier paramètre, même si elles n'utilisent pas d'autre argument.
- `retirer` : fais **toutes** les vérifications avant de modifier quoi que ce soit, sinon le test « stock inchangé » échoue.
- `appliquer` : un tuple se déballe dans la boucle (`for a, b, c in liste_de_tuples`). Ne nomme pas une variable `type`, c'est le piège de mardi.
- `appliquer` peut réutiliser `ajouter` et `retirer` : `self.ajouter(...)`.
- `en_rupture` : construis la liste des références sous le seuil, puis trie-la (carnet 3.6).

### Bloc 3
- REQUETE_3 : `WHERE type = 'achat'` vient avant `GROUP BY produit_id`.
- REQUETE_4 : `JOIN produits ON produits.id = mouvements.produit_id`, puis on regroupe par nom.
- REQUETE_5 : le `CASE` renvoie `+quantite` pour un achat et `-quantite` pour une vente, et `SUM` fait le reste.

### Bloc 4
- La classe Pydantic n'a qu'un seul champ, de type `str`.
- `@app.post("/question")` au-dessus de la fonction, et le paramètre de la fonction est typé avec ta classe.
- Le chargement de `docs.json` et le découpage se font **en dehors** de la fonction, en haut du fichier : une seule fois au démarrage, pas à chaque requête.
- Tes fonctions sont dans d'autres fichiers : `import doc`, `import scalaire`, puis `scalaire.meilleurs_passages(...)`.

Bon vol !
