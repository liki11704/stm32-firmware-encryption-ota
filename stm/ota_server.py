import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"Serving HTTP on 0.0.0.0 port {PORT} ...")
print("Place your 'firmware_encrypted.bin' in this same folder.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()