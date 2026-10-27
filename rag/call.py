from pathlib import Path
import anthropic
import scalaire


DOSSIER = Path(__file__).parent   # le dossier rag/, d'où que le script soit lancé

def repondre(question: str, passages: list) -> str:
    content = scalaire.construire_prompt(question, passages)
    client = anthropic.Anthropic()

    if passages == []:
        return("je ne sais pas")

    reponse = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[{"role": "user", "content": f"{content}"}],
    )
    for bloc in reponse.content:
        if bloc.type == "text":
            return(bloc.text)
    return("je ne sais pas")


       