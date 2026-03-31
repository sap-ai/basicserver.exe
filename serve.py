import socket
import os
fe = open("p.txt")
fet = fe.read()
fete = fet.split()
def stringtolist(file, character):
   global l
   c = file
   return c.split(character)
def listtostring(list, character): return character.join(list)
def decomp(l):
   f = stringtolist(l, "~_s")
   d = listtostring(f, '\n')
   y = stringtolist(d, "~_rz")
   z = listtostring(y, ' ')
   r = stringtolist(z, "%22")
   e = listtostring(r, '')
   return e # add spaces
try:
   print(SERVER_HOST)
except:
   SERVER_HOST = '0.0.0.0'
   SERVER_HOST = fete[0]
try:
   print(SERVER_PORT) # check if server port all ready chosen
except:
   SERVER_PORT = 8000 # define sever port
   SERVER_PORT = int(fete[1])
try:
   print(fi) # check if file to sent content to all ready chosen
except:
   fi = "pro.py" # define the file to send to
# init connection to port and host
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
while True:
    p = open(fi) # open the file
    client_connection, client_address = server_socket.accept() # bind server with ip and host
    request = client_connection.recv(1024).decode()
    headers = request.split('\n')
    try: filename = decomp(headers[0].split()[1]) # process url into data for translation back
    except: filename = ""
    if filename == "sz": # read the server
       response = p.read()
       os.startfile("serve.exe") # prevent server from closing at one response
    else:
          with open(fi, 'w') as file: file.write(p.read() + filename[2: len(filename)+1])# add the final reponse to pro.py 
          os.startfile("serve.exe")
    client_connection.sendall(response.encode())
