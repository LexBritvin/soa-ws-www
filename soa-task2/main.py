import socket

# Define constants.
HOST = 'localhost'
PORT = 8080
# Open socket and connect on port.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# Send HTTP request.
s.sendall('GET /soa-task1/index.php?name=britvin HTTP/1.1\r\nhost: 127.0.0.1\r\n\r\n')

# Read header infobyte by byte to get Content length.
response_text = ''
while True:
    # Receive a reply from the server.
    response_text += s.recv(1)
    if response_text.find("\r\n\r\n") != -1:
        print "\n--> Header section:\n\n", response_text
        break

# Get content length value.
header_len = len("Content-Length: ")
content_len_start = response_text.find("Content-Length")
content_length_end = response_text.find('\r\n', response_text.find("Content-Length"))
content_length = int(response_text[content_len_start + header_len:content_length_end])

# Read the whole content.
if content_length != -1:
    data = s.recv(content_length)
    print "--> Content Section: \n\n",  data
