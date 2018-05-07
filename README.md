# Log Analysis
Log Analysis is a reporting tool that prints out reports (in plain text) based on the data in the database. 


## Features
•	Written in Python 2.7
•	It uses psycopg2 module to connect to the database
•	It provides answers to the following three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?  


## Installation
1.	The tool makes use of the Linux-based virtual machine (VM). Make sure the VM having PostgreSQL database is installed on your system 
2.  Log into the virtual machine using vagrant tool
3.  Run psql -d news -f newsdata.sql command to connect to installed database server on the VM and execute the SQL commands for creating tables and populating them with data
4.	Make sure python as well as python modules(psycopg2) are installed on the virtual machine 
5.	Run the module log_report.py on the VM
6.	You will see the output of the report on the console


## Views Queries Used 
1. create view slugauthor as select name,slug from articles,authors where articles.author=authors.id;
2. create view totreqts as select time::date as date , count(*) as reqts from log group by time::date;
3. create view badreqts as select time::date as date , count(*) as errreqts from log where status like '4%' group by time::date;
