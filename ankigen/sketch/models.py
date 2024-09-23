# generated by datamodel-codegen:
#   filename:  concordance.schema.json
#   timestamp: 2024-09-23T17:34:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ContextTerm(BaseModel):
    strc: Optional[str] = None
    str_: Optional[str] = Field(None, alias='str')


class KwicTerm(BaseModel):
    str_: Optional[str] = Field(None, alias='str')
    coll: Optional[int] = None


class ConcordanceLine(BaseModel):
    left: Optional[List[ContextTerm]] = Field(None, alias='Left')
    kwic: Optional[List[KwicTerm]] = Field(None, alias='Kwic')
    right: Optional[List[ContextTerm]] = Field(None, alias='Right')


class SketchConcordanceResponse(BaseModel):
    lines: Optional[List[ConcordanceLine]] = Field(None, alias='Lines')
