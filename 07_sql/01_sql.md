# SQL
SQL, or Structured Query Language, is the most common way to manipulate data within a relational database system. It's used to retrieve data, add new data, change data, and remove data. It allows for unifying disparate pieces of data, performing aggregative operations on data, and much more. We'll be focusing on the MySQL dialect of SQL, since MySQL is free and is one of the more common database systems.

## A Note on DDL vs SQL
There is also a data definition language, or DDL. This is used for creating tables, altering columns, creating functions, and more. DDL is specific to a database system, so I won't cover it here. It's best to lookup the DDL for the operation you want to do on the database platform you're using. Each platform will have its own data types and other idiosyncrasies, so you'll need to do this anyway.

## Statements and Transactions
When you run a query against a database, the SQL text sent to the server is called a "statement". There are four main types of statements: `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. Each statement is considered a single operation from the perspective of the database server. Several statements can be run in a [transaction](https://en.wikipedia.org/wiki/Database_transaction), which can be rolled back if you decide you don't want to make changes or committed if you want the changes to persist in the database. Most often, your connection will default to "auto-commit", where any changes you make will be committed to persist in the database automatically. You can change this behavior when you connect, though this is likely a rare need for a data scientist.

Something worth noting: SQL itself is case-insensitive. `SELECT` is the same as `select`. Often times, you'll see SQL keywords in all capitals. This is due to just old programming habits and for readability of SQL versus data. Personally, I use capitals when talking about the SQL language but lower-case in my actual queries. There's no right or wrong way to do it. However, do be aware that the data _is_ case sensitive.

## Getting Data
Retrieving data is done with the `SELECT` keyword. The results of your statement will usually consist of the data you specify along with some metadata, like how many records were returned and if there are any warnings regarding your query. Let's go through an example and break it down piece by piece.

```sql
select
  name,
  phone_number
from employee
```

This is a very simple `SELECT` statement. It starts with `SELECT` followed by a list of the fields you want from the table, separated by commas. Whitespace does not matter. You can have newlines, tabs, spaces, etc wherever you want. Following the field list, you need a `FROM` phrase starting with `FROM` followed by the name of a table. This specifies the table you want to pull data from. In the above example, you're going to the name and phone number of every employee record. What if we wanted to get this info for an employee with the name "Jazzy"?

```sql
select
  name,
  phone_number
from employee
where name = 'Jazzy'
```

This is a little redundant, since we know the name we're looking for. To filter data, we can use the `WHERE` phrase. The `WHERE` phrase consists of `WHERE` followed by some condition. The database system will check the result of the condition for each record. If the condition is true, that record will be included in the results. There's some syntax to be aware of here. Notice that in SQL, we use a simple `=` for comparison, not `==`. SQL can make this distinction between comparison and assignment thanks to the phrase-based nature of the language. Notice also that text data uses single quotes `'` in SQL. This can sometimes trip people up when switching between a programming language and SQL. Keep this in mind.

What if you want more complicated conditions?

```sql
select
  name,
  phone_number
from employee
where (name = 'Jazzy' and department_id = 1 ) or phone_number = '010-7777-7777'
```

The `WHERE` phrase supports the `AND` and `OR` operators, along with parenthesis to group logic. Conditions inside the innermost parenthesis will be evaluated first. In the above example, we'll receive records that have both the name Jazzy and 1 as the department id or records with the phone number 010-7777-7777. Let's burn through more examples.

```sql
select
  *
from employee
where name in ('Jazzy', 'Beege')
  and email like '%@gmail.com'
```

This will select all fields `*` where the name of the employee is either `Jazzy` or `Beege` and the email ends in `@gmail.com`. The syntax `IN (...)` will be true if the field matches any of the values listed between parenthesis. The `LIKE` condition allows the use of wildcards `%` to search for data.

```sql
select
  phone_number as phone
from employee
where department_id in (select id from department where department_head_id = 5)
```

We're getting a little crazy here. The `IN (...)` will match any value in the parenthesis, yes? We can use another select statement to create these values. In this case, there are actually better ways to accomplish this, but this is a good demonstrate of the technique. This is called a sub-select. We'll give better examples of sub-selects later. We're also renaming a field here. In our output, `phone_number` will instead be labeled `phone` for whatever system we're using to get the data out of the database.

## Joining Data
You learned about normalization earlier, but how do you get data from these disparate tables to show up together? SQL has a `JOIN` phrase for making this happen. Let's try it.

