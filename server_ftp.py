from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configuración de autorización
authorizer = DummyAuthorizer()
authorizer.add_user(
    "usuario",
    "contrasenia",
    "D:\\",
    perm="elradfmw",
)

# Configuración del manejador FTP
handler = FTPHandler
handler.authorizer = authorizer

# Configuración del servidor FTP
server = FTPServer(("0.0.0.0", 21), handler)

# Iniciar el servidor FTP
try:
    # Iniciar el servidor FTP
    server.serve_forever()
except KeyboardInterrupt:
    print("Cerrando el servidor FTP...")
    server.close_all()
    server.stop()
