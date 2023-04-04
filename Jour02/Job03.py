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

first_request = "INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500), \
('R+1', 1, 500)"


second_request = "INSERT INTO salles (nom, id_etage, capacite) VALUES ('Lounge', 1, 100), \
('Studion Son', 1, 5), \
('Broadcasting', 2, 50),\
('Bocal Peda', 2, 4), \
('Coworking', 2, 80), \
('Studio Video', 2, 5)"

cursor.execute(first_request)
cursor.execute(second_request)
db.commit()
cursor.execute("SELECT * FROM etage")
result1 = cursor.fetchall()
print(result1)

cursor.execute("SELECT * FROM salles")
result2 = cursor.fetchall()
print(result2)

db.close()