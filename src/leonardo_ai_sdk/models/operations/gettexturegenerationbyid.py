"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import (
    job_status as shared_job_status,
    model_asset_texture_types as shared_model_asset_texture_types,
)
from leonardo_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from leonardo_ai_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetTextureGenerationByIDRequestBodyTypedDict(TypedDict):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    id: NotRequired[Nullable[str]]


class GetTextureGenerationByIDRequestBody(BaseModel):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id"]
        nullable_fields = ["id"]
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


class GetTextureGenerationByIDRequestTypedDict(TypedDict):
    id: str
    r"""_\"id\" is required (enter it either in parameters or request body)_"""
    request_body: NotRequired[GetTextureGenerationByIDRequestBodyTypedDict]
    r"""Query parameters can also be provided in the request body as a JSON object"""
    limit: NotRequired[int]
    offset: NotRequired[int]


class GetTextureGenerationByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""_\"id\" is required (enter it either in parameters or request body)_"""

    request_body: Annotated[
        Optional[GetTextureGenerationByIDRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Query parameters can also be provided in the request body as a JSON object"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0


class ModelAssetTextureImagesTypedDict(TypedDict):
    r"""columns and relationships of \"model_asset_texture_images\" """

    id: NotRequired[Nullable[str]]
    type: NotRequired[shared_model_asset_texture_types.ModelAssetTextureTypes]
    r"""When training model assets these are the texture types available to use."""
    url: NotRequired[str]


class ModelAssetTextureImages(BaseModel):
    r"""columns and relationships of \"model_asset_texture_images\" """

    id: OptionalNullable[str] = UNSET

    type: Optional[shared_model_asset_texture_types.ModelAssetTextureTypes] = (
        shared_model_asset_texture_types.ModelAssetTextureTypes.NORMAL
    )
    r"""When training model assets these are the texture types available to use."""

    url: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "type", "url"]
        nullable_fields = ["id"]
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


class GetTextureGenerationByIDModelAssetTextureGenerationsTypedDict(TypedDict):
    r"""columns and relationships of \"model_asset_texture_generations\" """

    created_at: NotRequired[str]
    id: NotRequired[Nullable[str]]
    model_asset_texture_images: NotRequired[List[ModelAssetTextureImagesTypedDict]]
    negative_prompt: NotRequired[Nullable[str]]
    prompt: NotRequired[str]
    seed: NotRequired[Nullable[int]]
    status: NotRequired[shared_job_status.JobStatus]
    r"""The status of the current task."""


class GetTextureGenerationByIDModelAssetTextureGenerations(BaseModel):
    r"""columns and relationships of \"model_asset_texture_generations\" """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None

    id: OptionalNullable[str] = UNSET

    model_asset_texture_images: Optional[List[ModelAssetTextureImages]] = None

    negative_prompt: Annotated[
        OptionalNullable[str], pydantic.Field(alias="negativePrompt")
    ] = UNSET

    prompt: Optional[str] = None

    seed: OptionalNullable[int] = UNSET

    status: Optional[shared_job_status.JobStatus] = None
    r"""The status of the current task."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "createdAt",
            "id",
            "model_asset_texture_images",
            "negativePrompt",
            "prompt",
            "seed",
            "status",
        ]
        nullable_fields = ["id", "negativePrompt", "seed"]
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


class GetTextureGenerationByIDResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /api/rest/v1/generations-texture/{id}"""

    model_asset_texture_generations_by_pk: NotRequired[
        Nullable[GetTextureGenerationByIDModelAssetTextureGenerationsTypedDict]
    ]
    r"""columns and relationships of \"model_asset_texture_generations\" """


class GetTextureGenerationByIDResponseBody(BaseModel):
    r"""Responses for GET /api/rest/v1/generations-texture/{id}"""

    model_asset_texture_generations_by_pk: OptionalNullable[
        GetTextureGenerationByIDModelAssetTextureGenerations
    ] = UNSET
    r"""columns and relationships of \"model_asset_texture_generations\" """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["model_asset_texture_generations_by_pk"]
        nullable_fields = ["model_asset_texture_generations_by_pk"]
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


class GetTextureGenerationByIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetTextureGenerationByIDResponseBodyTypedDict]
    r"""Responses for GET /api/rest/v1/generations-texture/{id}"""


class GetTextureGenerationByIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetTextureGenerationByIDResponseBody] = None
    r"""Responses for GET /api/rest/v1/generations-texture/{id}"""
