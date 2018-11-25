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

insert into employee (name, phone_number, email, department_id)
values
('Jazzy', '010-7777-7777', 'jazzy@gmail.com', 1),
('Beege', '010-7777-7776', 'beege@gmail.com', 1),
('Bob', '010-7777-7778', 'bob@gmail.com', 2);

insert into department (name, department_head_id)
values
('IT', 1),
('Marketing', 3);

insert into responsibility (name, description)
values
('Data Science', 'Does magic with data'),
('Being Awesome', 'How can you describe being awesome? This person just is.'),
('Software Engineering', 'Builds stuff using other stuff'),
('Marketing', 'lol');

insert into employee_responsibility(employee_id, responsibility_id)
values
(1, 1),
(1, 2),
(2, 3),
(2, 2),
(3, 4);
