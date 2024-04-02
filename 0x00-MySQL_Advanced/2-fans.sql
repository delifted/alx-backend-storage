-- Select origin and count the number of fans for each country
-- Group by origin to aggregate the number of fans for each country
-- Order by the number of fans in descending order
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;