from ftplib import FTP

# Detalles de conexión FTP
ftp_host = "192.168.124.18"  # Dirección IP del servidor FTP
ftp_port = 21  # Puerto del servidor FTP
ftp_user = "usuario"  # Nombre de usuario FTP
ftp_pass = "contrasenia"  # Contraseña FTP


# Función para descargar un archivo desde el servidor FTP
def descargar_archivo(archivo_remoto, archivo_local):
    with FTP() as ftp:
        # Conectar y autenticar
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_user, ftp_pass)

        # Descargar archivo
        with open(archivo_local, "wb") as f:
            ftp.retrbinary(f"RETR {archivo_remoto}", f.write)


# Función para listar archivos en el servidor FTP
def listar_archivos():
    with FTP() as ftp:
        # Conectar y autenticar
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_user, ftp_pass)

        # Listar archivos en el directorio actual del servidor
        archivos = ftp.nlst()
        print("Archivos en el servidor:")
        for archivo in archivos:
            print(archivo)


# Ejemplo de uso
if __name__ == "__main__":
    listar_archivos()
    # Descargar un archivo del servidor
    archivo_remoto = "fotos.docx"
    archivo_local = "archivo_descargado.txt"
    descargar_archivo(archivo_remoto, archivo_local)
    print(f"Archivo '{archivo_remoto}' descargado como '{archivo_local}'.")
