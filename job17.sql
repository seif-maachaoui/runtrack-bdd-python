mysql> UPDATE etudiants SET age_1 = 20 WHERE id = 1 ;
ERROR 1054 (42S22): Unknown column 'age_1' in 'field list'
mysql> UPDATE etudiants SET age = 20 WHERE id = 1 ;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> notee
