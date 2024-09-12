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
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CreateDatasetRequestBodyTypedDict(TypedDict):
    r"""Query parameters to be provided in the request body as a JSON object"""

    name: str
    r"""The name of the dataset."""
    description: NotRequired[Nullable[str]]
    r"""A description for the dataset."""


class CreateDatasetRequestBody(BaseModel):
    r"""Query parameters to be provided in the request body as a JSON object"""

    name: str
    r"""The name of the dataset."""

    description: OptionalNullable[str] = UNSET
    r"""A description for the dataset."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description"]
        nullable_fields = ["description"]
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


class DatasetsTypedDict(TypedDict):
    r"""columns and relationships of \"datasets\" """

    id: NotRequired[Nullable[str]]


class Datasets(BaseModel):
    r"""columns and relationships of \"datasets\" """

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


class CreateDatasetResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /datasets"""

    insert_datasets_one: NotRequired[Nullable[DatasetsTypedDict]]
    r"""columns and relationships of \"datasets\" """


class CreateDatasetResponseBody(BaseModel):
    r"""Responses for POST /datasets"""

    insert_datasets_one: OptionalNullable[Datasets] = UNSET
    r"""columns and relationships of \"datasets\" """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["insert_datasets_one"]
        nullable_fields = ["insert_datasets_one"]
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


class CreateDatasetResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[CreateDatasetResponseBodyTypedDict]
    r"""Responses for POST /datasets"""


class CreateDatasetResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[CreateDatasetResponseBody] = None
    r"""Responses for POST /datasets"""
