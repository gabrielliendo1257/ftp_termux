from dataclasses import dataclass

class UserCredentials:

    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

@dataclass
class UserConnected:
    ip: str
    port: int
    connected_at: float
    username: str