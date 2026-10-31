# Tests du bloc 4 (FastAPI), hors ligne.
# À mettre dans ton dossier rag/, à côté de api.py, puis :   python3 test_api_vol.py
#
# TestClient envoie de vraies requêtes à ton API sans lancer de serveur
# et sans internet. Ton api.py doit définir une variable `app`.

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def check(label, test):
    try:
        print(("OK    " if test() else "FAUX  ") + label)
    except Exception as e:
        print("ERR   " + label + "  (" + type(e).__name__ + ": " + str(e) + ")")


def ping():
    r = client.get("/ping")
    return r.status_code == 200 and r.json() == {"status": "ok"}


def question_pertinente():
    r = client.post("/question", json={"question": "Comment le RAG transforme les documents en vecteurs ?"})
    corps = r.json()
    return (r.status_code == 200
            and corps["question"] == "Comment le RAG transforme les documents en vecteurs ?"
            and isinstance(corps["passages"], list)
            and 1 <= len(corps["passages"]) <= 3)


def question_hors_sujet():
    r = client.post("/question", json={"question": "Quelle est la capitale du Japon ?"})
    return r.status_code == 200 and r.json()["passages"] == []


def corps_invalide():
    r = client.post("/question", json={})
    return r.status_code == 422


check("GET /ping", ping)
check("POST /question pertinente : 1 à 3 passages", question_pertinente)
check("POST /question hors sujet : aucun passage", question_hors_sujet)
check("POST /question sans champ question : 422", corps_invalide)
