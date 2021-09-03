import os
import urllib.parse as up
import mariadb
from xml.etree import ElementTree
import secret
def connect():
    return mariadb.connect(database=secret.dbname, user=secret.user, host=secret.host, password=secret.password)

def pelleilya():
    connection = connect()
    cursor = connection.cursor()
    sql = "SELECT * FROM morningbehaviour ORDER BY dt;"
    cursor.execute(sql)
    for r in cursor.fetchall():
        print(r)
    connection.close()


def parse():
    dom = ElementTree.parse('shipment.xml')
    args_list = ([t.text for t in dom.iter(tag)] for tag in ['ToteId', 'SKUId', 'PalletId'])
    connection = connect()
    cursor = connection.cursor()
    query = "Insert into line(box, product, pallet) VALUES (%s, %s, %s);"
    sqltuples = list(zip(*args_list))
    cursor.executemany(query, sqltuples)
    connection.commit()
    print("Query succeeded")
    connection.close()
    #print(sqltuples)
    
def executequery(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    if 'SELECT' in query:
        for r in cursor.fetchall():
            print(r)
    connection.close()
    
def main():
    txt = input("Please select what you want to do: \n 1. Check on which pallet and box product is on \n 2. Check which products are on pallet \n 3. Check on which pallet a box is on \n 4. Insert data from xml file\n 5. Show table. \n")
    txt = txt.strip()
    if txt=='1':
        product = input("Product id: ")
        product = product.strip()
        query = "SELECT pallet, box FROM line WHERE product='%s'" % product
        executequery(query)
    if txt=='2':
        pallet = input("pallet id: ")
        pallet = pallet.strip()
        query = "SELECT product FROM line WHERE pallet='%s'" % pallet
        executequery(query)
    if txt=='3':
        box = input("box id: ")
        box = box.strip()
        query = "SELECT pallet FROM line WHERE box='%s'" % box
        executequery(query)
    if txt == '4':
        parse()
    if txt == '5':
        executequery('SELECT * FROM line')
main()


# XML sisältää lavoja, laatikoita, laatikoissa tuotteita
# PalletID  eurolava
# Laatikossa voi olla vaan yhtä tuotetta
# Laatikko ei voi olla monessa lavassa
# Lavassa voi olla monta laatikkoa
# toteid = laatikko, skuid = tuote, palletid = lava
'''
create table line(
id SERIAL PRIMARY KEY,
box varchar(255),
product varchar(255),
pallet varchar(255)
);
'''
