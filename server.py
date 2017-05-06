from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    authorizer=DummyAuthorizer()
    # authorizing the client if genuine or not
    # also setting the permissions that client would have in the server(Eg.read,write etc.)
    # change permissions in perm as required
    authorizer.add_user("ab369","123","/home/arindam/Desktop/data",perm="elradfmw")
    # In the above statement the client is directed to a particular directory of the server
    authorizer.add_anonymous("/home/arindam/Desktop/data")
    # FTP handler is created
    handler=FTPHandler
    handler.authorizer=authorizer
    handler.banner="connected to AB server"
    # creating address argument
    address=('localhost',8000)
    # server module being given parameters for network settings
    server=FTPServer(address,handler)
    # setting maximum number of clients attaching to the server
    server.max_cons=100
    server.max_cons_per_ip=5
    # running the server
    server.serve_forever()



main()
