"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateTextureGenerationRequestBodyTypedDict(TypedDict):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    front_rotation_offset: NotRequired[Nullable[int]]
    model_asset_id: NotRequired[str]
    negative_prompt: NotRequired[Nullable[str]]
    preview: NotRequired[Nullable[bool]]
    preview_direction: NotRequired[Nullable[str]]
    prompt: NotRequired[str]
    sd_version: NotRequired[Nullable[str]]
    seed: NotRequired[Nullable[int]]


class CreateTextureGenerationRequestBody(BaseModel):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    front_rotation_offset: OptionalNullable[int] = UNSET

    model_asset_id: Annotated[Optional[str], pydantic.Field(alias="modelAssetId")] = (
        None
    )

    negative_prompt: OptionalNullable[str] = UNSET

    preview: OptionalNullable[bool] = UNSET

    preview_direction: OptionalNullable[str] = UNSET

    prompt: Optional[str] = None

    sd_version: OptionalNullable[str] = UNSET

    seed: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "front_rotation_offset",
            "modelAssetId",
            "negative_prompt",
            "preview",
            "preview_direction",
            "prompt",
            "sd_version",
            "seed",
        ]
        nullable_fields = [
            "front_rotation_offset",
            "negative_prompt",
            "preview",
            "preview_direction",
            "sd_version",
            "seed",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class TextureGenerationJobOutputTypedDict(TypedDict):
    api_credit_cost: NotRequired[Nullable[int]]
    r"""API Credits Cost for Texture Generation. Available for Production API Users."""
    id: NotRequired[str]


class TextureGenerationJobOutput(BaseModel):
    api_credit_cost: Annotated[
        OptionalNullable[int], pydantic.Field(alias="apiCreditCost")
    ] = UNSET
    r"""API Credits Cost for Texture Generation. Available for Production API Users."""

    id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["apiCreditCost", "id"]
        nullable_fields = ["apiCreditCost"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class CreateTextureGenerationResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /api/rest/v1/generations-texture"""

    texture_generation_job: NotRequired[Nullable[TextureGenerationJobOutputTypedDict]]


class CreateTextureGenerationResponseBody(BaseModel):
    r"""Responses for POST /api/rest/v1/generations-texture"""

    texture_generation_job: Annotated[
        OptionalNullable[TextureGenerationJobOutput],
        pydantic.Field(alias="textureGenerationJob"),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["textureGenerationJob"]
        nullable_fields = ["textureGenerationJob"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class CreateTextureGenerationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[CreateTextureGenerationResponseBodyTypedDict]
    r"""Responses for POST /api/rest/v1/generations-texture"""


class CreateTextureGenerationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[CreateTextureGenerationResponseBody] = None
    r"""Responses for POST /api/rest/v1/generations-texture"""
