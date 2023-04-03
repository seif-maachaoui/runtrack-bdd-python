mysql> Select id, nom, prenom, email, age from etudiants where age >= 18 and age <= 25 order by age ASC;
+----+--------+-----------+---------------------------------+-----+
| id | nom    | prenom    | email                           | age |
+----+--------+-----------+---------------------------------+-----+
|  3 | Doe    | John      | john.doe@laplateforme.io        |  18 |
|  6 | Dupuis | Martin    | martin.dupuis@laplateforme.io   |  18 |
|  5 | Dupuis | Gertrude  | gertrude.dupuis@laplateforme.io |  20 |
|  1 | Betty  | Spaghetti | betty.Spaghetti@laplateforme.io |  23 |
+----+--------+-----------+---------------------------------+-----+
4 rows in set (0.00 sec)

mysql> notee
