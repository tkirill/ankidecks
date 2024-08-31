# generated by datamodel-codegen:
#   filename:  gerund_or_infinitive.schema.json
#   timestamp: 2024-08-31T17:27:22+00:00

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class FollowedByEnum(Enum):
    gerund = 'gerund'
    infinitive = 'infinitive'
    bare_infinitive = 'bare infinitive'


@dataclass
class GerundOrInfinitiveItem:
    verb: str
    followed_by: List[FollowedByEnum]


GerundOrInfinitive = Optional[Dict[str, GerundOrInfinitiveItem]]
