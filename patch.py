#!/usr/bin/python3

import os

for file in os.listdir():
    if file.endswith(("_eo.html", "-eo.html", "eo.html")):
        os.system("sed -i -f patchfile.sed {0}".format(file))
            