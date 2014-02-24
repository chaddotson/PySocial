#!/bin/python
from facepy import GraphAPI 

from secrets import FACEBOOK_OAUTH

import sys

if not len(sys.argv) == 2:
    print "usage: python PySocial.py MESSAGE"
    exit()

graph = GraphAPI(FACEBOOK_OAUTH)

graph.post(path='me/feed', message=sys.argv[1])

