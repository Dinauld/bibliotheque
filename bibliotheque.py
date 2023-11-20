import sqlite3
from tkinter import *
from tkinter import messagebox

# Connexion à la base de données
conn = sqlite3.connect('bibliotheque.db')
cursor = conn.cursor()

# Création de la table Livres
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT,
        auteur TEXT,
        genre TEXT,
        isbn TEXT
    )
''')
conn.commit()

# Création de la table Utilisateurs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        categorie TEXT
    )
''')
conn.commit()

# Création de la table Prêts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livre_id INTEGER,
        utilisateur_id INTEGER,
        date_emprunt DATE,
        date_retour DATE,
        FOREIGN KEY (livre_id) REFERENCES Livres(id),
        FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(id)
    )
''')
conn.commit()

# Fonction pour ajouter un livre
def ajouter_livre():
    titre = entry_titre.get()
    auteur = entry_auteur.get()
    genre = entry_genre.get()
    isbn = entry_isbn.get()

    cursor.execute("INSERT INTO Livres (titre, auteur, genre, isbn) VALUES (?, ?, ?, ?)",
                   (titre, auteur, genre, isbn))
    conn.commit()
    messagebox.showinfo("Succès", "Livre ajouté avec succès")

# Fonction pour afficher les livres
def afficher_livres():
    livres = cursor.execute("SELECT * FROM Livres").fetchall()
    for livre in livres:
        print(livre)

# Interface graphique
root = Tk()
root.title("Gestion de Bibliothèque")
root.geometry('1280x720')


# Entrées pour ajouter un livre
label_titre = Label(root, text="Titre")
label_titre.grid(row=0, column=0)
entry_titre = Entry(root)
entry_titre.grid(row=0, column=1)

label_auteur = Label(root, text="Auteur")
label_auteur.grid(row=1, column=0)
entry_auteur = Entry(root)
entry_auteur.grid(row=1, column=1)

label_genre = Label(root, text="Genre")
label_genre.grid(row=2, column=0)
entry_genre = Entry(root)
entry_genre.grid(row=2, column=1)

label_isbn = Label(root, text="ISBN")
label_isbn.grid(row=3, column=0)
entry_isbn = Entry(root)
entry_isbn.grid(row=3, column=1)

# Bouton pour ajouter un livre
button_ajouter = Button(root, text="Ajouter Livre", command=ajouter_livre)
button_ajouter.grid(row=4, column=0, columnspan=2)

# Bouton pour afficher les livres
button_afficher = Button(root, text="Afficher Livres", command=afficher_livres)
button_afficher.grid(row=5, column=0, columnspan=2)

root.mainloop()
