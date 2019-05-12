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
    some_array = range(101, 207)
    
    return render_template(
                              "home.html"
                            , my_string="akash"
                            , posts=backend.apis.getPosts()
                            , some_array=some_array
    )

@app.route("/posts")
def posts():
    print ("Woohhhoooo")
    return render_template(
                              "post.html"
    )

@app.route("/api/getPosts", methods=['GET'])
def api_getPosts():
    return backend.apis.getPosts()


if __name__ == "__main__":
    port = 8081
    
    #app.debug = True # Turn False later
    # For Development:
    app.run(host='0.0.0.0', port=port)
    
    # For Production: 
    #http_server = WSGIServer(('', port), app)
    #http_server.serve_forever()

