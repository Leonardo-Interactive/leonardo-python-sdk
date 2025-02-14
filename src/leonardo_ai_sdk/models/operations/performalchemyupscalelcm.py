"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import (
    lcm_generation_style as shared_lcm_generation_style,
)
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


class PerformAlchemyUpscaleLCMRequestBodyTypedDict(TypedDict):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    image_data_url: str
    r"""Image data used to generate image. In base64 format. Prefix: `data:image/jpeg;base64,`"""
    prompt: str
    r"""The prompt used to generate images"""
    guidance: NotRequired[Nullable[float]]
    r"""How strongly the generation should reflect the prompt. Must be a float between 0.5 and 20."""
    height: NotRequired[Nullable[int]]
    r"""The output width of the image. Must be 512, 640 or 1024."""
    refine_creative: NotRequired[Nullable[bool]]
    r"""Refine creative"""
    refine_strength: NotRequired[Nullable[float]]
    r"""Must be a float between 0.5 and 0.9."""
    request_timestamp: NotRequired[str]
    seed: NotRequired[Nullable[int]]
    r"""Apply a fixed seed to maintain consistency across generation sets. The maximum seed value is 2147483637 for Flux and 9999999998 for other models"""
    steps: NotRequired[Nullable[int]]
    r"""The number of steps to use for the generation. Must be between 4 and 16."""
    strength: NotRequired[Nullable[float]]
    r"""Creativity strength of generation. Higher strength will deviate more from the original image supplied in imageDataUrl. Must be a float between 0.1 and 1."""
    style: NotRequired[Nullable[shared_lcm_generation_style.LcmGenerationStyle]]
    r"""The style to generate LCM images with."""
    width: NotRequired[Nullable[int]]
    r"""The output width of the image. Must be 512, 640 or 1024."""


class PerformAlchemyUpscaleLCMRequestBody(BaseModel):
    r"""Query parameters can also be provided in the request body as a JSON object"""

    image_data_url: Annotated[str, pydantic.Field(alias="imageDataUrl")]
    r"""Image data used to generate image. In base64 format. Prefix: `data:image/jpeg;base64,`"""

    prompt: str
    r"""The prompt used to generate images"""

    guidance: OptionalNullable[float] = UNSET
    r"""How strongly the generation should reflect the prompt. Must be a float between 0.5 and 20."""

    height: OptionalNullable[int] = 512
    r"""The output width of the image. Must be 512, 640 or 1024."""

    refine_creative: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="refineCreative")
    ] = UNSET
    r"""Refine creative"""

    refine_strength: Annotated[
        OptionalNullable[float], pydantic.Field(alias="refineStrength")
    ] = UNSET
    r"""Must be a float between 0.5 and 0.9."""

    request_timestamp: Annotated[
        Optional[str], pydantic.Field(alias="requestTimestamp")
    ] = None

    seed: OptionalNullable[int] = UNSET
    r"""Apply a fixed seed to maintain consistency across generation sets. The maximum seed value is 2147483637 for Flux and 9999999998 for other models"""

    steps: OptionalNullable[int] = UNSET
    r"""The number of steps to use for the generation. Must be between 4 and 16."""

    strength: OptionalNullable[float] = UNSET
    r"""Creativity strength of generation. Higher strength will deviate more from the original image supplied in imageDataUrl. Must be a float between 0.1 and 1."""

    style: OptionalNullable[shared_lcm_generation_style.LcmGenerationStyle] = UNSET
    r"""The style to generate LCM images with."""

    width: OptionalNullable[int] = 512
    r"""The output width of the image. Must be 512, 640 or 1024."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "guidance",
            "height",
            "refineCreative",
            "refineStrength",
            "requestTimestamp",
            "seed",
            "steps",
            "strength",
            "style",
            "width",
        ]
        nullable_fields = [
            "guidance",
            "height",
            "refineCreative",
            "refineStrength",
            "seed",
            "steps",
            "strength",
            "style",
            "width",
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


class PerformAlchemyUpscaleLCMLCMGenerationOutputTypedDict(TypedDict):
    api_credit_cost: NotRequired[Nullable[int]]
    r"""API credits cost, available for Production API users."""
    generated_image_id: NotRequired[str]
    generation_id: NotRequired[List[str]]
    image_data_url: NotRequired[List[str]]
    request_timestamp: NotRequired[str]
    variation_id: NotRequired[List[str]]


class PerformAlchemyUpscaleLCMLCMGenerationOutput(BaseModel):
    api_credit_cost: Annotated[
        OptionalNullable[int], pydantic.Field(alias="apiCreditCost")
    ] = UNSET
    r"""API credits cost, available for Production API users."""

    generated_image_id: Annotated[
        Optional[str], pydantic.Field(alias="generatedImageId")
    ] = None

    generation_id: Annotated[
        Optional[List[str]], pydantic.Field(alias="generationId")
    ] = None

    image_data_url: Annotated[
        Optional[List[str]], pydantic.Field(alias="imageDataUrl")
    ] = None

    request_timestamp: Annotated[
        Optional[str], pydantic.Field(alias="requestTimestamp")
    ] = None

    variation_id: Annotated[
        Optional[List[str]], pydantic.Field(alias="variationId")
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "apiCreditCost",
            "generatedImageId",
            "generationId",
            "imageDataUrl",
            "requestTimestamp",
            "variationId",
        ]
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


class PerformAlchemyUpscaleLCMResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /lcm-upscale"""

    lcm_generation_job: NotRequired[
        Nullable[PerformAlchemyUpscaleLCMLCMGenerationOutputTypedDict]
    ]


class PerformAlchemyUpscaleLCMResponseBody(BaseModel):
    r"""Responses for POST /lcm-upscale"""

    lcm_generation_job: Annotated[
        OptionalNullable[PerformAlchemyUpscaleLCMLCMGenerationOutput],
        pydantic.Field(alias="lcmGenerationJob"),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["lcmGenerationJob"]
        nullable_fields = ["lcmGenerationJob"]
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


class PerformAlchemyUpscaleLCMResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[PerformAlchemyUpscaleLCMResponseBodyTypedDict]
    r"""Responses for POST /lcm-upscale"""


class PerformAlchemyUpscaleLCMResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[PerformAlchemyUpscaleLCMResponseBody] = None
    r"""Responses for POST /lcm-upscale"""
