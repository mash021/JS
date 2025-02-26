import socketserver
import os

import http.server

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = '/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            response = f"Received POST data: {post_data.decode('utf-8')}"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))

    def run(server_class=http.server.HTTPServer, handler_class=CustomHandler):
        server_address = ('', PORT)
        httpd = server_class(server_address, handler_class)
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

    if __name__ == '__main__':
        web_dir = os.path.join(os.path.dirname(__file__), 'web')
        os.chdir(web_dir)
        run()
