-- 01: Total transaction volume per category
SELECT category, SUM(amount) AS total_volume
FROM transactions
GROUP BY category
ORDER BY total_volume DESC;

-- 02: Average transaction amount per user
SELECT 
    customers.name, 
    AVG(transactions.amount) AS avg_transaction
FROM 
    transactions
INNER JOIN accounts ON transactions.account_id = accounts.account_id
INNER JOIN customers ON accounts.customer_id = customers.customer_id
GROUP BY customers.name
ORDER BY name;

--03: Which are the 10 customers who spend the most
SELECT 
    customers.name
--SUM(transactions.amount) as sum_transactions

FROM 
    transactions
INNER JOIN accounts ON transactions.account_id = accounts.account_id
INNER JOIN customers ON accounts.customer_id = customers.customer_id
GROUP BY customers.name
ORDER BY SUM(transactions.amount) DESC
LIMIT 10;
