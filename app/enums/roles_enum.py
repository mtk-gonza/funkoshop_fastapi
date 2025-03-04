from enum import Enum

class Roles(Enum):
    ROOT = 'root'
    ADMIN = 'admin'
    EDITOR = 'editor'
    USER = 'user'
    GUEST = 'guest'