# generated by datamodel-codegen:
#   filename:  skell_concordance.schema.json
#   timestamp: 2024-09-13T19:04:45+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class KwicItem(BaseModel):
    str_: str = Field(..., alias='Str')
    class_: Optional[str] = Field(None, alias='Class')


class ConcordanceItem(BaseModel):
    left: List[KwicItem] = Field(..., alias='Left')
    kwic: List[KwicItem] = Field(..., alias='Kwic')
    right: List[KwicItem] = Field(..., alias='Right')
    token_num: Optional[int] = Field(None, alias='TokenNum')


class SkellConcordanceResponse(BaseModel):
    query: Optional[str] = Field(None, alias='Query')
    user: Optional[str] = Field(None, alias='User')
    method_name: Optional[str] = Field(None, alias='MethodName')
    corp_name: Optional[str] = Field(None, alias='CorpName')
    ui_lang: Optional[str] = Field(None, alias='UiLang')
    ad_sense: Optional[bool] = Field(None, alias='AdSense')
    mobile: Optional[bool] = Field(None, alias='Mobile')
    err: Optional[Dict[str, Any]] = Field(None, alias='Err')
    lines: List[ConcordanceItem] = Field(..., alias='Lines')
