

### basic concepts: 
- relational design: https://web.mit.edu/11.521/www/lectures/lecture10/lec_data_design.html
- entity-relationship : http://web.mit.edu/11.521/www/sqlnotes/referential_integrity.html
- https://geekgirls.com/category/office/databases/

### basic query examples:
https://www.javatpoint.com/mysql-queries
https://sqlzoo.net/wiki/SELECT
https://www.mysqltutorial.org/mysql-subquery/
https://www.mysqltutorial.org/mysql-datetime/
https://www.mysqltutorial.org/mysql-show-processlist/

http://web.mit.edu/11.521/www/sqlnotes/sqlhelp.html

```sql
--specify primary key
ALTER TABLE students ADD CONSTRAINT pk_studentid PRIMARY KEY (studentid);

-- drop tables 
drop table stu_cou  CASCADE CONSTRAINTS;
drop table tea_cou  CASCADE CONSTRAINTS;

-- Create Table with Constraints
create table students
(studentid number(9,0) CONSTRAINT pk_students PRIMARY KEY,
 fname varchar2(20), 
 lname varchar2(20),
 department varchar2(30),
 year number(1,0),
 email varchar2(30),
 phone varchar2(20),
 height number(3,0) 
);

create table teachers
(teacherid number(9,0) CONSTRAINT pk_teachers PRIMARY KEY,
 fname varchar2(20),
 lname varchar2(20),
 email varchar2(30),
 phone varchar2(20),
 office varchar2(20),
 hours varchar2(20)
);


-- Specify Primary Key (Multi-columns)
ALTER TABLE tea_cou 
	ADD CONSTRAINT pk_tea_cou PRIMARY KEY (teacherid,courseid);

ALTER TABLE stu_cou
    ADD CONSTRAINT pk_stu_cou PRIMARY KEY (studentid,courseid);

-- Specify Foreign Key
ALTER TABLE tea_cou
    ADD CONSTRAINT fk_teacherid
    FOREIGN KEY (teacherid)
    REFERENCES teachers (teacherid);

ALTER TABLE stu_cou
	ADD CONSTRAINT fk_studentid
	FOREIGN KEY (studentid)
	REFERENCES students (studentid);

-- Drop Tables
drop table students CASCADE CONSTRAINTS;

```



#### ALTER TABLE
    - https://www.mysqltutorial.org/mysql-add-column/
    - https://stackoverflow.com/questions/14500911/add-new-column-in-table-with-value-depending-value-of-another-column-in-same-tab
    - https://stackoverflow.com/questions/14500911/add-new-column-in-table-with-value-depending-value-of-another-column-in-same-tab#14500957
    - http://www.tutorialspoint.com/mysql/mysql-alter-command.htm
    - https://stackoverflow.com/questions/27352332/populate-a-column-based-on-another-column
    - https://stackoverflow.com/questions/18312429/how-to-create-add-a-column-in-an-sql-select-query-based-on-another-columns-valu#18312544
    - https://stackoverflow.com/questions/61700149/alter-table-add-column-as-select
    - https://stackoverflow.com/questions/18312429/how-to-create-add-a-column-in-an-sql-select-query-based-on-another-columns-valu

#### ERROR1406: 
    - > define dtype and max.value.length when you create a new table/column
    - reference: https://dev.mysql.com/doc/refman/8.0/en/char.html
    https://www.tutorialspoint.com/fix-for-mysql-error-1406-data-too-long-for-column-but-it-shouldn-t-be
    https://stackoverflow.com/questions/34418870/error-1406-1406-data-too-long-for-column-but-it-shouldnt-be
    https://forums.mysql.com/read.php?20,73012,73084 