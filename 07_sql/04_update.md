# Update
Now we're getting into scary stuff. `UPDATE` statements are how you can change data in your database. You should _always_ take care when doing this. If you write an `UPDATE` statement incorrectly, you could irrevocably mangle your data. This may be a good time to read up on [transactions](https://en.wikipedia.org/wiki/Database_transaction), for safety. I tend not to use transactions, but that's because I'm a cowboy. You're smarter than me. Use transactions. Okay, let's get to it.

```sql
select * from employee
where name = 'Beege';
```

This isn't a valid `UPDATE` statement. Surprise! This is how I first write my `UPDATE` statements. I first make sure my filter is accurate. If this query doesn't return the records I want to change, I've made sure that I haven't accidentally changed data I didn't intend to. Yeah, yeah, I'm not quite a cowboy. Next, I edit this `SELECT` statement to become an `UPDATE`.

```sql
update employee
set email = 'beegimus_maximus@gmail.com'
where name = 'Beege';
```

_This_ is a valid `UPDATE` statement. This will change the email to "beegimus_maximus@gmail.com" for all records with a `name` as "Beege". (For all you Github trolls, that is not my email. Sorry.) **NOTE**: if the `WHERE` phrase was omitted, **ALL** records' emails would be changed. There is no undo. There is no reset. Do not make this mistake. This is scary. It's supposed to be scary. It's okay, you can do it. As long as you're careful and take some time to practice (and maybe use a transaction), you'll be just fine.

Believe it or not, we can get fancier.

```sql
update employee e
set e.name = CONCAT('Marketer ', e.name)
join department d
on e.department_id = d.id
where d.name = 'Marketing'
```

Yes, we can use `JOIN` phrases in our `UPDATE` statements as well. It works exactly as you would expect it to. One thing to keep in mind is that `JOIN` filtering behavior still happens. If there was an employee without a matching department, they would be skipped for update. In this case, it makes sense since we're keying off of the department's name, but it's helpful to keep in mind for other cases.

Okay, one more `UPDATE` example.

```sql
update employee e, department d
set e.name = CONCAT('Marketer ', e.name),
    d.name = 'Randos'
where e.department_id = d.id
```

We can update multiple tables simultaneously using the above syntax. To accomplish a normal `JOIN`'s `ON` phrase, we can toss the condition into `WHERE`. In any `UPDATE` statement, you can update multiple fields by separating your field changes with commas.

That actually covers the most common use cases of `UPDATE` statements in SQL. Good job!
