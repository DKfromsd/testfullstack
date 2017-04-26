
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output=b""
                output +=b"<html><body>"
                output +=b"Hello!"
                output +=b"<form method='POST' enctype='multipart/form-data' action='/" \
                        b"hello'><h2>What would you like me to say?</h2><input name='message'" \
                        b" type='text'><input type='submit' value='Submit'> </form>"
                output +=b"</body></html>"
                self.wfile.write(output) # (output.encode()) this is for python 3.x instead of (output)
                print (output)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output =b""
                output +=b"<html><body>"
                output +=b"&#161Hola! <a href = '/hello'>Back to Hello</a>"
                output +=b"<form method='POST' enctype='multipart/form-data' action='/" \
                        b"hello'><h2>What would you like me to say?</h2><input name='message'" \
                        b" type='text'><input type='submit' value='Submit'> </form>"
                output +=b"</body></html>"
                self.wfile.write(output) 
                print (output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' %self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output =b""
            output +=b"<html><body>"
            output +=b"<h2> Ok, how about this: </h2>"
            output +=b"<h1> {} </h1>".format(messagecontent[0])
            output +=b"<form method='POST' enctype='multipart/form-data' action='/" \
                    b"hello'><h2>What would you like me to say?</h2><input name='message'" \
                     b" type='text'><input type='submit' value='Submit'> </form>"
            output +=b"</body></html>"
            self.wfile.write(output) 
            print (output)
        except:
            pass
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web server running on port {}".format(port))
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping the server...")
        server.socket.close()


if __name__ == "__main__":
    main()