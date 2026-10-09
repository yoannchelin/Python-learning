import json


def open_doc(doc: str) -> list:
        with open(doc, "r", encoding="utf-8") as f:
            charges = json.load(f)
        return charges


def filtrer_titres(documents, motcle):
    res = []
    for doc in documents:
        if motcle.lower() in doc["contenu"].lower():
            res.append(doc["titre"])        
    return sorted(res)
