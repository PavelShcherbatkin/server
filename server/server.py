import http.server
import socketserver

HOST = 'localhost'
PORT = 9090

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = str(f'http://84.201.165.21:{PORT}') + self.path
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(('Copy the url and send it to the bot: ' + url).encode('utf-8'))

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()
