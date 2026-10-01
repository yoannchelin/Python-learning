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
    
    def tag_principal(self) -> str:
        if not self.tags:
            return "aucun"
        return self.tags[0]


def chercher(notes: list, motcle: str) -> list:
    resultat = []
    for note in notes:
        if note.contient(motcle):
            resultat.append(note.titre)
    return sorted(resultat)

def compter_par_tag(notes: list, tag: str) -> int:
    count = 0
    for note in notes:
        if tag in note.tags:
            count += 1
    return count

def note_la_plus_longue(notes: list, tag: str) -> list:
    score = 0 
    meilleur_titre = ""
    for note in notes:
        if tag in note.tags:
            if note.nombre_mots() > score:
                score = note.nombre_mots()
                meilleur_titre = note.titre  
                
    return meilleur_titre

def est_palindrome(mot: str) -> bool:
    return mot[::-1] == mot



notes = [
    Note("Python bases", "Python est un langage simple et lisible", ["python", "débutant"]),
    Note("RAG intro", "Un RAG combine recherche et génération de texte", ["ia", "rag"]),
    Note("Chunking", "Découper un texte en morceaux avec chevauchement", ["ia", "rag", "python"]),
]

note = Note("Python bases", "Python est un langage simple", ["python", "débutant"])
print(note.tag_principal())   # "python"

note_sans_tag = Note("Vide", "Rien ici", [])
print(note_sans_tag.tag_principal())   # "aucun"

print(chercher(notes, "texte"))          # ['Chunking', 'RAG intro']
print(compter_par_tag(notes, "python"))  # 2
print(note_la_plus_longue(notes, "rag")) # "Chunking" (le plus long des deux notes taguées "rag")
print(est_palindrome("radar"))