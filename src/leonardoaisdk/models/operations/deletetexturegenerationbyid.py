"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteTextureGenerationByIDRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is DeleteTextureGenerationByIDRequestBody.UNSET }})
    



@dataclasses.dataclass
class DeleteTextureGenerationByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""_\\"id\\" is required (enter it either in parameters or request body)_"""
    request_body: Optional[DeleteTextureGenerationByIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters can also be provided in the request body as a JSON object"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelAssetTextureGenerations:
    r"""columns and relationships of \\"model_asset_texture_generations\\" """
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is ModelAssetTextureGenerations.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteTextureGenerationByIDResponseBody:
    r"""Responses for DELETE /api/rest/v1/generations-texture/{id}"""
    UNSET='__SPEAKEASY_UNSET__'
    delete_model_asset_texture_generations_by_pk: Optional[ModelAssetTextureGenerations] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_model_asset_texture_generations_by_pk'), 'exclude': lambda f: f is DeleteTextureGenerationByIDResponseBody.UNSET }})
    r"""columns and relationships of \\"model_asset_texture_generations\\" """
    



@dataclasses.dataclass
class DeleteTextureGenerationByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[DeleteTextureGenerationByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for DELETE /api/rest/v1/generations-texture/{id}"""
    
