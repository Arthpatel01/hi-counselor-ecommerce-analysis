SELECT brand,
    COUNT(CASE WHEN sentiment="positive" THEN 1 END) AS positive_count,
    COUNT(CASE WHEN sentiment="negative" THEN 1 END) AS negative_count,
    COUNT(*) AS total_reviews,
    FORMAT((COUNT(CASE WHEN sentiment="positive" THEN 1 END)/COUNT(*) * 100), 2)AS positive_percentage,
    FORMAT((COUNT(CASE WHEN sentiment="negative" THEN 1 END)/COUNT(*) * 100), 2) AS negative_percentage
FROM ecommerce GROUP BY brand