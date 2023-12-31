"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclasses.dataclass
class DeleteInitImageByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""_\\"id\\" is required_"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InitImages:
    r"""columns and relationships of \\"init_images\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteInitImageByIDResponseBody:
    r"""Responses for DELETE /init-image/{id}"""
    delete_init_images_by_pk: Optional[InitImages] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_init_images_by_pk') }})
    r"""columns and relationships of \\"init_images\\" """
    



@dataclasses.dataclass
class DeleteInitImageByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[DeleteInitImageByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for DELETE /init-image/{id}"""
    

