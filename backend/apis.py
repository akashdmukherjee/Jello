import psycopg2
import csv
from flask import Flask, render_template, request
import json

#try:
#    conn = psycopg2.connect("dbname='omemqnfx' user='omemqnfx' host='elmer.db.elephantsql.com' password='8VSwANQ4OPI-pMDU5zGKbgOe4MtHZ369'")
#except:
#    print ("I am unable to connect to the database")

#cur = conn.cursor()


def getPosts():
    print ("=================Entered getPosts=================")
    #print (request)
    #param = request.values.get("param")
    
    # Read
    #sql_query = """SELECT * FROM webapp.items"""
    #cur.execute(sql_query)
    #rows = cur.fetchall()
  
    #data = []

    #for row in rows:
    #  obj = {}
    #  obj["item_id"] = row[0]
    #  obj["item_name"] = row[1]
    #  obj["item_image"] = row[2]
    #  data.append(obj)

    #data_json = {"datakey": data}
    #print (request)
    user_search_string = request.values.get("param")
    
    print ("SEARCHING FOR: ")
    print (user_search_string)

    posts = [
                {"post_id": 1, "post_name":"Capuccino", "post_image": "card-1.png", "post_tags": ["Tech", "Marketing"] }
                , {"post_id": 2, "post_name":"Latte", "post_image": "card-2.png", "post_tags": ["Design", "Produc"]}
                , {"post_id": 3, "post_name":"Irish Coffee", "post_image": "card-3.png", "post_tags": ["Design", "Finance"]}
                , {"post_id": 4, "post_name":"Caffe Mocha", "post_image": "card-4.png", "post_tags": ["Marketing"]}
                , {"post_id": 5, "post_name":"Americano", "post_image": "card-5.png", "post_tags": ["Tech"]}
                , {"post_id": 6, "post_name":"Machiato", "post_image": "card-6.png", "post_tags": ["Tech"]}
                , {"post_id": 7, "post_name":"Espresso", "post_image": "card-7.png", "post_tags": ["Business"]}
                , {"post_id": 8, "post_name":"Iced Coffee", "post_image": "card-8.png", "post_tags": ["Tech"]}
                , {"post_id": 9, "post_name":"Turkish Coffee", "post_image": "card-9.png", "post_tags": ["Tech"]}
                , {"post_id": 10, "post_name":"Cortado", "post_image": "card-10.png", "post_tags": ["Marketing"]}
                , {"post_id": 11, "post_name":"Filter Coffee", "post_image": "card-11.png", "post_tags": ["Tech"]}
                , {"post_id": 12, "post_name":"Ristretto", "post_image": "card-12.png", "post_tags": ["Tech"]}
                , {"post_id": 13, "post_name":"Cafe au lait", "post_image": "card-13.png", "post_tags": ["Tech"]}
                , {"post_id": 14, "post_name":"Cuban Espresso", "post_image": "card-14.png", "post_tags": ["Tech"]}
                , {"post_id": 15, "post_name":"Nescafe", "post_image": "card-15.png", "post_tags": ["Tech"]}
                , {"post_id": 16, "post_name":"Frappuccino", "post_image": "card-16.png", "post_tags": ["Tech"]}
                , {"post_id": 17, "post_name":"Plain Coffee", "post_image": "card-17.png", "post_tags": ["Tech"]}
                , {"post_id": 18, "post_name":"Columbian Coffee", "post_image": "card-18.png", "post_tags": ["Marketing"]}
                , {"post_id": 19, "post_name":"Black Coffee", "post_image": "card-19.png", "post_tags": ["Tech"]}
                , {"post_id": 20, "post_name":"Chai", "post_image": "card-20.png", "post_tags": ["Tech"]}
    ]

    filtered_posts = []

    if user_search_string != None:
        for post in posts:
            if user_search_string.upper() in post["post_name"].upper():
                #filter out posts
                filtered_posts.append(post)
 
        data_json = json.dumps(filtered_posts)
    else:
        data_json = json.dumps(posts)

    #data_json = json.dumps(data)
    #print(type(data_json))
    print (data_json)
    return data_json