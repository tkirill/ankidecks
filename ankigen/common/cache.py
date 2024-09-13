from typing import Optional


class FileCache:

    def __init__(self, name: str):
        self.name = name
    
    def get(self, key: str) -> Optional[str]:
        pass

    def set(self, key: str, value: str):
        pass