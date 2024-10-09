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
from leonardo_ai_sdk.utils import FieldMetadata, PathParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetInitImageByIDRequestTypedDict(TypedDict):
    id: str
    r"""_\"id\" is required_"""


class GetInitImageByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""_\"id\" is required_"""


class GetInitImageByIDInitImagesTypedDict(TypedDict):
    r"""columns and relationships of \"init_images\" """

    created_at: NotRequired[str]
    id: NotRequired[Nullable[str]]
    url: NotRequired[str]


class GetInitImageByIDInitImages(BaseModel):
    r"""columns and relationships of \"init_images\" """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None

    id: OptionalNullable[str] = UNSET

    url: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["createdAt", "id", "url"]
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


class GetInitImageByIDResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /init-image/{id}"""

    init_images_by_pk: NotRequired[Nullable[GetInitImageByIDInitImagesTypedDict]]
    r"""columns and relationships of \"init_images\" """


class GetInitImageByIDResponseBody(BaseModel):
    r"""Responses for GET /init-image/{id}"""

    init_images_by_pk: OptionalNullable[GetInitImageByIDInitImages] = UNSET
    r"""columns and relationships of \"init_images\" """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["init_images_by_pk"]
        nullable_fields = ["init_images_by_pk"]
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


class GetInitImageByIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetInitImageByIDResponseBodyTypedDict]
    r"""Responses for GET /init-image/{id}"""


class GetInitImageByIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetInitImageByIDResponseBody] = None
    r"""Responses for GET /init-image/{id}"""