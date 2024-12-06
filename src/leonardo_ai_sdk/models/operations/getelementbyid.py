"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import job_status as shared_job_status
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


class GetElementByIDRequestTypedDict(TypedDict):
    id: int
    r"""The ID of the custom element to return."""


class GetElementByIDRequest(BaseModel):
    id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the custom element to return."""


class GetElementByIDUserLorasTypedDict(TypedDict):
    r"""columns and relationships of \"user_loras\"."""

    base_model: NotRequired[str]
    created_at: NotRequired[str]
    description: NotRequired[str]
    focus: NotRequired[str]
    id: NotRequired[int]
    instance_prompt: NotRequired[Nullable[str]]
    learning_rate: NotRequired[float]
    name: NotRequired[str]
    resolution: NotRequired[int]
    status: NotRequired[shared_job_status.JobStatus]
    r"""The status of the current task."""
    train_text_encoder: NotRequired[bool]
    training_epoch: NotRequired[int]
    updated_at: NotRequired[str]


class GetElementByIDUserLoras(BaseModel):
    r"""columns and relationships of \"user_loras\"."""

    base_model: Annotated[Optional[str], pydantic.Field(alias="baseModel")] = None

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None

    description: Optional[str] = None

    focus: Optional[str] = None

    id: Optional[int] = None

    instance_prompt: Annotated[
        OptionalNullable[str], pydantic.Field(alias="instancePrompt")
    ] = UNSET

    learning_rate: Annotated[Optional[float], pydantic.Field(alias="learningRate")] = (
        None
    )

    name: Optional[str] = None

    resolution: Optional[int] = None

    status: Optional[shared_job_status.JobStatus] = None
    r"""The status of the current task."""

    train_text_encoder: Annotated[
        Optional[bool], pydantic.Field(alias="trainTextEncoder")
    ] = None

    training_epoch: Annotated[Optional[int], pydantic.Field(alias="trainingEpoch")] = (
        None
    )

    updated_at: Annotated[Optional[str], pydantic.Field(alias="updatedAt")] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "baseModel",
            "createdAt",
            "description",
            "focus",
            "id",
            "instancePrompt",
            "learningRate",
            "name",
            "resolution",
            "status",
            "trainTextEncoder",
            "trainingEpoch",
            "updatedAt",
        ]
        nullable_fields = ["instancePrompt"]
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


class GetElementByIDResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /elements/{id}."""

    user_loras_by_pk: NotRequired[Nullable[GetElementByIDUserLorasTypedDict]]
    r"""columns and relationships of \"user_loras\"."""


class GetElementByIDResponseBody(BaseModel):
    r"""Responses for GET /elements/{id}."""

    user_loras_by_pk: OptionalNullable[GetElementByIDUserLoras] = UNSET
    r"""columns and relationships of \"user_loras\"."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["user_loras_by_pk"]
        nullable_fields = ["user_loras_by_pk"]
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


class GetElementByIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetElementByIDResponseBodyTypedDict]
    r"""Responses for GET /elements/{id}."""


class GetElementByIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetElementByIDResponseBody] = None
    r"""Responses for GET /elements/{id}."""
