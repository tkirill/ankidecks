from abc import ABC
from typing import Iterable


class NoteABC(ABC):

    def get_properties(self) -> Iterable[str]:
        pass