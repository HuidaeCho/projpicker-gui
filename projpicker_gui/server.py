#!/bin/env python3
import os
import json
import projpicker as ppik
from flask import Flask, render_template, request, session
from app import Geometry, colors, bbox_to_json, create_parsable_geoms, query

gui_dir = os.path.join(os.path.dirname(__file__), 'gui')  # development path

if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')

server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching

server.debug = True
server.config['TEMPLATES_AUTO_RELOAD'] = True

#################################
# Constants
MAP = "index.html"


projpick_query = ""
@server.route("/")
def home():
    global projpick_query
    return render_template(MAP, projpick_query="")


@server.route('/data', methods=["POST", "GET"])
def get_javascript_data():
    if request.method == "POST":
        global projpick_query
        geojson = request.get_json()
        query_str = create_parsable_geoms(geojson)
        crs_list = query(query_str)
        projpick_query = bbox_to_json(crs_list)
        # Explicetly call so async function is ran
        get_python_data()
        return projpick_query


@server.route('/projdata', methods=["GET"])
def get_python_data():
    global projpick_query
    return json.dumps(projpick_query)

