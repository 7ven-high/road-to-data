-- 01: Total transaction volume per category
SELECT category, COUNT(*) AS n_tx, ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY category
ORDER BY total_amount DESC;
