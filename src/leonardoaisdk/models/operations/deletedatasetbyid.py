"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclasses.dataclass
class DeleteDatasetByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the dataset to delete."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDatasetByID200ApplicationJSONDatasets:
    r"""columns and relationships of \\"datasets\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDatasetByID200ApplicationJSON:
    r"""Responses for DELETE /datasets/{id}"""
    delete_datasets_by_pk: Optional[DeleteDatasetByID200ApplicationJSONDatasets] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_datasets_by_pk') }})
    r"""columns and relationships of \\"datasets\\" """
    



@dataclasses.dataclass
class DeleteDatasetByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_dataset_by_id_200_application_json_object: Optional[DeleteDatasetByID200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for DELETE /datasets/{id}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

