mysql> INSERT INTO etudiants(id, nom, prenom, age, email) 
    -> VALUES (NULL, 'Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
Query OK, 1 row affected (0.02 sec)

mysql> select * from etudiants where nom = 'Dupuis' ;
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+-----+---------------------------------+
2 rows in set (0.00 sec)

mysql> notee
