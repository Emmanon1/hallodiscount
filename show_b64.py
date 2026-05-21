import http.server
import socketserver

b64 = open('b64_out.txt').read().strip()

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b64.encode())

with socketserver.TCPServer(('', 8765), Handler) as httpd:
    print('Serving on port 8765')
    httpd.serve_forever()
