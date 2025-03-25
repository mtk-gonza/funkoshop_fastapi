from enum import Enum

class ImageType(str, Enum):
    FRONT = "front"
    BACK = "back"
    LOGO = "logo"
    BANNER = "banner"