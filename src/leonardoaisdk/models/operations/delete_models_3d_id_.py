"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteModels3dIDRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclasses.dataclass
class DeleteModels3dIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""_\\"id\\" is required (enter it either in parameters or request body)_"""
    request_body: Optional[DeleteModels3dIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters can also be provided in the request body as a JSON object"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelAssets:
    r"""columns and relationships of \\"model_assets\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteModels3dIDResponseBody:
    r"""Responses for DELETE /api/rest/v1/models-3d/{id}"""
    delete_model_assets_by_pk: Optional[ModelAssets] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_model_assets_by_pk') }})
    r"""columns and relationships of \\"model_assets\\" """
    



@dataclasses.dataclass
class DeleteModels3dIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[DeleteModels3dIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for DELETE /api/rest/v1/models-3d/{id}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

