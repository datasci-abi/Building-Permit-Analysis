-- Top 10 states by total residential permits
SELECT State, Total
FROM permits
ORDER BY Total DESC
LIMIT 10;

-- Bottom 5 states by permit volume
SELECT State, Total
FROM permits
ORDER BY Total ASC
LIMIT 5;

-- State permit share as a percent of national total
SELECT State,
       ROUND(Total * 100.0 / (SELECT SUM(Total) FROM permits), 2) AS Share_Pct
FROM permits
ORDER BY Share_Pct DESC
LIMIT 10;
