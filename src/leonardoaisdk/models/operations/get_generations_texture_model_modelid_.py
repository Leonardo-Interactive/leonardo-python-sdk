"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import job_status as shared_job_status
from ...models.shared import model_asset_texture_types as shared_model_asset_texture_types
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationsTextureModelModelIDRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    model_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset') }})
    



@dataclasses.dataclass
class GetGenerationsTextureModelModelIDRequest:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    r"""_\\"modelId\\" is required (enter it either in parameters or request body)_"""
    limit: Optional[int] = dataclasses.field(default=10, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    request_body: Optional[GetGenerationsTextureModelModelIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters can also be provided in the request body as a JSON object"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelAssetTextureImages:
    r"""columns and relationships of \\"model_asset_texture_images\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    type: Optional[shared_model_asset_texture_types.ModelAssetTextureTypes] = dataclasses.field(default=shared_model_asset_texture_types.ModelAssetTextureTypes.NORMAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""When training model assets these are the texture types available to use."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationsTextureModelModelIDModelAssetTextureGenerations:
    r"""columns and relationships of \\"model_asset_texture_generations\\" """
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_asset_texture_images: Optional[List[ModelAssetTextureImages]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_asset_texture_images'), 'exclude': lambda f: f is None }})
    negative_prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negativePrompt') }})
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    seed: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed') }})
    status: Optional[shared_job_status.JobStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the current task."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetGenerationsTextureModelModelIDResponseBody:
    r"""Responses for GET /api/rest/v1/generations-texture/model/{modelId}"""
    model_asset_texture_generations: Optional[List[GetGenerationsTextureModelModelIDModelAssetTextureGenerations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_asset_texture_generations'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetGenerationsTextureModelModelIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[GetGenerationsTextureModelModelIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for GET /api/rest/v1/generations-texture/model/{modelId}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

