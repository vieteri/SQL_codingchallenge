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

## Applying xml data to database
Some key lines fetched from the code

``` py
dom = ElementTree.parse('shipment.xml')
args_list = ([t.text for t in dom.iter(tag)] for tag in ['ToteId', 'SKUId', 'PalletId'])
query = "Insert into line(box, product, pallet) VALUES (%s, %s, %s);"
sqltuples = list(zip(*args_list))
cursor.executemany(query, sqltuples)
``` 

## Setup

Create your own secret.py file where you have the needed fields for connecting to the database you choose.
