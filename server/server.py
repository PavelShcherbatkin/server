import http.server
import socketserver


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 9090), handler) as httpd:
    httpd.serve_forever()
