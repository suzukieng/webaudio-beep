from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")


if __name__ == '__main__':
    # Minimal example of serving the directory contents via HTTPS
    httpd = HTTPServer(('0.0.0.0', 8888), MyHTTPRequestHandler)
    print(f'Serving directory on http://0.0.0.0:8888 (plain HTTP, you need to use ngrok or similar tool for SSL)')
    httpd.serve_forever()
