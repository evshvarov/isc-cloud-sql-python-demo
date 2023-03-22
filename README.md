# isc-cloud-sql-python-demo

This is an example of a very simple python-flask application, which works with InterSystems IRIS Cloud SQL server.

## Prerequisits
I consider you deployed InterSystems Cloud SQL and have the name of the host and password for SQLAdmin user.
You should have git installed locally. If not, [here is](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) where you can make it.
you should have Python3 installed locally. Here is [how to install](https://www.python.org/downloads/) if not.

## Running app locally 
1. Git clone the repository.
2. Create venv:
Open terminal in the repository folder and call:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
3. Install  python libs
Run the command below to install packages listed in requirements.txt
```
$ python3 -m pip install -r requirements.txt
```
4. Init local environment variables:
```
$ echo "HOST=your_iris_cloud_sql_host_name" > .env
$ echo "IRIS_USERNAME=SQLAdmin" >> .env
$ echo "IRIS_PASSWORD=password" >> .env
```
Port is hardcoded to 1972 and namespace is hardcoded to "USER" in this demo.
5. Let's create a few records!
Run init_db.py to connect, create a table and add two records:
```
$ python3 init_db.py
```
Let's check if there are records in the database. Connect to the server via irissqlcli:
irissqlcli -h iris_cloud_sql_host -p 1972 -u SQLAdmin -n USER -W
Should be something like that:
```
$[SQL]server:USER> select * from books
+----+----------------------+-----------------+-----------+------------------------+---------------------+
| id | title                | author          | pages_num | review                 | date_added          |
+----+----------------------+-----------------+-----------+------------------------+---------------------+
| 1  | A Tale of Two Cities | Charles Dickens | 489       | A great classic!       | 2023-03-21 16:40:19 |
| 2  | Anna Karenina        | Leo Tolstoy     | 864       | Another great classic! | 2023-03-21 16:40:19 |
+----+----------------------+-----------------+-----------+------------------------+---------------------+
2 rows in set
Time: 0.186s
```
6. Let's run flask app.
$ flask run
Open in browser: http://127.0.0.1:5000/
You should see the small web app listing this two records.



7. Deploying the app to Heroku.
TBD



