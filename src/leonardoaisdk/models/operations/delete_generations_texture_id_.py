"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteGenerationsTextureIDRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclasses.dataclass
class DeleteGenerationsTextureIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""_\\"id\\" is required (enter it either in parameters or request body)_"""
    request_body: Optional[DeleteGenerationsTextureIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters can also be provided in the request body as a JSON object"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelAssetTextureGenerations:
    r"""columns and relationships of \\"model_asset_texture_generations\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteGenerationsTextureIDResponseBody:
    r"""Responses for DELETE /api/rest/v1/generations-texture/{id}"""
    delete_model_asset_texture_generations_by_pk: Optional[ModelAssetTextureGenerations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_model_asset_texture_generations_by_pk') }})
    r"""columns and relationships of \\"model_asset_texture_generations\\" """
    



@dataclasses.dataclass
class DeleteGenerationsTextureIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[DeleteGenerationsTextureIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for DELETE /api/rest/v1/generations-texture/{id}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

