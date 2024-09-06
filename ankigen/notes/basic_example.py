from dataclasses import dataclass
from typing import Iterable, List

from ankigen.notes.abstractions import NoteABC


@dataclass
class BasicExampleNote(NoteABC):

    front: str
    back: str
    examples: List[str]
    tags: List[str]

    def get_properties(self) -> Iterable[str]:
        yield self.front
        yield self.back
        yield from self.examples
        yield ' '.join(self.tags)