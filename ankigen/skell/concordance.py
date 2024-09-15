from typing import List

from ankigen.skell.client import SkellClient
import dbm


class SkellConcordance:

    def __init__(self):
        self.client = SkellClient()
    
    def __enter__(self):
        self.cache = dbm.open('skell_cache', 'c')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.cache.close()

    def get_examples(self, pattern: str) -> List[str]:
        response = self.cache.get(pattern)
        if response is None:
            response = self.client.search(pattern)
            self.cache[pattern] = response
        
        return [f'Example for {pattern}']