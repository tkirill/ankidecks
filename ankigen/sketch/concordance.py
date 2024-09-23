from typing import List, Iterable

from ankigen.sketch.client import SketchClient
from ankigen.gerund_or_infinitive.models import GerundOrInfinitiveItem, FollowedByEnum


class SketchConcordance:

    def __init__(self):
        self.client = SketchClient()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    def get_examples_gerund_or_infinitive(self, verb: str, followed_by: FollowedByEnum) -> List[str]:
        pattern = self.get_gerund_or_infinitive_query(verb, followed_by)
        response = self.client.search(pattern)
        examples = []
        for line in response.lines:
            left = ' '.join(x.str_ for x in line.left if x.str_)
            kwic = ' '.join(x.str_ for x in line.kwic)
            right = ' '.join(x.str_ for x in line.right if x.str_)
            examples.append(f'{left} <b>{kwic}</b> {right}')
        return examples
    
    def get_gerund_or_infinitive_query(self, verb: str, followed_by: FollowedByEnum) -> str:
        match followed_by:
            case FollowedByEnum.gerund:
                return f'[lemma="{verb}"] [tag="VVG"]'
            case FollowedByEnum.infinitive:
                return f'[lemma="{verb}"] [lemma="to"] [tag="V.*"]'
            case FollowedByEnum.bare_infinitive:
                return f'[lemma="{verb}"] [tag="V.*"]'
