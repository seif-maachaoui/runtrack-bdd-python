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

cursor.execute("SELECT SUM(capacite) \
FROM salles")
result = cursor.fetchone()
print("La capacité de toutes les salles est de :", result[0])