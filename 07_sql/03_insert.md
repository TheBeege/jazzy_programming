# Adding Data
Now that you know how to get data out, you should know how to get data into a database in the first place. To add data to a table, we use `INSERT` statements. You may have noticed a few of them in the SQLFiddle link. We'll cover them in detail now. Let's hop right in.

```sql
insert into employee (name, phone_number, email, department_id)
values
('Joe', '010-7777-7775', 'joe@gmail.com', 2);
```

Say hello to Joe in marketing. We've created a new employee. (Note that to try this in SQLFiddle, it needs to be in the left pane.) This will insert a new record into the `employee` table. `INSERT INTO` is the statement for adding new data to a table. Following the keywords is the table name and the list of fields whose values you want to specify inside parenthesis. If you want to specify every field, you can omit the parenthesis and their contents, but you'll usually only want to set some fields and let the database do the rest. After the fields to insert, you can use the keyword `VALUES` followed by the values of the specified fields again surrounded by parenthesis. The id will automatically be set, since we gave it the `auto_increment` property at creation of the table. The `created_at` and `updated_at` fields will also be set according to their default values.

Pretty straightforward, but we can do more.
```sql
insert into employee (name, phone_number, email, department_id)
values
('Janet', '010-7777-7774', 'janet@gmail.com', 2),
('Bridgette', '010-7777-7773', null, 1);
```

In the `VALUES` phrase, you can insert multiple records at once by just separated the parenthesis groups with commas. You can also specify `null` values if you want to set the value for one record but not another, assuming the table allows nulls for the given field.

There's one more kind of insert that will probably be the most valuable to you as a data scientist:
```sql
insert into employee (name, phone_number, email, department_id)
select 'Felix', '010-7777-7779', 'mista_felix@gmail.com', id from department where name = 'IT';
```
This is an insert based on a select statement. Using this, you can easily transform data. This is especially useful if you're working with data engineers to ETL (remember extract, transform, load? also see ELT - extract, load, transform) data from an application database to your reporting database or data warehouse. Like above, you can specify hard-coded values in addition to data selected from other tables. In the above, we're getting the department id from the department table, in case we don't know what the department id is already. One thing to be careful of when combining hard-coded values and select statements: if your select returns multiple records, your hard-coded values will be duplicated. In our case, we know the department name is unique, so there is no danger of that here. You can also get as complex as you want with your select statement. Any statement that returns the appropriate number and types of fields is valid.

With that, you're effectively all set for `INSERT` statements! Nice work
