-- Prepare > SQL > Aggregation
-- Population Density Difference
-- Query the difference between the maximum and minimum populations in CITY.

SELECT max(Population)-min(Population) FROM City;