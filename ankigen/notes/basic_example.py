from dataclasses import dataclass
from typing import List


@dataclass
class BasicExampleNote:
    front: str
    back: str
    examples: List[str]