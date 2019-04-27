import psycopg2
from sqlalchemy import create_engine
import csv
import json

db_string = "postgres://omemqnfx:8VSwANQ4OPI-pMDU5zGKbgOe4MtHZ369@elmer.db.elephantsql.com:5432/omemqnfx"
db = create_engine(db_string)


def getData():
    print ("=================Entered getData=================")
    #print (request)
    #param = request.values.get("param")
    
    # Read
    result_set = db.execute("SELECT * FROM webapp.items")  
    for r in result_set:  
      print(r)

    #data_json = {"datakey": data}
    #data_json = json.dumps(data_json)
    #print (data_json)
    return data_json