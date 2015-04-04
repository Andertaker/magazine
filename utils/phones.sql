ALTER TABLE phones ADD PRIMARY KEY (phone);
ALTER TABLE items ADD PRIMARY KEY (id);


INSERT INTO phones (phone, users) VALUES ('123', '{1,2,3}');

INSERT INTO phones (phone, users) VALUES ('456', '{4,5,6}');
INSERT INTO phones (phone, users) VALUES ('789', '{7,8,9}');



INSERT INTO items (user_id, status) VALUES (1, 1);



SELECT
    phone, unnest(users) as user_id, status
FROM phones
LEFT JOIN items ON (user_id = items.user_id AND items.status=1)



SELECT
    phone, user_id
FROM (SELECT phone, unnest(users) as user_id FROM phones)
LEFT JOIN items ON (user_id = items.user_id AND items.status=1)



SELECT
    p.phone, COUNT(*) as items_sold
FROM (SELECT phone, unnest(users) as user_id FROM phones) p
JOIN items ON (p.user_id = items.user_id AND items.status=1)
GROUP BY phone
ORDER BY phone


SELECT
    p.phone, SUM(status) as items_sold, SUM(CASE items.status WHEN 1 THEN 0 ELSE 1 END) as unsold_sold, COUNT(*) as total
FROM (SELECT phone, unnest(users) as user_id FROM phones) p
JOIN items ON (p.user_id = items.user_id)
GROUP BY phone
ORDER BY phone





