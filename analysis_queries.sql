-- Top 10 Best Selling Games
SELECT name, global_sales
FROM sales
ORDER BY global_sales DESC
LIMIT 10;

-- Genres with Highest Sales
SELECT genre, SUM(global_sales) AS total_sales
FROM sales
GROUP BY genre
ORDER BY total_sales DESC;

-- Rating vs Sales Correlation
SELECT g.title, g.rating, s.global_sales
FROM games g
JOIN sales s ON g.title = s.name
ORDER BY s.global_sales DESC;
