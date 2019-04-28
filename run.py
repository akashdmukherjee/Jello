import os
from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
import csv
import json
import re
import datetime
import time
import urllib
import backend.apis
import backend.utils


app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    #my_list = range(101, 207)
    webapp_config = backend.utils.textfile_to_var("config/webapp.config.json", "json")

    return render_template(
                              "home.html"
                            , my_string="akash"
                            , items=backend.apis.getItems()
                            , background_color=("background-color: " + str(webapp_config['website_background'])) 
    )

@app.route("/api/getItems", methods=['POST'])
def api_getItems():
    backend.apis.getItems()

#def getUser_fromDB():
#    cur = db_conn.cursor()
#    try:
#        cur.execute("""SELECT * from bar""")
#    except:
#        print "I can't SELECT from bar"
#
#    rows = cur.fetchall()
#    print "\nRows: \n"
#    for row in rows:
#        print "   ", row[1]


if __name__ == "__main__":
    port = 8081
    #app.debug = True # Turn False later
    app.run(host='0.0.0.0', port=port)
    #http_server = WSGIServer(('', port), app)
    #http_server.serve_forever()

