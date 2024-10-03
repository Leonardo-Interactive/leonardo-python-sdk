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


class CreateVariationUnzoomRequestBodyTypedDict(TypedDict):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    id: NotRequired[str]
    is_variation: NotRequired[Nullable[bool]]


class CreateVariationUnzoomRequestBody(BaseModel):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    id: Optional[str] = None

    is_variation: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="isVariation")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "isVariation"]
        nullable_fields = ["isVariation"]
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


class SDUnzoomOutputTypedDict(TypedDict):
    api_credit_cost: NotRequired[Nullable[int]]
    r"""API Credits Cost for Unzoom Variation. Available for Production API Users."""
    id: NotRequired[str]


class SDUnzoomOutput(BaseModel):
    api_credit_cost: Annotated[
        OptionalNullable[int], pydantic.Field(alias="apiCreditCost")
    ] = UNSET
    r"""API Credits Cost for Unzoom Variation. Available for Production API Users."""

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


class CreateVariationUnzoomResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /api/rest/v1/variations/unzoom"""

    sd_unzoom_job: NotRequired[Nullable[SDUnzoomOutputTypedDict]]


class CreateVariationUnzoomResponseBody(BaseModel):
    r"""Responses for POST /api/rest/v1/variations/unzoom"""

    sd_unzoom_job: Annotated[
        OptionalNullable[SDUnzoomOutput], pydantic.Field(alias="sdUnzoomJob")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["sdUnzoomJob"]
        nullable_fields = ["sdUnzoomJob"]
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


class CreateVariationUnzoomResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[CreateVariationUnzoomResponseBodyTypedDict]
    r"""Responses for POST /api/rest/v1/variations/unzoom"""


class CreateVariationUnzoomResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[CreateVariationUnzoomResponseBody] = None
    r"""Responses for POST /api/rest/v1/variations/unzoom"""
