#!/usr/bin/env python3
################################################################################
# Project: ProjPicker
# Purpose: This Python script provides the main CLI API for ProjPicker.
# Author(s): Huidae Cho, Owen Smith
# Since:   June 4, 2021
#
# Copyright (C) 2021, Huidae Cho <https://faculty.ung.edu/hcho/>,
#                     Owen Smith <https://www.gaderian.io/>
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
################################################################################


import pprint
import argparse
import json
from utils.connection import projpicker_connection
from utils.geom import bbox_coors, intersect


def json_entry(cursor, code, bbox):
    epsg = code
    extent = bbox_coors(bbox)
    entry = {'epsg': epsg,
             'extent': extent,
             'products': [
                 ],
             }
    return entry


def main():
    parser = argparse.ArgumentParser(description="ProjPicker")
    parser.add_argument('coordinates', type=float, nargs=2,
                        help="Point coordinates in lat/lon")
    parser.add_argument('-o', '--output', type=str,
                        help='Create output file of intersection')
    args = parser.parse_args()

    con = projpicker_connection()
    cur = con.cursor()

    inter_crs = intersect(args.coordinates)

    output = {}
    for i in inter_crs:
        output[i[0]] = json_entry(cur, i[0], i[1])

    if args.output:
        with open(args.output, 'w') as file:
            json.dump(output, file, indent=2)
        return

    pprint.pprint(output)


if __name__ == '__main__':
    main()
