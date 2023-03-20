import iris
import os
from dotenv import load_dotenv
# host = "k8s-edc81448-a8016263-43619b8c24-04f9d3b32dd23896.elb.us-east-1.amazonaws.com"
# port = 1972
# namespace = "USER"
load_dotenv('.env') 
host = os.environ.get('HOST')
port = 1972
namespace = 'USER'
username = os.environ.get('IRIS_USERNAME')
password = os.environ.get('IRIS_PASSWORD')

conn = iris.connect(host, port, namespace, username, password)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review varchar (150),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP)'
                                 )

# Insert data into the table


sql="INSERT INTO books (title, author, pages_num, review) VALUES('A Tale of Two Cities', 'Charles Dickens', 489,'A great classic!')"

cur.execute(sql)  

sql="INSERT INTO books (title, author, pages_num, review) VALUES('Anna Karenina', 'Leo Tolstoy', 864,'Another great classic!')"

cur.execute(sql)  


conn.commit()

cur.close()
conn.close()