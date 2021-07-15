#!/bin/env python3
import os
import json
import projpicker as ppik
from flask import Flask, render_template, request

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

app = Flask(__name__, )
app.debug = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

#################################
# Constants
VERBOSE = True
MAP = "gui.html"


#################################
# Geometry
class Geometry:
    def __init__(self, type, coors):
        self.type = "poly" if type == "Polygon" else "point"

        # Reverse coordinates as leaflet returns opposite order of what
        # ProjPicker takes
        if self.type == "point":
            # Coordinates in "Point" type are single-depth tuple [i, j]
            self.coors = coors[::-1]
        else:
            # Coordinates in "Poly" type are in multi-depth array of size
            # [[[i0, j0], [i1, j1], ...]]; Move down array depth for easier
            # iteration
            latlon_coors = []
            for lonlat in coors[0]:
                latlon_coors.append(lonlat[::-1])
            self.coors = list(latlon_coors)


# Utility Functions
def create_parsable_geoms(geojson):
    # TODO: Logical operator buttons
    geoms = geojson['logicalOperator']
    for feature in geojson["features"]:
        json_geom = feature["geometry"]
        coors = json_geom["coordinates"]
        geom = Geometry(json_geom["type"], json_geom["coordinates"])
        geoms += f"\n{geom.type}"
        if geom.type == "point":
            geoms += f"\n{geom.coors[0]},{geom.coors[1]}"
        else:
            for coors in geom.coors:
                geoms += f"\n{coors[0]},{coors[1]}"

    return geoms


def bbox_to_json(bbox_list):
    crs_json = {}
    for crs in bbox_list:
        entry = {}
        crs_dict = crs._asdict()
        for key in list(crs_dict.keys()):
            entry[key] = crs_dict[key]
        crs_json[f"{crs.crs_auth_name}|{crs.crs_code}"] = entry
    return crs_json


def query(geoms):
    crs_list = []
    crs = []
    if geoms is not None:
        parsed_geoms = ppik.parse_mixed_geoms(geoms)
        crs.extend(ppik.query_mixed_geoms(parsed_geoms))
        if VERBOSE:
            ppik.message(f"Query geometries: {parsed_geoms}")
            ppik.message(f"Number of queried CRSs: {len(crs)}")

    return crs


# WEB LOGIC
@app.route("/")
def home():
    return render_template(MAP)


@app.route('/data', methods=["POST", "GET"])
def get_javascript_data():
    geojson = request.get_json()
    if VERBOSE:
        print(f"{colors.OKGREEN}Success!\n{colors.OKCYAN}{geojson}{colors.ENDC}")
    query_str = create_parsable_geoms(geojson)
    print(f"{colors.OKBLUE}{query_str}{colors.ENDC}")
    crs_list = query(query_str)
    print(bbox_to_json(crs_list))
    return request.form


# RUN
if __name__ == '__main__':
    app.run()
