import base64

class BaseUtil:
    @staticmethod
    def encode(string: str):
        return base64.b64encode(string.encode())
    @staticmethod
    def decode(string: str):
        return base64.b64decode(string)