```sql
select
  *
from employee e
join department d
  on e.department_id = d.id
```

This will combine data from the `employee` and `department` tables based on the employee's `department_id` and the department's `id`. The means that a record from the employee table will be linked to a record from the department table if the employee record's `department_id` and the department's `id` are the same. If there are multiple employees that have the same department id, the department record will be duplicated in the output for each employee. Also, for ease, you can alias table names. Above, I aliased `employee` as `e` and `department` as `d` so I could reference their fields more easily. Some people don't like this as they feel it reduces readability. It's also unnecessary to specify the table for a column if the column name is unique among all of the tables. In the above example, since both `employee` and `department` have a column named `id`, we need to specify the table that we want the id from. It wasn't necessary to prepend `department_id` with `e`, since the `employee` table is the only one in this statement that has a column named `department_id`. It's just my style choice to specify the table in this case.

We can still use other elements of select. Let's replicate the sub-select example using `JOIN`.

```sql
select
  e.phone_number as phone
from employee e
join department d
  on e.department_id = d.id
where d.department_head_id = 5
```

Here, we'll get all employees' phone numbers whose department has a department head with id 5.

Something worth noting: SQL statements are evaluated as a whole, with the exception of sub-statements (like sub-selects), which will be evaluated first. The join, the field selection, and the filtering should happen all at the same time from your perspective. Under the hood, this is not the case. The database will filter data in whatever order leads to the fastest result, deciding the path to take based on filtering logic, indexes, partitions, etc. It used to be the case that you needed to specify something like the department head filtering as another condition within the `ON` phrase in order for that filter to happen before joining _all_ departments to _all_ employees, but today's databases are smart enough to apply the filter before joining data if that's more efficient.

We can also join multiple times.

```sql
select
  *
from employee e
join employee_responsibility er
  on er.employee_id = e.id
join responsibility r
  on r.id = er.responsibility_id
join department d
  on d.id = e.department_id
```

This will get all employees with all of their responsibilities and their department. Now, since an employee will have many responsibilities, employees will be duplicated when they have more than one responsibility. Let's make this nicer.

```sql
select
  e.name,
  e.phone_number,
  e.email,
  d.name as department_name,
  dh.name as manager_name,
  GROUP_CONCAT(r.name SEPARATOR ', ')
from employee e
join employee_responsibility er
  on er.employee_id = e.id
join responsibility r
  on r.id = er.responsibility_id
join department d
  on d.id = e.department_id
join employee dh
  on d.department_head_id = dh.id
group by
  e.name,
  e.phone_number,
  e.email,
  d.name,
  dh.name
```

Now we're getting a little advanced. Let's go over what's going on here:
* We're joining employee to itself via department. This last join represents the head of the department. Joining a table to itself is perfectly fine, whether directly or indirectly.
* The [`GROUP_CONCAT`](https://dev.mysql.com/doc/refman/8.0/en/group-by-functions.html#function_group-concat) function is used for grouping multiple values into a single string. All of the values `r.name` will be put together into one string with `, ` separating them, leading to a nice, comma-delimited list.
* We're using `GROUP BY` to allow the grouping of responsibilities. The `GROUP BY` phrase is used for aggregate functions, like `GROUP_CONCAT`, `MIN`, `MAX`, `AVG`, and many more. This means that all results that share the same fields listed in the `GROUP BY` phrase will be grouped together. Any other fields will either show the first encountered value or an aggregate value. Make sure not to forget to put the right fields in `GROUP BY`!

All of these `JOIN` statements have been an `INNER JOIN`. `INNER JOIN` will only give you values that have matching records for the `ON` phrase. If you have an employee in the above example with no responsibilities or no department, the employee would not show up in the results. If you want to join two tables even if there's no match in one of them, you need an `OUTER JOIN`. These are either `LEFT JOIN` or `RIGHT JOIN`. If we used a `LEFT JOIN` from `employee` to `employee_responsibility`, we would still get all of our `employee` records, even if there was no matching `employee_responsibility` record. Alternatively, if we used a `RIGHT JOIN`, we would get all `employee_responsibility` records, even if there was no corresponding `employee` record.

Lastly, there's `CROSS JOIN`, which will give you all possible combinations of records between the two sides of the join. This requires no `ON` phrase, since there's no matching between records. 
