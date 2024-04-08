"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PromptImproveRequestBody:
    r"""Query parameters to be provided in the request body as a JSON object"""
    prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt') }})
    r"""The prompt to improve."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PromptGenerationOutput:
    api_credit_cost: Optional[int] = dataclasses.field(default=4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost'), 'exclude': lambda f: f is None }})
    r"""API Credits Cost for Random Prompt Generation. Available for Production API Users."""
    prompt: Optional[str] = dataclasses.field(default='The improved prompt.', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    r"""The improved prompt."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PromptImproveResponseBody:
    r"""Responses for POST /prompt/improve"""
    prompt_generation: Optional[PromptGenerationOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptGeneration'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class PromptImproveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[PromptImproveResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /prompt/improve"""
    

