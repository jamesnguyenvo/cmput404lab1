#!/usr/bin/env python3

import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/jamesnguyenvo/cmput404lab1/master/script.py")
print(r.text)