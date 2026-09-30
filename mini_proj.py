class Note:
    def __init__(self, titre: str, contenu: str, tags: list):
        self.titre = titre
        self.contenu = contenu
        self.tags = tags
    
    def contient(self, motcle: str) -> bool:
        return motcle.lower() in self.contenu.lower()
    
    def nombre_mots(self) -> int:
        nbr = self.contenu.split()
        return len(nbr)


def chercher(notes: list, motcle: str) -> list:
    resultat = []
    for note in notes:
        if note.contient(motcle):
            resultat.append(note.titre)
    return resultat

def compter_par_tag(notes: list, tag: str) -> int:
    count = 0
    for note in notes:
        if tag in note.tags:
            count += 1
    return count

def note_la_plus_longue(notes: list, tag: str) -> list:
    score = 0 
    meilleur_titre = []
    for note in notes:
        if tag in note.tags:
            if note.nombre_mots() > score:
                score = note.nombre_mots()
                meilleur_titre = note.titre  
                
    return meilleur_titre



notes = [
    Note("Python bases", "Python est un langage simple et lisible", ["python", "débutant"]),
    Note("RAG intro", "Un RAG combine recherche et génération de texte", ["ia", "rag"]),
    Note("Chunking", "Découper un texte en morceaux avec chevauchement", ["ia", "rag", "python"]),
]

print(chercher(notes, "texte"))          # ['Chunking', 'RAG intro']
print(compter_par_tag(notes, "python"))  # 2
print(note_la_plus_longue(notes, "rag")) # "Chunking" (le plus long des deux notes taguées "rag")