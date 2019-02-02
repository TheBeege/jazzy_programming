# SQL
SQL, or Structured Query Language, is the most common way to manipulate data within a relational database system. It's used to retrieve data, add new data, change data, and remove data. It allows for unifying disparate pieces of data, performing aggregative operations on data, and much more. We'll be focusing on the MySQL dialect of SQL, since MySQL is free and is one of the more common database systems.

## Sandbox
I've setup a sandbox on [DB-Fiddle](https://www.db-fiddle.com/f/pQkEECzSsz96MLYjoNEKJE/0), an online tool for experimenting with SQL. I recommend using later SQL examples with this to see how things work and to carry out exercises. Make sure to check out [answers.md](answers.md) to see the expected data for exercises in the lessons.

## A Note on DDL vs SQL
There is also a data definition language, or DDL. This is used for creating tables, altering columns, creating functions, and more. DDL is specific to a database system, so I won't cover it here. It's best to lookup the DDL for the operation you want to do on the database platform you're using. Each platform will have its own data types and other idiosyncrasies, so you'll need to do this anyway.

## Statements and Transactions
When you run a query against a database, the SQL text sent to the server is called a "statement". There are four main types of statements: `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. Each statement is considered a single operation from the perspective of the database server. Several statements can be run in a [transaction](https://en.wikipedia.org/wiki/Database_transaction), which can be rolled back if you decide you don't want to make changes or committed if you want the changes to persist in the database. Most often, your connection will default to "auto-commit", where any changes you make will be committed to persist in the database automatically. You can change this behavior when you connect, though this is likely a rare need for a data scientist.

Something worth noting: SQL itself is case-insensitive. `SELECT` is the same as `select`. Often times, you'll see SQL keywords in all capitals. This is due to just old programming habits and for readability of SQL versus data. Personally, I use capitals when talking about the SQL language but lower-case in my actual queries. There's no right or wrong way to do it. However, do be aware that the data _is_ case sensitive.

With that, let's dive into learning some SQL, starting with how to get data out.
