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
from leonardo_ai_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UploadDatasetImageRequestBodyTypedDict(TypedDict):
    r"""Query parameters provided in the request body as a JSON object"""

    extension: str
    r"""Has to be png, jpg, jpeg, or webp."""


class UploadDatasetImageRequestBody(BaseModel):
    r"""Query parameters provided in the request body as a JSON object"""

    extension: str
    r"""Has to be png, jpg, jpeg, or webp."""


class UploadDatasetImageRequestTypedDict(TypedDict):
    request_body: UploadDatasetImageRequestBodyTypedDict
    r"""Query parameters provided in the request body as a JSON object"""
    dataset_id: str
    r"""_\"datasetId\" is required"""


class UploadDatasetImageRequest(BaseModel):
    request_body: Annotated[
        UploadDatasetImageRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Query parameters provided in the request body as a JSON object"""

    dataset_id: Annotated[
        str,
        pydantic.Field(alias="datasetId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""_\"datasetId\" is required"""


class DatasetUploadOutputTypedDict(TypedDict):
    fields: NotRequired[Nullable[str]]
    id: NotRequired[Nullable[str]]
    key: NotRequired[Nullable[str]]
    url: NotRequired[Nullable[str]]


class DatasetUploadOutput(BaseModel):
    fields: OptionalNullable[str] = UNSET

    id: OptionalNullable[str] = UNSET

    key: OptionalNullable[str] = UNSET

    url: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["fields", "id", "key", "url"]
        nullable_fields = ["fields", "id", "key", "url"]
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


class UploadDatasetImageResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /datasets/{datasetId}/upload"""

    upload_dataset_image: NotRequired[Nullable[DatasetUploadOutputTypedDict]]


class UploadDatasetImageResponseBody(BaseModel):
    r"""Responses for POST /datasets/{datasetId}/upload"""

    upload_dataset_image: Annotated[
        OptionalNullable[DatasetUploadOutput],
        pydantic.Field(alias="uploadDatasetImage"),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["uploadDatasetImage"]
        nullable_fields = ["uploadDatasetImage"]
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


class UploadDatasetImageResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[UploadDatasetImageResponseBodyTypedDict]
    r"""Responses for POST /datasets/{datasetId}/upload"""


class UploadDatasetImageResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[UploadDatasetImageResponseBody] = None
    r"""Responses for POST /datasets/{datasetId}/upload"""