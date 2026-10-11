# Python-learning

Mon parcours pour passer de développeur front-end junior à **AI engineer**. Je repars de zéro en Python et je construis progressivement vers un chatbot, un RAG et un agent.

Ce dépôt contient mes exercices, mon carnet d'erreurs et les petits projets qui en découlent.

## Où j'en suis

- Bases de Python : fonctions, boucles, dictionnaires, classes
- Fichiers et JSON : lecture avec `json.load`
- Exceptions : `try/except`, `raise`, laisser remonter l'erreur
- Appel de l'API Anthropic depuis Python
- Briques d'un RAG : chunking avec overlap, similarité cosinus
- `sorted` avec `key`, compréhensions de liste

## Le carnet de pièges

Le fichier [`carnet-pieges-python.md`](carnet-pieges-python.md) liste mes erreurs récurrentes en passant de JS/TS à Python, avec pour chacune la version fausse, la version juste et le réflexe à avoir. C'est le document le plus utile du dépôt pour moi.

## Ma méthode

- **Le tableau** : avant d'écrire une boucle, je déroule un petit exemple à la main et je note ce que vaut chaque variable à chaque tour.
- **Une phrase en français avant le code** : je décris chaque étape avant de la traduire.
- **Séances chronométrées** : je réécris des fonctions à partir d'un fichier vide, sans regarder l'ancien code, et je note le temps.
- **Indices plutôt que solutions** : quand je bloque, je cherche à comprendre l'erreur avant de demander de l'aide.
- **Noms parlants** : une variable dit ce qu'elle contient (`i` seulement pour un `range`).

## Structure

```
.
├── carnet-pieges-python.md   # mes erreurs récurrentes et leurs corrections
├── docs.json                 # documents de test pour les exercices de recherche
├── doc.py                    # chargement et recherche dans les documents
├── call.py                   # appel de l'API Anthropic
├── semaine1.py
├── training.py
└── exercices/                # exercices réécrits à vide, chronométrés
```

## Lancer le projet

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic
```

Pour les scripts qui appellent l'API, la clé se définit dans le terminal et ne se met **jamais** dans le code :

```bash
export ANTHROPIC_API_KEY="ma-cle"
```

## Sécurité

Le fichier `.gitignore` exclut `.venv/` et tout fichier contenant une clé. Aucune clé d'API n'est commitée.

## Prochaines étapes

- [ ] `.get()` et `enumerate`
- [ ] Mini-RAG en mémoire : chunking, similarité, meilleurs passages
- [ ] API avec FastAPI
- [ ] Tests avec pytest
- [ ] Chatbot, puis RAG complet, puis agent

## Contact

[Yoann Chelin] · [https://linkedin.com/in/yoann-chelin] · [yoannchelin9@gmail.com]