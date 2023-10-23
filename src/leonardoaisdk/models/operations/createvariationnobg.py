"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateVariationNoBGRequestBody:
    r"""Query parameters are provided in the request body as a JSON object"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    is_variation: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isVariation'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateVariationNoBG200ApplicationJSONSDUpscaleJobOutput:
    api_credit_cost: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost') }})
    r"""API Credits Cost for No Background Variation. Available for Production API Users"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateVariationNoBG200ApplicationJSON:
    r"""Responses for POST /variations/nobg"""
    sd_nobg_job: Optional[CreateVariationNoBG200ApplicationJSONSDUpscaleJobOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdNobgJob'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class CreateVariationNoBGResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_variation_no_bg_200_application_json_object: Optional[CreateVariationNoBG200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for POST /variations/nobg"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

