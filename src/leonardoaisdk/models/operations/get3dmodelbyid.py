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
from leonardoaisdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class Get3DModelByIDRequestBodyTypedDict(TypedDict):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    id: NotRequired[Nullable[str]]


class Get3DModelByIDRequestBody(BaseModel):
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


class Get3DModelByIDRequestTypedDict(TypedDict):
    id: str
    r"""_\"id\" is required (enter it either in parameters or request body)_"""
    request_body: NotRequired[Get3DModelByIDRequestBodyTypedDict]
    r"""Query parameters can also be provided in the request body as a JSON object"""
    limit: NotRequired[int]
    offset: NotRequired[int]


class Get3DModelByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""_\"id\" is required (enter it either in parameters or request body)_"""

    request_body: Annotated[
        Optional[Get3DModelByIDRequestBody],
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


class Get3DModelByIDModelAssetsTypedDict(TypedDict):
    r"""columns and relationships of \"model_assets\" """

    created_at: NotRequired[str]
    id: NotRequired[Nullable[str]]
    mesh_url: NotRequired[str]
    name: NotRequired[Nullable[str]]
    updated_at: NotRequired[str]
    user_id: NotRequired[Nullable[str]]


class Get3DModelByIDModelAssets(BaseModel):
    r"""columns and relationships of \"model_assets\" """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None

    id: OptionalNullable[str] = UNSET

    mesh_url: Annotated[Optional[str], pydantic.Field(alias="meshUrl")] = None

    name: OptionalNullable[str] = UNSET

    updated_at: Annotated[Optional[str], pydantic.Field(alias="updatedAt")] = None

    user_id: Annotated[OptionalNullable[str], pydantic.Field(alias="userId")] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["createdAt", "id", "meshUrl", "name", "updatedAt", "userId"]
        nullable_fields = ["id", "name", "userId"]
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


class Get3DModelByIDResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /api/rest/v1/models-3d/{id}"""

    model_assets_by_pk: NotRequired[Nullable[Get3DModelByIDModelAssetsTypedDict]]
    r"""columns and relationships of \"model_assets\" """


class Get3DModelByIDResponseBody(BaseModel):
    r"""Responses for GET /api/rest/v1/models-3d/{id}"""

    model_assets_by_pk: OptionalNullable[Get3DModelByIDModelAssets] = UNSET
    r"""columns and relationships of \"model_assets\" """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["model_assets_by_pk"]
        nullable_fields = ["model_assets_by_pk"]
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


class Get3DModelByIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[Get3DModelByIDResponseBodyTypedDict]
    r"""Responses for GET /api/rest/v1/models-3d/{id}"""


class Get3DModelByIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[Get3DModelByIDResponseBody] = None
    r"""Responses for GET /api/rest/v1/models-3d/{id}"""
