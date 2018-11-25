# Delete
I lied. __THIS__ is the scary one. `DELETE` statements are one way of removing data according to a filter. There is also `TRUNCATE TABLE` for deleting all data from a table and resetting auto incrementing values. Here, we'll cover `DELETE` statements.

```sql
delete from employee
where department_id = 2;
```

This will do exactly what you think it does. It will delete all records from the table that have a department id of 2. Again, for safety, I write my `DELETE` statements after getting a `SELECT` statement working. This is much safer.

But what if we want to delete all marketers from all tables? No problem.

```sql
delete from employee, department, employee_responsibility
from employee e
join department d
on e.department_id = d.id
left join employee_responsibility er
on er.employee_id = e.id
where d.name = 'Marketing'
```

This will delete all employee, department, and employee responsibility records for any employees in the marketing department. By specifying a table in the `DELETE FROM` phrase, we are saying to delete records from the table. We could specify a table in `FROM` or `JOIN` phrases for purposes of identifying records without deleting them. Only mentioning them in the `DELETE FROM` phrase will cause records to be removed from that table.

Congratulations! You now have a solid understanding of the 4 main SQL statements: `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
