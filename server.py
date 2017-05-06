from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    authorizer=DummyAuthorizer()
    authorizer.add_user("ab369","123","/home/arindam/Desktop/data",perm="elradfmw")# authorizing the client if genuine or not
    # In the above statement the client is directed to a particular directory of the server
    authorizer.add_anonymous("/home/arindam/Desktop/data")

    handler=FTPHandler# FTP handler is created
    handler.authorizer=authorizer
    handler.banner="connected to AB server"
    address=('localhost',8000)
    server=FTPServer(address,handler)# server module being given parameters for network settings
    # setting maximum number of clients attaching to the server
    server.max_cons=100
    server.max_cons_per_ip=5
 
    server.serve_forever()# running the server



main()
