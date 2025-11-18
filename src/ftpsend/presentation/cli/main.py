from ftpsend.infrastructure.authorizers import AdminAuthorizer
from ftpsend.infrastructure.ftp_service import FtpServerService
from pyftpdlib.log import logging

def main():
    admin_account = AdminAuthorizer()
    admin_account.add_user(
        "admin", "1234", "/home/backdev/go", perm="elradfmw"
    )

    ftp_service = FtpServerService("0.0.0.0", 8787, admin_account)
    ftp_service.serve_forever()
