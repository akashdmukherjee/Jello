import psycopg2
import csv
import json

try:
    conn = psycopg2.connect("dbname='omemqnfx' user='omemqnfx' host='elmer.db.elephantsql.com' password='8VSwANQ4OPI-pMDU5zGKbgOe4MtHZ369'")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()


def getItems():
    print ("=================Entered getItems=================")
    #print (request)
    #param = request.values.get("param")
    
    # Read
    sql_query = """ 
                    SELECT * 
                    FROM webapp.items 
                """
    
    cur.execute(sql_query)
    rows = cur.fetchall()
  
    data = []

    for row in rows:
      obj = {}
      obj["item_id"] = row[0]
      obj["item_name"] = row[1]
      obj["item_image"] = row[2]
      data.append(obj)

    #data_json = {"datakey": data}
    data_json = json.dumps(data)
    print(type(data_json))
    print (data_json)
    return data_json