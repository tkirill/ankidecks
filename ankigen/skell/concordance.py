from typing import List

from ankigen.skell.client import SkellClient


class SkellConcordance:

    def __init__(self):
        self.client = SkellClient()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    def get_examples(self, pattern: str) -> List[str]:
        response = self.client.search(pattern)
        examples = []
        for line in response.lines:
            examples.append(line.left[0].str_ + line.kwic[1].str_ + line.kwic[2].str_)
        return examples