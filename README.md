# SQL codingchallenge

For the job interview the task was to read an xml file and save skuid, pallet and tote to database. I used Python3 and psycopg2 to solve the problem.

## Database

The databse which I use for my solution is provided by free tier elephantsql.

## Creating the required table to store the data
``` sql
CREATE TABLE line(
id SERIAL PRIMARY KEY,
box varchar(255),
product varchar(255),
pallet varchar(255)
);
```


## Setup
  You have to install the correct library corresponding to the database you use
  
  For MariaDB
  ``` python
  pip3 install mariadb
  ```
  For PostgreSQL
  ``` python
  pip3 install psycopg2
  ```
 
  Configure your own database: secret.py
  
  ``` python
    host=*****
    user=*****
    password=*****
    dbname=******
  ```
 
 Connect to your configured database
 
  ``` python
  import secret
  def connect():
    return mariadb.connect(database=secret.dbname, user=secret.user, host=secret.host, password=secret.password)
  ```

## Applying xml data to database
Some key lines fetched from the code

``` py
dom = ElementTree.parse('shipment.xml')
args_list = ([t.text for t in dom.iter(tag)] for tag in ['ToteId', 'SKUId', 'PalletId'])
query = "Insert into line(box, product, pallet) VALUES (%s, %s, %s);"
sqltuples = list(zip(*args_list))
cursor.executemany(query, sqltuples)


 def executequery(query):
      connection = connect()
      cursor = connection.cursor()
      cursor.execute(query)
      if 'SELECT' in query:
          for r in cursor.fetchall():
              print(r)
      connection.close()

``` 

## Read data from database

``` py
   executequery('SELECT * FROM line')
``` 

    
