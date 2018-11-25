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

create table call_log (
  call_time timestamp not null default current_timestamp,
  employee_id int not null,
  origin_number varchar(13) not null,
  duration_seconds int not null,
  primary key (call_time, employee_id),
  index call_log_reverse_index (employee_id, call_time),
  index call_log_index_origin_number (origin_number)
);

insert into call_log
values
('2018-11-25 12:00:00', 1, '010-5555-5555', 30),
('2018-10-25 12:00:00', 2, '010-5555-5555', 20),
('2018-10-25 12:00:00', 3, '010-5555-5556', 300),
('2018-11-25 11:00:00', 2, '010-5555-5555', 600),
('2018-11-26 12:00:00', 3, '010-5555-5556', 10),
('2018-11-26 12:00:00', 1, '010-5555-5555', 60),
('2018-11-26 13:00:00', 1, '010-5555-5555', 90),
('2018-11-25 12:00:00', 3, '010-5555-5557', 3600),
('2018-11-15 15:00:00', 1, '010-5555-5555', 300),
('2018-11-15 13:00:00', 1, '010-5555-5556', 600),
('2018-11-15 16:00:00', 2, '010-5555-5556', 45),
('2018-11-25 14:00:00', 1, '010-5555-5556', 60),
('2018-11-25 12:00:00', 2, '010-5555-5555', 270),
('2018-11-25 17:00:00', 2, '010-5555-5557', 30),
('2018-11-25 10:00:00', 3, '010-5555-5557', 90),
('2018-11-25 13:00:00', 3, '010-5555-5557', 30);
