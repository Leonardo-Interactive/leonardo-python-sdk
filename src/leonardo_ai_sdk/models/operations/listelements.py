"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import sd_versions as shared_sd_versions
from leonardo_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LorasTypedDict(TypedDict):
    r"""columns and relationships of \"elements\" """

    ak_uuid: NotRequired[Nullable[str]]
    r"""Unique identifier for the element. Elements can be found from the List Elements endpoint."""
    base_model: NotRequired[shared_sd_versions.SdVersions]
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
    creator_name: NotRequired[Nullable[str]]
    r"""Name of the creator of the element"""
    description: NotRequired[Nullable[str]]
    r"""Description for the element"""
    name: NotRequired[Nullable[str]]
    r"""Name of the element"""
    url_image: NotRequired[Nullable[str]]
    r"""URL of the element image"""
    weight_default: NotRequired[Nullable[int]]
    r"""Default weight for the element"""
    weight_max: NotRequired[Nullable[int]]
    r"""Maximum weight for the element"""
    weight_min: NotRequired[Nullable[int]]
    r"""Minimum weight for the element"""


class Loras(BaseModel):
    r"""columns and relationships of \"elements\" """

    ak_uuid: Annotated[OptionalNullable[str], pydantic.Field(alias="akUUID")] = UNSET
    r"""Unique identifier for the element. Elements can be found from the List Elements endpoint."""

    base_model: Annotated[
        Optional[shared_sd_versions.SdVersions], pydantic.Field(alias="baseModel")
    ] = None
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""

    creator_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="creatorName")
    ] = UNSET
    r"""Name of the creator of the element"""

    description: OptionalNullable[str] = UNSET
    r"""Description for the element"""

    name: OptionalNullable[str] = UNSET
    r"""Name of the element"""

    url_image: Annotated[OptionalNullable[str], pydantic.Field(alias="urlImage")] = (
        UNSET
    )
    r"""URL of the element image"""

    weight_default: Annotated[
        OptionalNullable[int], pydantic.Field(alias="weightDefault")
    ] = UNSET
    r"""Default weight for the element"""

    weight_max: Annotated[OptionalNullable[int], pydantic.Field(alias="weightMax")] = (
        UNSET
    )
    r"""Maximum weight for the element"""

    weight_min: Annotated[OptionalNullable[int], pydantic.Field(alias="weightMin")] = (
        UNSET
    )
    r"""Minimum weight for the element"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "akUUID",
            "baseModel",
            "creatorName",
            "description",
            "name",
            "urlImage",
            "weightDefault",
            "weightMax",
            "weightMin",
        ]
        nullable_fields = [
            "akUUID",
            "creatorName",
            "description",
            "name",
            "urlImage",
            "weightDefault",
            "weightMax",
            "weightMin",
        ]
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


class ListElementsResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /api/rest/v1/elements"""

    loras: NotRequired[List[LorasTypedDict]]


class ListElementsResponseBody(BaseModel):
    r"""Responses for GET /api/rest/v1/elements"""

    loras: Optional[List[Loras]] = None


class ListElementsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[ListElementsResponseBodyTypedDict]
    r"""Responses for GET /api/rest/v1/elements"""


class ListElementsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[ListElementsResponseBody] = None
    r"""Responses for GET /api/rest/v1/elements"""
