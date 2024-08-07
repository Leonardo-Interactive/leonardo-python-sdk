"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSVDMotionGenerationRequestBody:
    r"""Query parameters can also be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    image_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imageId') }})
    r"""The ID of the image, supports generated images, variation images, and init images."""
    is_init_image: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isInitImage'), 'exclude': lambda f: f is CreateSVDMotionGenerationRequestBody.UNSET }})
    r"""If it is an init image uploaded by the user. This image is uploaded from endpoint: Upload init image."""
    is_public: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isPublic'), 'exclude': lambda f: f is CreateSVDMotionGenerationRequestBody.UNSET }})
    r"""Whether the generation is public or not"""
    is_variation: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isVariation'), 'exclude': lambda f: f is CreateSVDMotionGenerationRequestBody.UNSET }})
    r"""If it is a variation image."""
    motion_strength: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('motionStrength'), 'exclude': lambda f: f is CreateSVDMotionGenerationRequestBody.UNSET }})
    r"""The motion strength."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MotionSvdGenerationOutput:
    UNSET='__SPEAKEASY_UNSET__'
    api_credit_cost: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost'), 'exclude': lambda f: f is MotionSvdGenerationOutput.UNSET }})
    r"""API credits cost, available for Production API users."""
    generation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generationId'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSVDMotionGenerationResponseBody:
    r"""Responses for POST /generations-motion-svd"""
    UNSET='__SPEAKEASY_UNSET__'
    sd_generation_job: Optional[MotionSvdGenerationOutput] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdGenerationJob'), 'exclude': lambda f: f is CreateSVDMotionGenerationResponseBody.UNSET }})
    



@dataclasses.dataclass
class CreateSVDMotionGenerationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[CreateSVDMotionGenerationResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /generations-motion-svd"""
    

