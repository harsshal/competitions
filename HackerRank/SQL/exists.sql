-- approach 1
WITH RECURSIVE total_numbers AS (
    SELECT 2 AS num
    UNION ALL
    SELECT num + 1 FROM total_numbers WHERE num < 1000
)
SELECT GROUP_CONCAT(num SEPARATOR '&')
FROM total_numbers outert
WHERE outert.num NOT in (
    SELECT outert.num
    FROM total_numbers innert
    WHERE outert.num % innert.num = 0 AND outert.num > innert.num
)

-- approach 2
-- for every row in inner_table, see if we have any row which satisfies the condition
WITH RECURSIVE total_numbers AS (
    SELECT 2 AS num
    UNION ALL
    SELECT num + 1 FROM total_numbers WHERE num < 1000
)
SELECT GROUP_CONCAT(num SEPARATOR '&')
FROM total_numbers outert
WHERE NOT EXISTS (
    SELECT 1 -- column name doesnt matter
    FROM total_numbers innert
    WHERE outert.num % innert.num = 0 AND outert.num > innert.num
)