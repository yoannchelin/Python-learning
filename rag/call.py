from pathlib import Path

import anthropic
import doc

DOSSIER = Path(__file__).parent   # le dossier rag/, d'où que le script soit lancé

def resumer(texte: str) -> str:
    client = anthropic.Anthropic()

    reponse = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=200,
    messages=[{"role": "user", "content": f"fais un resume du texte en 1 phrase\n .{texte}"}],
    )
    return reponse.content[0].text


documents = doc.open_doc(DOSSIER / "docs.json")     # une liste de dictionnaires
premier = documents[4]                # un dictionnaire
texte = premier["contenu"]            # une chaîne (crochets : c'est un dict)
print(resumer(texte))
       