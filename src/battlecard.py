#/usr/bin/python3

from http.server import BaseHTTPRequestHandler

class BattleCardServer(BaseHTTPRequestHandler):
    def __init__(self):
        BaseHTTPRequestHandler.__init__()

    def do_GET(self):
        pass
