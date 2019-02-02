# Joining Data
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
where d.department_head_id = 1
```

Here, we'll get all employees' phone numbers whose department has a department head with id 5.

Something worth noting: SQL statements are evaluated as a whole, with the exception of sub-statements (like sub-selects), which will be evaluated first. The join, the field selection, and the filtering should happen all at the same time from your perspective. Under the hood, this is not the case. The database will filter data in whatever order leads to the fastest result, deciding the path to take based on filtering logic, indexes, partitions, etc. It used to be the case that you needed to specify something like the department head filtering as another condition within the `ON` phrase in order for that filter to happen before joining _all_ departments to _all_ employees, but today's databases are smart enough to apply the filter before joining data if that's more efficient.

We can also join multiple times. To do so, you simply repeat the `join` and `on` clauses for each `join` you need.

*Exercise 02-01*: Can you write a query that joins the `employee` table, the `employee_responsibility` table, and the `responsibility` table, in that order and return the employee name and the responsibility name? The `employee_responsibility` table has fields `employee_id` and `responsibility_id` for you to use. The `responsibility` table also has an `id` field. For clarity, rename the responsibility `name` to `responsibility`. ([Answer](answers.md#02-01))

Since an employee will have many responsibilities, employees will be duplicated when they have more than one responsibility. You'll see this in your results.

Let's make this nicer.

```sql
select
  e.name,
  e.phone_number,
  e.email,
  d.name as department_name,
  dh.name as manager_name,
  GROUP_CONCAT(r.name SEPARATOR ', ') as responsibilities
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

You can also have multiple conditions in a join's `on` clause. You can use `and` and `or` just like in a typical `where` clause.

*Exercise 02-02*: Can you write a query to get the employee name and department name using a `left join` from the `employee` table to the `department` table but only when the department name is `Business Development`? Rename the department's `name` field to `department`. ([Answer](answers.md#02-02))

Lastly, there's `CROSS JOIN`, which will give you all possible combinations of records between the two sides of the join. This requires no `ON` phrase, since there's no matching between records.
