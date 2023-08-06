-- Write an SQL query to solve the given problem statement.
-- Retrieve all records from the 'ecommerce' table where the product name contains the word 'Tablet' as a substring

-- How to finish the current Task?
-- To successfully finish this task, you need to compose your SQL query in the ""task3_11.sql"" file and click on the ""Run Test"" button. If your query passes, you will proceed to the next task. However, if your query fails, the results will be displayed on your screen.


SELECT * FROM ecommerce WHERE name LIKE "%Tablet%"