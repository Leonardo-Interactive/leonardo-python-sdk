"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateVariationUpscaleRequestBody:
    r"""Query parameters are provided in the request body as a JSON object"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateVariationUpscale200ApplicationJSONSDUpscaleJobOutput:
    api_credit_cost: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost') }})
    r"""API Credits Cost for Upscale Variation. Available for Production API Users"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateVariationUpscale200ApplicationJSON:
    r"""Responses for POST /variations/upscale"""
    sd_upscale_job: Optional[CreateVariationUpscale200ApplicationJSONSDUpscaleJobOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdUpscaleJob') }})
    



@dataclasses.dataclass
class CreateVariationUpscaleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_variation_upscale_200_application_json_object: Optional[CreateVariationUpscale200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for POST /variations/upscale"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

