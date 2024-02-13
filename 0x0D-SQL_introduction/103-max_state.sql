-- Script to display the top 3 cities' temperatures during July and August ordered by temperature (descending)

SELECT city, temperature
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;`
