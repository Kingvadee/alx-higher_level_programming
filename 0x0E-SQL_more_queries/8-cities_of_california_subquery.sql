-- Subquery of california states in db hbtn_0d_usa
SELECT id, name
  FROM cities
 WHERE state_id
       IN (SELECT id FROM states WHERE name = 'California')
 ORDER BY id;
