"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardoaisdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from leonardoaisdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Delete3DModelByIDRequestBodyTypedDict(TypedDict):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    id: NotRequired[Nullable[str]]


class Delete3DModelByIDRequestBody(BaseModel):
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


class Delete3DModelByIDRequestTypedDict(TypedDict):
    id: str
    r"""_\"id\" is required (enter it either in parameters or request body)_"""
    request_body: NotRequired[Delete3DModelByIDRequestBodyTypedDict]
    r"""Query parameters can also be provided in the request body as a JSON object"""


class Delete3DModelByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""_\"id\" is required (enter it either in parameters or request body)_"""

    request_body: Annotated[
        Optional[Delete3DModelByIDRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Query parameters can also be provided in the request body as a JSON object"""


class ModelAssetsTypedDict(TypedDict):
    r"""columns and relationships of \"model_assets\" """

    id: NotRequired[Nullable[str]]


class ModelAssets(BaseModel):
    r"""columns and relationships of \"model_assets\" """

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


class Delete3DModelByIDResponseBodyTypedDict(TypedDict):
    r"""Responses for DELETE /api/rest/v1/models-3d/{id}"""

    delete_model_assets_by_pk: NotRequired[Nullable[ModelAssetsTypedDict]]
    r"""columns and relationships of \"model_assets\" """


class Delete3DModelByIDResponseBody(BaseModel):
    r"""Responses for DELETE /api/rest/v1/models-3d/{id}"""

    delete_model_assets_by_pk: OptionalNullable[ModelAssets] = UNSET
    r"""columns and relationships of \"model_assets\" """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["delete_model_assets_by_pk"]
        nullable_fields = ["delete_model_assets_by_pk"]
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


class Delete3DModelByIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[Delete3DModelByIDResponseBodyTypedDict]
    r"""Responses for DELETE /api/rest/v1/models-3d/{id}"""


class Delete3DModelByIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[Delete3DModelByIDResponseBody] = None
    r"""Responses for DELETE /api/rest/v1/models-3d/{id}"""
