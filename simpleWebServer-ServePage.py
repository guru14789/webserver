import http.server
import socketserver
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'myWebPage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
# Create an object of the above class
handler_object = MyHttpRequestHandler

# Set the port number for the server
PORT = 8080

# Create the server and bind it to the specified port
my_server = socketserver.TCPServer(("", PORT), handler_object)

print(f"Serving on port {PORT}....")

# Start the server - run indefinately
my_server.serve_forever()