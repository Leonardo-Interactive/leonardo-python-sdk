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


class CreateVariationNoBGRequestBodyTypedDict(TypedDict):
    r"""Query parameters are provided in the request body as a JSON object"""

    id: str
    is_variation: NotRequired[bool]


class CreateVariationNoBGRequestBody(BaseModel):
    r"""Query parameters are provided in the request body as a JSON object"""

    id: str

    is_variation: Annotated[Optional[bool], pydantic.Field(alias="isVariation")] = None


class SDUpscaleJobOutputTypedDict(TypedDict):
    api_credit_cost: NotRequired[Nullable[int]]
    r"""API Credits Cost for No Background Variation. Available for Production API Users."""
    id: NotRequired[Nullable[str]]


class SDUpscaleJobOutput(BaseModel):
    api_credit_cost: Annotated[
        OptionalNullable[int], pydantic.Field(alias="apiCreditCost")
    ] = UNSET
    r"""API Credits Cost for No Background Variation. Available for Production API Users."""

    id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["apiCreditCost", "id"]
        nullable_fields = ["apiCreditCost", "id"]
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


class CreateVariationNoBGResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /variations/nobg"""

    sd_nobg_job: NotRequired[SDUpscaleJobOutputTypedDict]


class CreateVariationNoBGResponseBody(BaseModel):
    r"""Responses for POST /variations/nobg"""

    sd_nobg_job: Annotated[
        Optional[SDUpscaleJobOutput], pydantic.Field(alias="sdNobgJob")
    ] = None


class CreateVariationNoBGResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[CreateVariationNoBGResponseBodyTypedDict]
    r"""Responses for POST /variations/nobg"""


class CreateVariationNoBGResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[CreateVariationNoBGResponseBody] = None
    r"""Responses for POST /variations/nobg"""
