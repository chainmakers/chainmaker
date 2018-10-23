#!/bin/env python3
import requests
import json
import sys


# get the file from github
r = requests.get(
    'https://raw.githubusercontent.com/jl777/coins/master/coins')

# process coin list
coins = r.json()
export_array = []
for coin in coins:
    if coin['coin'] in sys.argv:
        # delete unneeded data
        try:
            del(coin['fname'])
        except:
            pass
        # relevant, add to the list
        export_array.append(coin)

# translate to jsonish
export_json = json.dumps(export_array)

# print output
print("export coins='" + str(export_json) + "'")
