SELECT r.first_name, r.last_name, COUNT(*) --COUNT(DISTINCT r.first_name) --, , 
FROM books as b, readers as r--books--, authors, readers, registers
GROUP BY r.first_name, r.last_name
