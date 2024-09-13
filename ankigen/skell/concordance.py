from typing import List

from ankigen.skell.client import SkellClient
from ankigen.common.cache import FileCache


class SkellConcordance:

    def __init__(self):
        self.cache = FileCache('skell')
        self.client = SkellClient()

    def get_examples(self, pattern: str) -> List[str]:
        response = self.cache.get(pattern)
        if response is None:
            response = self.client.search(pattern)
            self.cache.set(pattern, response)
        
        return [f'Example for {pattern}']