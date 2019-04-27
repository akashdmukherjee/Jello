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


app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    my_list = range(101, 207)
    backend.apis.getData()

    webapp_config_txt = ""
    with open('config/webapp.config.json', 'r') as file:
        webapp_config_txt = file.read()

    webapp_config = json.loads(webapp_config_txt)

    return render_template("home.html", my_string="akash", my_list=my_list, background_color=("background-color: " + str(webapp_config['website_background'])) )

@app.route("/api/getData", methods=['POST'])
def api_getData():
    getData()

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

