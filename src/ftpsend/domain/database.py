from __future__ import annotations

from typing import Optional, TypeVar


class Connection:

    def __init__(self, username: str, password: str, database: str, host: str = "localhost"):
        self.username = username
        self.password = password
        self.database = database
        self.host = host

T = TypeVar("T")

class Repository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def save_user(self) -> Optional[T]:
        raise NotImplementedError()

    def get_by_id(self) -> Optional[T]:
        raise NotImplementedError()