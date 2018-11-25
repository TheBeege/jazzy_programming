# Relational Database Design
Relational databases are arguably the most popular database system in use today. They allow you to have disparate data that's relatable to each other with minimal duplicate data and accessible at high speeds. SQL, or structured query language, is the most common interface language for relational database systems. Here, we'll cover concepts in relational databases and use a simple development databases called SQLite3.

## The Structure of a Relational Database
Relational databases have several ways of grouping data. Within a database server or cluster of servers, there's often the concept of a schema, sometimes also called a database. A schema, at a high level, is a way to group different types of data, either logically or according to some technical requirements like storage location or character set.

Within a schema, you then have tables. Tables is where all of the magic happens. Similar to CSV files, tables have the concept of rows and columns. Rows are also called records. Columns are also called fields, and they must be defined when you define the table. Fields can be altered, but doing this can make life miserable very quickly. It's worth putting up-front thought into table design to save yourself pain later on.

Each field within a table must have a name and data type. Data types can be things like integer, varchar (variable character, or basically, limited text), boolean, and more.

Each table must have a primary key. A primary key determines the order in which data is stored in the table and serves as the identifier for a given row. This primary key is often just a selected field, though you can also have composite primary keys, consisting of multiple fields.

## Creating Tables
Let's check out a table definition:
```sql
create table person (
    id int auto_increment,
    name varchar(255),
    is_admin boolean,
    primary key (id)
)
```

Be aware that this is a MySQL dialect of SQL. ANSI SQL's (standard SQL) more recent updates deviate from this, since the updates were made after several database systems were already well established. When trying out a new database system, make sure to check the syntax for various features.

This statement will create a table called `person`. It will have 3 columns. The first will be called `id` and will store `integer` data. It will increase by 1 each time a new record is created, assuming it isn't specified. It also has a `name` field which can be up to 255 characters long for latin characters. Other text in utf-8 may require more space, so you should plan accordingly depending on the size of the text you'll be storing. The `is_admin` column is a boolean (true/false) column. Lastly, the `id` field will be the primary key. When storing data, the database will store it according to the `id` column. Each `id` _must_ be unique. Attempting to create a new record with a duplicate `id` will give you an error. In a table like this, you'll want to omit the `id` when creating a new record and let the database create it for you. This saves you headaches and is very efficient.

## Indexes for Great Speed
The above `person` table will work great for a simple application. However, if you end up getting millions of `person` records and often lookup people by `name`, you'll notice things will being to get slow. When searching for data, a database will use indexes to find records. Primary keys are indexes by definition, so any lookups by id will be near-instant. However, when there are lookups for fields that don't have an index, the database will have to scan all of the data in the entire table to try and find the right records. This is can make your life a nightmare if not handled correctly. This is why we're covering indexes before we even learn how to lookup data.

Let's take a look at how we would define this table if we knew we'd be looking up records by the `name` field:
```sql
create table person (
    id int auto_increment,
    name varchar(255),
    is_admin boolean,
    primary key (id),
    index person_index_name (name)
)
```

This will create the table with an index on the `name` column. The text `person_index_name` is the name of the index, which must be unique throughout the whole database. To this end, I prefer to use `<table>_<index type>_<column>` as my index names, to prevent name collisions. This is a simple index, so I just use `index`. We'll cover other types later. Using this table definition, any lookups by `name` will also be near-instant.

So why don't we just define indexes for every column? Again, speed. For each index you add to a table, create or updating data in that table gets slowed down. You don't want to overload tables with indexes. You should make sure to figure out how you'll access your tables in advance and plan your indexes accordingly.

In additional to simple indexes, there are unique indexes, which will enforce that each record of data has a unique value. Here's an example:
```sql
create table person (
    id int auto_increment,
    name varchar(255),
    is_admin boolean,
    primary key (id),
    unique index person_index_name (name)
)
```

This will create an index just like above, but it will also enforce that each record's `name` field is unique. If there's an attempt to create a new record with the same `name`, the database will spit out an error.

## Partitions, Also Speed
Partitions are also something that needs to be considered up front. Traditionally, databases would store table data in one file on the disk. When the file gets really huge, efficiency can degrade very quickly. To solve this, the idea of partitions was created. Partitions are rules by which the database should split up tables into multiple files. Akin to indexes, this requires a balance. Having tons of tiny partitions will cause the database to open tons of files unnecessarily, while keeping your partitions too large can make finding data slower.

Partitions are really complicated and vary on a case-by-case basis. I've mostly only used partitioning on time-series data, that is, data primarily organized by time. For example, if I have a table like below:
```sql
create table server_status_report (
    create_timestamp timestamp,
    server_id int,
    is_alive boolean,
    count_requests int
    primary key (create_timestamp, server_id)
)
```

