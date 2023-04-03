mysql> DELETE FROM 'etudiants' WHERE 'id' = 3 ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''etudiants' WHERE 'id' = 3' at line 1
mysql> DELETE FROM etudiants WHERE id = 3 ;
Query OK, 1 row affected (0.02 sec)

mysql> notee
