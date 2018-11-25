# Getting Data
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
where (name = 'Jazzy' and department_id = 1 ) or phone_number = '010-7777-7778'
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
where department_id in (select id from department where department_head_id = 1)
```

We're getting a little crazy here. The `IN (...)` will match any value in the parenthesis, yes? We can use another select statement to create these values. In this case, there are actually better ways to accomplish this, but this is a good demonstrate of the technique. This is called a sub-select. We'll give better examples of sub-selects later. We're also renaming a field here. In our output, `phone_number` will instead be labeled `phone` for whatever system we're using to get the data out of the database.
