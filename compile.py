#!/usr/local/bin/python -u

import json
import os.path
import tornado
import tornado.template

FILE_ROOT = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_FILE = "./templates/index.html.tmpl"
DATA_FILE = "data.json"

template_loader = tornado.template.Loader(FILE_ROOT)
template = template_loader.load(TEMPLATE_FILE)

with open(os.path.join(FILE_ROOT, DATA_FILE), "r") as fh:
	template_vars = json.load(fh)

print template.generate(**template_vars)
