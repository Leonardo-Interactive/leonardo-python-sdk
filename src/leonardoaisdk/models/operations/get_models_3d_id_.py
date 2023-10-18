"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetModels3dIDRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclasses.dataclass
class GetModels3dIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""_\\"id\\" is required (enter it either in parameters or request body)_"""
    limit: Optional[int] = dataclasses.field(default=10, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    request_body: Optional[GetModels3dIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters can also be provided in the request body as a JSON object"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetModels3dID200ApplicationJSONModelAssets:
    r"""columns and relationships of \\"model_assets\\" """
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    mesh_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meshUrl'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'exclude': lambda f: f is None }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetModels3dID200ApplicationJSON:
    r"""Responses for GET /api/rest/v1/models-3d/{id}"""
    model_assets_by_pk: Optional[GetModels3dID200ApplicationJSONModelAssets] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_assets_by_pk') }})
    r"""columns and relationships of \\"model_assets\\" """
    



@dataclasses.dataclass
class GetModels3dIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_models_3d_id_200_application_json_object: Optional[GetModels3dID200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for GET /api/rest/v1/models-3d/{id}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

