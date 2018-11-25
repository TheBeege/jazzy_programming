# Aggregations
Next, we'll go over aggregations, which is the most likely type of query you'll be running for either data analysis or data science. Essentially, we'll be focusing on writing `SELECT` statements that aggregate and summarize data in a meaningful way to show to customers within your organization. Put on your smart-looking glasses, cuz we 'bout to do some SCIENCE! (But not data science, cuz I don't actually know how to do that shit.)

First, let's setup a new table that we might want to do analytics on:

```sql
  create table call_log (
    call_time timestamp not null default current_timestamp,
    employee_id int not null,
    origin_number varchar(13) not null,
    duration_seconds int not null,
    primary key (call_time, employee_id),
    index call_log_reverse_index (employee_id, call_time),
    index call_log_index_origin_number (origin_number)
  );
```

Let's setup a new [DB-Fiddle](https://www.db-fiddle.com/f/asg5kM7LBkMJLKgvizTyyK/0) for you based on this.

Alright, so your boss wants to know which department gets the most phone calls. Let's write a query to find this out.

```sql
select
  d.name,
  count(1) as count_calls
from department d
join employee e
on e.department_id = d.id
join call_log l
on l.employee_id = e.id
group by d.name
```

There's no direct connection from department to call_log, so we have to go through employee. It doesn't matter if we start from department or from call_log. The database optimizer is smart enough under the hood to take care of efficiency of join order for you. You just need to make sure your logic is accurate. First, we grab all departments. Next, we connect those to the departments' employees. Lastly, we link those employees to the calls they've received. Once we've got the data connected, we can do our aggregation. It's sometimes helpful to verbalize what you want to help you get the right query. In this case, we want the "count of calls by department". We're doing the "<aggregate> of <measuring entity> by <grouping entity>". The <aggregate> is your aggregate function, in this case, `COUNT`. The <measuring entity> is the field you want to measure. Since we're counting, we just care about the number of records returned. The field doesn't matter. Lastly, we're grouping by the <grouping entity>, in this case, department. Since departments are unique by name, we can just group by their name. You need to also make sure you group by whatever you want to display, otherwise you'll get weird behavior.

Note also that we did `COUNT(1)`. This is shorthand. The `1` is actually the first field returned by the statement. Since we're counting records, it doesn't actually matter which field you specify. However, what if you wanted to count the number of distinct callers per department?

```sql
select
  d.name,
  count(distinct l.origin_number) as count_distinct_callers
from department d
join employee e
on e.department_id = d.id
join call_log l
on l.employee_id = e.id
group by d.name
```

This query will show the number of distinct callers per department. We're counting only `DISTINCT` instances of the origin number. This is especially useful, but I strongly recommend it only be done on indexed fields, similar to any `GROUP BY` phrases.

What if we wanted to see the total number of hours each employee has spent on the phone?

```sql
select
  d.name as department,
  e.name as employee,
  round(sum(l.duration_seconds)/60) as total_call_duration_minutes
from department d
join employee e
on d.id = e.department_id
join call_log l
on e.id = l.employee_id
group by
  d.name,
  e.name
```

We have a few things going on here. We're using a new aggregate function, `SUM`. We're also using a number function `ROUND` to round the result of our division up to a whole number. Note that you should do your summation before your mathematical operations. If you have a lot of calls that are 89 seconds, for example, you could end up missing a large amount of time over a lot of records.

How about average number of calls per day of the week?

```sql
select
  dayname(call_date),
  avg(count_calls)
from (
  select
    date(call_time) as call_date,
    count(1) as count_calls
  from call_log
  group by
  	date(call_time)
) as calls_per_day
group by
  dayname(call_date)
```

This is new. We're doing a sub-select inside our `FROM` phrase. Let's look at the sub-select first:

```sql
select
  date(call_time) as call_date,
  count(1) as count_calls
from call_log
group by
  date(call_time)
```

This gives us our total number of calls per date. Inside the larger query, we wrap this in parentheses and toss an `AS ...` at the end. This creates a "virtual table". The database creates a temporary table out of our select statement that it can use for further operations. It all happens in memory, so it's usually pretty fast, as long as the data isn't too large. It's a good idea to make sure that sub-selects are a limited set of data, like an aggregation. If your sub-select takes up too much memory, it will end up swapping to disk, bringing your query performance to a crawl. However, once we have our sub-select setup, we can treat it just like a table whose columns are the field aliases from the sub-select. From there, we just average the number of calls by the `DAYNAME()` of the call date. Fancy.

Again, sub-selects are virtual tables, so you can use them in `JOIN` phrases as well. This is helpful if you need to do joins of data or filtering based on aggregations.

See if you can come up with more interesting aggregations that you may want to report to a stakeholder or manager. 
