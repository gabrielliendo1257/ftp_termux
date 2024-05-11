from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configuración de autorización
authorizer = DummyAuthorizer()
authorizer.add_user(
    "usuario",
    "contrasenia",
    "D:\\vsCode\\python\\practicas\\003-pyshark",
    perm="elradfmw",
)

# Configuración del manejador FTP
handler = FTPHandler
handler.authorizer = authorizer

# Configuración del servidor FTP
server = FTPServer(("0.0.0.0", 21), handler)

# Iniciar el servidor FTP
server.serve_forever()