It's highly likely that this table would become _huge_, especially if I have a large number of servers and am receiving status reports every minute. The structure of this table is highly conducive to partitioning. I care about data specifically by time, and the table will grow to be very large. Let's take a stab at partitioning this.
```sql
create table server_status_report (
    create_timestamp timestamp,
    server_id int,
    is_alive boolean,
    count_requests int
    primary key (create_timestamp, server_id)
) partition by hash (DATE(create_timestamp))
partitions 30;
```

This would partition the table into 30 partitions by date, meaning we'd have 30 files representing this table, each file containing 1 day's worth of data. Be aware that __this specific example is very naive__. You'll want to read up on partitioning in greater detail specific to your use case. You'll also likely need some sort of maintenance system to manage your partitions.

## A Note on Table Management
You should have some degree of familiarity with these things, but ideally, your organization should have data engineers to manage these things for you. Data engineers specialize in acquiring, storing, and managing data. Things like partitioning should be under their purview, but responsibilities will always vary across organizations. If your organization does have dedicated data engineers, you should make sure to build a strong relationship with them as quickly as you can. Ensuring that data setup in a manner that makes your job easy is critical to your success. Be friends with your data engineers. Make them want to make your life easier. Your job is to derive insights from data, not muck around with how exactly it sits on a disk; however, some base knowledge of these topics will help you communicate with your data engineers and garner you some respective for having knowledge in their craft.

## Schema Design
Now you know how to create tables and design individual tables with at least some degree of effiency, but how do you define multiple tables in a way that makes sense? Why is it called a relational database?

