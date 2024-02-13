-- Script to display the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, AVG(temperature) AS avg_temperature_fahrenheit
FROM table_name
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
