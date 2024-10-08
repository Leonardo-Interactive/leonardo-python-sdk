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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetDatasetByIDRequestTypedDict(TypedDict):
    id: str
    r"""The ID of the dataset to return."""


class GetDatasetByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the dataset to return."""


class DatasetImagesTypedDict(TypedDict):
    r"""columns and relationships of \"dataset_images\" """

    created_at: NotRequired[str]
    id: NotRequired[Nullable[str]]
    url: NotRequired[str]


class DatasetImages(BaseModel):
    r"""columns and relationships of \"dataset_images\" """

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


class GetDatasetByIDDatasetsTypedDict(TypedDict):
    r"""columns and relationships of \"datasets\" """

    created_at: NotRequired[str]
    dataset_images: NotRequired[List[DatasetImagesTypedDict]]
    description: NotRequired[Nullable[str]]
    id: NotRequired[Nullable[str]]
    name: NotRequired[str]
    updated_at: NotRequired[str]


class GetDatasetByIDDatasets(BaseModel):
    r"""columns and relationships of \"datasets\" """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None

    dataset_images: Optional[List[DatasetImages]] = None

    description: OptionalNullable[str] = UNSET

    id: OptionalNullable[str] = UNSET

    name: Optional[str] = None

    updated_at: Annotated[Optional[str], pydantic.Field(alias="updatedAt")] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "createdAt",
            "dataset_images",
            "description",
            "id",
            "name",
            "updatedAt",
        ]
        nullable_fields = ["description", "id"]
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


class GetDatasetByIDResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /datasets/{id}"""

    datasets_by_pk: NotRequired[Nullable[GetDatasetByIDDatasetsTypedDict]]
    r"""columns and relationships of \"datasets\" """


class GetDatasetByIDResponseBody(BaseModel):
    r"""Responses for GET /datasets/{id}"""

    datasets_by_pk: OptionalNullable[GetDatasetByIDDatasets] = UNSET
    r"""columns and relationships of \"datasets\" """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["datasets_by_pk"]
        nullable_fields = ["datasets_by_pk"]
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


class GetDatasetByIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetDatasetByIDResponseBodyTypedDict]
    r"""Responses for GET /datasets/{id}"""


class GetDatasetByIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetDatasetByIDResponseBody] = None
    r"""Responses for GET /datasets/{id}"""