Schema design should follow the concepts of [database normalization](https://en.wikipedia.org/wiki/Database_normalization). Normalization is the idea of splitting up data in a manner where repetition is reduced, and therefore data storage and maintenance are reduced. To make things work, database queries will join tables together to assemble the data needed. Be aware that application databases will often have a pretty high amount of normalization. The way applications access data makes splitting out data a good thing. However, data warehouses normally have __de__normalized data. They will intentionally duplicate data in order to eliminate the need for joining tables. When operating at huge scales, table joins can be costly.

Let's show some examples of normalized and denormalized schemas.

```sql
create table employee (
    id int auto_increment,
    name varchar(255) not null,
    phone_number varchar(13) not null,
    email varchar(255),
    department_id int,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    primary key (id),
    index employee_index_name (name)
);

create table department (
    id int auto_increment,
    name varchar(255) not null,
    department_head_id int not null,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    primary key (id),
    unique index department_unique_index_name (name)
);

create table responsibility (
  id int auto_increment,
  name varchar(255) not null,
  description text not null,
  created_at timestamp not null default current_timestamp,
  updated_at timestamp not null default current_timestamp on update current_timestamp,
  primary key (id),
  unique index responsibility_unique_index_name (name)
);

create table employee_responsibility (
  employee_id int,
  responsibility_id int,
  primary key (employee_id, responsibility_id),
  unique index employee_responsibility_reverse_index (responsibility_id, employee_id)
);
```

This is a typical, basic, normalized database schema. Data that could be duplicated lives in separate tables. This way, we don't actually need to duplicate the data. We can relate tables with data that would be repeated to the tables that need the data. For example, we can connect the `department` and `employee` tables based on the `department_id` in the `employee` table in order to get the departments for each employee. This is common in applications due to multiple advantages. The most major one is that if a department name ever changes, we only need to update data in the department table. It also saves on disk space, which is helpful for application database that you don't want to get too large.

You can see this schema in action using [DB-Fiddle](https://www.db-fiddle.com/f/pQkEECzSsz96MLYjoNEKJE/0), an online tool for experimenting with SQL. I recommend using later SQL examples with this to see how things work.

However, once you get into the millions magnitude of database records, trying to do reporting across all of these tables together would be challenging. Here's the same data in a denormalized format, which would be helpful for reporting performance.

```sql
create table employee (
    id int auto_increment,
    employee_name varchar(255) not null,
    phone_number varchar(13) not null,
    email varchar(255),
    employee_created_at timestamp not null,
    employee_updated_at timestamp not null,
    department_name varchar(255) not null,
    department_head_name varchar(255) not null,
    department_head_phone_number varchar(13) not null,
    department_head_email varchar(255),
    department_head_created_at timestamp not null,
    department_head_updated_at timestamp not null,
    responsibilities_names varchar(255) not null,
    count_responsibilities int not null,
    insert_timestamp timestamp not null,
    primary key (id),
    index employee_index_name (employee_name),
    index employee_department_index_name (department_name),
    index employee_responsibilities_names (responsibilities_names),
    index employee_insert_timestamp (insert_timestamp)
);

create table department (
    id int auto_increment,
    department_name varchar(255) not null,
    department_head_name varchar(255) not null,
    department_head_phone_number varchar(13) not null,
    department_head_email varchar(255),
    department_head_created_at timestamp not null,
    department_head_updated_at timestamp not null,
    department_created_at timestamp not null,
    department_updated_at timestamp not null,
    count_employees int not null default 0,
    count_employee_responsibilities not null default 0,
    count_responsibilities not null default 0,
    avg_count_responsibilities_per_employee not null default 0,
    median_count_responsibilities_per_employee not null default 0,
    insert_timestamp timestamp not null,
    primary key (id),
    unique index department_unique_index_name (name),
    index department_insert_timestamp (insert_timestamp)
);

create table responsibility (
  id int auto_increment,
  name varchar(255) not null,
  description text not null,
  created_at timestamp not null default current_timestamp,
  updated_at timestamp not null default current_timestamp on update current_timestamp,
  count_employees int not null 0,
  count_departments int not null 0,
  insert_timestamp timestamp not null,
  primary key (id),
  unique index responsibility_unique_index_name (name),
  index department_insert_timestamp (insert_timestamp)
);
```

You'll notice this is much more verbose. We call this "wide" tables. If we were to put these into a spreadsheet with the fields as columns, the spreadsheet would be very wide. You'll notice that there is a large amount of duplicate data. There are also some aggregations, mostly counts and averages. A reporting database is not the initial destination for data. Often, the data is exported (or ETLed - extracted, transformed, and loaded) from an application database. When we do this export, we can calculate these aggregations. You'll also see an `insert_timestamp`. Rather than frequently update the reporting database, which could lead to data discrepancies among duplicated data, engineers will do nightly "snapshots" of data. They take a snapshot of the application database at some point in time and export that to the reporting database. This is cleaner and safer than doing on-the-fly updates. There are organizations that are exceptionally mature and capable that can do on-the-fly reporting database updates, but they are in the minority. Due to this, we include the `insert_timestamp` as an indexed column in order to see the state of data from day to day, if there are nightly snapshots. This allows you to easily report on the current state of the data or on how data has evolved over time.

Be aware that not all organizations will have data warehouses with denormalized data like this. If you don't start in a full-fledged data scientist job (or more likely, if a company hires you as a data scientist but is only capable of supporting a data analyst), a data warehouse with a denormalized schema like this may not exist. In such cases, you'll either need to work with the application database or wokr with engineers to create a reporting database.

### Normalizing Data
You saw an example of a normalized database schema, but we haven't covered the strategies and reasoning around normalizing data. If you're in an organization with data warehousing infrastructure already, you likely don't need this knowledge. However, it will be absolutely critical if you're working in a less mature organization.

Normalization is based on relationships between data. There are three key relationships:
* One-to-One
* Many-to-One / One-to-Many
* Many-to-Many

We'll cover each of these individually.

#### One-to-One Relationships
These are probably the least frequent relationships you'll see normalized. These are cases where one entity has some amount of critical data along with some amount of verbose and non-critical data. A good example is accounts with profiles. An account's critical information may include things like username, password, email, and icon. Non-critical information would be data that doesn't appear as frequently and tends to take up more space. This could include things like personal bio, large profile photo, and additional information that might only show up on their profile page. In this case, we would want to split up an account, which would normally be considered one entity, into two separate tables. Good names may be something like `account` and `account_detail` or `account` and `account_profile`. In one of the tables, you would want to have the id of the corresponding record in the other table. For example, `account_detail` might have an `account_id` column. This allows for the connection between the two tables, but when you only need the critical information, you can just pull data from `account` and not worry about `account_detail`.

#### Many-to-One / One-to-Many Relationships
Many-to-one and many-to-many relationships are inverses of one another. When you have one, you have the other. The normalized schema above is a good example of this. Employees have a many-to-one relationship to departments, and departments have a one-to-many relationship to employees. Rather than repeat the department info for every employee, we just connect each employee to their department whenever we need. In these relationships, we put the id of the "one" in the table of the "many". So here, we put the department id in each employee record.

#### Many-to-Many Relationships
Many-to-many relationships are the most complicated. In order to establish these, you need a third table to relate the two entities with the many-to-many relationship. In our example above, there is a many-to-many relationship between an employee and a responsibility. In order to connect them, we create a third table, `employee_responsibility`, which contains `employee_id` and `responsibility_id`. With this, we can connect many employees with multiple employee_responsibility records, and we can then connect many responsibilities with multiple employee_responsibility records. The `employee_responsibility` table is called a "linking table" in this case. You can also add fields to your linking table to enrich data about the relationship. For example, if you wanted to track when an employee started assuming some responsibility, you could include a `start_date` datetime or timestamp field in `employee_responsibility`. This would be specific to a unique combination of an employee and a responsibility. Lastly, you'll want to put a reverse index on linking tables so that you can lookup data from either direction quickly and easily.

With this information, you should have everything you need to design a traditional relational data warehouse. Next up, we'll cover how to actually interact with the data using sql.
