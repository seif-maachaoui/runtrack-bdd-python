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

#Création de la première table etage
first_request = "CREATE TABLE etage(id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero INT, superficie INT)"
second_request = "CREATE TABLE salles (id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT)"

cursor.execute(first_request)
cursor.execute(second_request)

db.close() #ferme la connexion à la base de donnée
