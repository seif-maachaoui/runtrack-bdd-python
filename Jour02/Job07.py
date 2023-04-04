import mysql.connector

# Connexion à la nouvelle base de données
new_db = mysql.connector.connect(
  host="localhost",
  user="seifeddine",
  password="Cyberpunk2077*",
  database="entreprise"
)


cursor = new_db.cursor()

#Création de la table employes
#request1 = ("CREATE TABLE employes (id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL, id_service INT)")
#cursor.execute(request1)


# Insertion de données dans la table employes
#request2 = ("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES ('White', 'Walter', 10000, 1), ('Pinkman', 'Jessie', 10000, 2), ('Fring', 'Gustavo', 50000, 3), ('Goodman', 'Saul', 500, 4), ('Salamanca', 'Tuco', 300, 5)")
#cursor.execute(request2)
#new_db.commit()

# Récupération des employés dont le salaire est supérieur à 3000
cursor.execute("SELECT nom, prenom, salaire FROM employes WHERE salaire > 3000")
result = cursor.fetchall()
print(result)

#request3 = ("CREATE TABLE services (id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")
#cursor.execute(request3)

#request4 = ("INSERT INTO services (nom) VALUES ('Chimiste'), ('Vendeur'), ('Avocat'), ('Trafiquant')")
#cursor.execute(request4)
#new_db.commit()


# Fermeture de la connexion
new_db.close()
