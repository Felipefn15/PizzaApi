INSERT INTO `Order-Progress`
VALUES ('{0}','{1}',1,now()) 
ON DUPLICATE KEY 
UPDATE 
    quantity = quantity + 1,
    date = now()