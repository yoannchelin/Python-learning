import doc
import scalaire
import call


if __name__ == "__main__":
    questions = ["Comment le RAG transforme les documents en vecteurs ?",
                "Comment écrire un bon prompt ?",
                "Quelle est la capitale du Japon ?",
                ""]
    docs = doc.open_doc("docs.json")
    morceaux = scalaire.preparer_morceaux(docs, 30, 5)
    for question in questions:
        meilleurs_passage = scalaire.meilleurs_passages(question, morceaux, 3)
        response = call.repondre(question, meilleurs_passage)
