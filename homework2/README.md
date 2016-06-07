# Homework 2
### Working with SQL data derived from from the MovieLens data.

Created a database with the imported sql data (in psql)

Connected to the database via pg8000 in jupyter

Performed a variety of queries on the data using WHERE, ORDER BY, aggregation, GROUP BY, HAVING, COUNT() and JOIN in order to have the desired output.


I learned that ORDER MATTERS:
```ORDER BY avg(rating)``` would not work unless it was at the end of SQL statement.

Also, it was helpful to include ```conn.rollback()``` at the beginning of different code blocks in order to ensure every time that it was run that any previous errors were cleared out.
