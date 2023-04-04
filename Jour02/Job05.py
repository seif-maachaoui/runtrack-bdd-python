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

cursor.execute("SELECT SUM(superficie) \
FROM etage")
result = cursor.fetchone()
print("La superficie de La Plateforme est de", result[0], "m2" )