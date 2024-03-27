import sqlite3


users = []
chats = []
messages = []
conectedUser = []

# def creer_base_de_donnees():
#     connexion = sqlite3.connect('medical_advisor.db')
#     curseur = connexion.cursor()
#     curseur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             email TEXT NOT NULL UNIQUE,
#             phone TEXT NOT NULL UNIQUE,
#             password TEXT NOT NULL,
#             birth_date INTEGER NOT NULL
#         );
#     """)
#     curseur.execute("""
#         CREATE TABLE IF NOT EXISTS chats (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             userId INTEGER,
#             date DATETIME NOT NULL,
#             FOREIGN KEY (userId) REFERENCES users(id)
#         );
#     """)
#     curseur.execute("""
#         CREATE TABLE IF NOT EXISTS messages (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             label TEXT NOT NULL,
#             chatId INTEGER,
#             date DATETIME NOT NULL,
#             isGenerated BOOLEAN NOT NULL DEFAULT 0,
#             FOREIGN KEY (chatId) REFERENCES chats(id)
#         );
#     """)
#     connexion.commit()
#     connexion.close()

    
# def inserer_utilisateur(first_name, last_name, email, phone, password, birth_date):
#     try:
#         connexion = sqlite3.connect('medical_advisor.db')
#         curseur = connexion.cursor()
#         curseur.execute("""
#             INSERT INTO users (first_name, last_name, email, phone, password, birth_date)
#             VALUES (?, ?, ?, ?, ?, ?)
#         """, (first_name, last_name, email, phone, password, birth_date))
#         connexion.commit()
#         connexion.close()
#     except sqlite3.Error as e:
#         print("ther is an error")
#         print("An error occurred:", e)
#         connexion.close()
#         return e
    

# def connecter_utilisateur(email, password):
#     connexion = sqlite3.connect('medical_advisor.db')
#     curseur = connexion.cursor()
#     curseur.execute("""
#         SELECT * FROM users WHERE email = ? AND password = ?
#     """, (email, password))
#     utilisateur = curseur.fetchone()
#     connexion.close()
#     return utilisateur


