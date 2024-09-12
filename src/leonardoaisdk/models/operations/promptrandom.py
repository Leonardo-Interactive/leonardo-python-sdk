"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardoaisdk.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PromptRandomPromptGenerationOutputTypedDict(TypedDict):
    api_credit_cost: NotRequired[int]
    r"""API Credits Cost for Random Prompt Generation. Available for Production API Users."""
    prompt: NotRequired[str]
    r"""The random prompt generated."""


class PromptRandomPromptGenerationOutput(BaseModel):
    api_credit_cost: Annotated[Optional[int], pydantic.Field(alias="apiCreditCost")] = 4
    r"""API Credits Cost for Random Prompt Generation. Available for Production API Users."""

    prompt: Optional[str] = "The random prompt generated."
    r"""The random prompt generated."""


class PromptRandomResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /prompt/random"""

    prompt_generation: NotRequired[PromptRandomPromptGenerationOutputTypedDict]


class PromptRandomResponseBody(BaseModel):
    r"""Responses for POST /prompt/random"""

    prompt_generation: Annotated[
        Optional[PromptRandomPromptGenerationOutput],
        pydantic.Field(alias="promptGeneration"),
    ] = None


class PromptRandomResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[PromptRandomResponseBodyTypedDict]
    r"""Responses for POST /prompt/random"""


class PromptRandomResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[PromptRandomResponseBody] = None
    r"""Responses for POST /prompt/random"""
