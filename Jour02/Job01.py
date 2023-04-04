import mysql.connector #Importation du module mysql.connector

#Connexion à la base de donnée
db = mysql.connector.connect(
    host = "localhost",
    user = "seifeddine",
    password = "Cyberpunk2077*",
    database = "laplateforme" 
)

#Création d'un objet cursor pour éxécuter des requêtes SQL
cursor = db.cursor()

#J'éxécute ma requête pour récupérer l'ensemble des étudiants
cursor.execute('SELECT * FROM etudiants')
result = cursor.fetchall() #récupère toute les lignes de la table étudiants
print(result) #affiche le résultat sous forme de tuple
db.close() #ferme la connexion à la base de donnée


