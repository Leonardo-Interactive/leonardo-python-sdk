"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import (
    pricingcalculatorservices as shared_pricingcalculatorservices,
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
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PricingCalculatorObjectTypedDict(TypedDict):
    r"""Parameters for FANTASY_AVATAR_GENERATION service"""

    image_height: NotRequired[int]
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""
    image_width: NotRequired[int]
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""
    num_images: NotRequired[int]
    r"""The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4."""


class PricingCalculatorObject(BaseModel):
    r"""Parameters for FANTASY_AVATAR_GENERATION service"""

    image_height: Annotated[Optional[int], pydantic.Field(alias="imageHeight")] = None
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""

    image_width: Annotated[Optional[int], pydantic.Field(alias="imageWidth")] = None
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""

    num_images: Annotated[Optional[int], pydantic.Field(alias="numImages")] = None
    r"""The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4."""


class PricingCalculatorPricingCalculatorObjectTypedDict(TypedDict):
    r"""Parameters for IMAGE_GENERATION service"""

    alchemy_mode: NotRequired[bool]
    r"""Enable to use Alchemy."""
    controlnets_cost: NotRequired[Nullable[int]]
    r"""The total cost of controlnets input."""
    high_resolution: NotRequired[bool]
    r"""Enable to use high resolution."""
    image_height: NotRequired[int]
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""
    image_width: NotRequired[int]
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""
    inference_steps: NotRequired[int]
    r"""The Step Count to use for the generation. Must be between 10 and 60."""
    is_model_custom: NotRequired[Nullable[bool]]
    r"""Enable to use custom model."""
    is_phoenix: NotRequired[Nullable[bool]]
    r"""Enable to use Phoenix model."""
    is_sdxl: NotRequired[Nullable[bool]]
    r"""Enable to use SDXL model."""
    is_sdxl_lightning: NotRequired[Nullable[bool]]
    r"""Enable to use SDXL Lightning model."""
    lora_count: NotRequired[Nullable[int]]
    r"""The number of elements used for the generation."""
    num_images: NotRequired[int]
    r"""The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4."""
    photo_real_mode: NotRequired[Nullable[bool]]
    r"""Enable to use PhotoReal. Requires enabling alchemy."""
    photo_real_strength: NotRequired[Nullable[float]]
    r"""Depth of field of photoReal. Must be 0.55 for low, 0.5 for medium, or 0.45 for high. Defaults to 0.55 if not specified."""
    photo_real_version: NotRequired[Nullable[str]]
    r"""The version of photoReal to use. Must be v1 or v2."""
    prompt_magic: NotRequired[Nullable[bool]]
    r"""Enable to use Prompt Magic."""
    prompt_magic_strength: NotRequired[Nullable[float]]
    r"""Strength of prompt magic. Must be a float between 0.1 and 1.0"""
    prompt_magic_version: NotRequired[Nullable[str]]
    r"""Prompt magic version v2 or v3, for use when promptMagic: true"""
    ultra: NotRequired[Nullable[bool]]
    r"""Enable to use Ultra mode."""


class PricingCalculatorPricingCalculatorObject(BaseModel):
    r"""Parameters for IMAGE_GENERATION service"""

    alchemy_mode: Annotated[Optional[bool], pydantic.Field(alias="alchemyMode")] = None
    r"""Enable to use Alchemy."""

    controlnets_cost: Annotated[
        OptionalNullable[int], pydantic.Field(alias="controlnetsCost")
    ] = UNSET
    r"""The total cost of controlnets input."""

    high_resolution: Annotated[
        Optional[bool], pydantic.Field(alias="highResolution")
    ] = None
    r"""Enable to use high resolution."""

    image_height: Annotated[Optional[int], pydantic.Field(alias="imageHeight")] = None
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""

    image_width: Annotated[Optional[int], pydantic.Field(alias="imageWidth")] = None
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features"""

    inference_steps: Annotated[
        Optional[int], pydantic.Field(alias="inferenceSteps")
    ] = None
    r"""The Step Count to use for the generation. Must be between 10 and 60."""

    is_model_custom: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="isModelCustom")
    ] = UNSET
    r"""Enable to use custom model."""

    is_phoenix: Annotated[OptionalNullable[bool], pydantic.Field(alias="isPhoenix")] = (
        UNSET
    )
    r"""Enable to use Phoenix model."""

    is_sdxl: Annotated[OptionalNullable[bool], pydantic.Field(alias="isSDXL")] = UNSET
    r"""Enable to use SDXL model."""

    is_sdxl_lightning: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="isSDXLLightning")
    ] = UNSET
    r"""Enable to use SDXL Lightning model."""

    lora_count: Annotated[OptionalNullable[int], pydantic.Field(alias="loraCount")] = (
        UNSET
    )
    r"""The number of elements used for the generation."""

    num_images: Annotated[Optional[int], pydantic.Field(alias="numImages")] = None
    r"""The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4."""

    photo_real_mode: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="photoRealMode")
    ] = UNSET
    r"""Enable to use PhotoReal. Requires enabling alchemy."""

    photo_real_strength: Annotated[
        OptionalNullable[float], pydantic.Field(alias="photoRealStrength")
    ] = UNSET
    r"""Depth of field of photoReal. Must be 0.55 for low, 0.5 for medium, or 0.45 for high. Defaults to 0.55 if not specified."""

    photo_real_version: Annotated[
        OptionalNullable[str], pydantic.Field(alias="photoRealVersion")
    ] = UNSET
    r"""The version of photoReal to use. Must be v1 or v2."""

    prompt_magic: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="promptMagic")
    ] = UNSET
    r"""Enable to use Prompt Magic."""

    prompt_magic_strength: Annotated[
        OptionalNullable[float], pydantic.Field(alias="promptMagicStrength")
    ] = UNSET
    r"""Strength of prompt magic. Must be a float between 0.1 and 1.0"""

    prompt_magic_version: Annotated[
        OptionalNullable[str], pydantic.Field(alias="promptMagicVersion")
    ] = UNSET
    r"""Prompt magic version v2 or v3, for use when promptMagic: true"""

    ultra: OptionalNullable[bool] = UNSET
    r"""Enable to use Ultra mode."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "alchemyMode",
            "controlnetsCost",
            "highResolution",
            "imageHeight",
            "imageWidth",
            "inferenceSteps",
            "isModelCustom",
            "isPhoenix",
            "isSDXL",
            "isSDXLLightning",
            "loraCount",
            "numImages",
            "photoRealMode",
            "photoRealStrength",
            "photoRealVersion",
            "promptMagic",
            "promptMagicStrength",
            "promptMagicVersion",
            "ultra",
        ]
        nullable_fields = [
            "controlnetsCost",
            "isModelCustom",
            "isPhoenix",
            "isSDXL",
            "isSDXLLightning",
            "loraCount",
            "photoRealMode",
            "photoRealStrength",
            "photoRealVersion",
            "promptMagic",
            "promptMagicStrength",
            "promptMagicVersion",
            "ultra",
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


class PricingCalculatorPricingCalculatorRequestObjectTypedDict(TypedDict):
    r"""Parameters for LCM_GENERATION service"""

    height: NotRequired[Nullable[int]]
    r"""The output height of the image. Must be 512, 640 or 1024."""
    instant_refine: NotRequired[Nullable[bool]]
    r"""Enable for instant upscale"""
    refine: NotRequired[Nullable[bool]]
    r"""Enable for normal alchemy upscale"""
    width: NotRequired[Nullable[int]]
    r"""The output width of the image. Must be 512, 640 or 1024."""


class PricingCalculatorPricingCalculatorRequestObject(BaseModel):
    r"""Parameters for LCM_GENERATION service"""

    height: OptionalNullable[int] = UNSET
    r"""The output height of the image. Must be 512, 640 or 1024."""

    instant_refine: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="instantRefine")
    ] = UNSET
    r"""Enable for instant upscale"""

    refine: OptionalNullable[bool] = UNSET
    r"""Enable for normal alchemy upscale"""

    width: OptionalNullable[int] = UNSET
    r"""The output width of the image. Must be 512, 640 or 1024."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["height", "instantRefine", "refine", "width"]
        nullable_fields = ["height", "instantRefine", "refine", "width"]
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


class PricingCalculatorPricingCalculatorRequestRequestBodyObjectTypedDict(TypedDict):
    r"""Parameters for MODEL_TRAINING service"""

    resolution: NotRequired[int]
    r"""The resolution for training. Must be 512 or 768."""


class PricingCalculatorPricingCalculatorRequestRequestBodyObject(BaseModel):
    r"""Parameters for MODEL_TRAINING service"""

    resolution: Optional[int] = None
    r"""The resolution for training. Must be 512 or 768."""


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsObjectTypedDict(
    TypedDict
):
    r"""Parameters for MOTION_GENERATION service"""

    duration_seconds: NotRequired[int]
    r"""The total duration of the motion generation in seconds."""


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsObject(
    BaseModel
):
    r"""Parameters for MOTION_GENERATION service"""

    duration_seconds: Annotated[
        Optional[int], pydantic.Field(alias="durationSeconds")
    ] = None
    r"""The total duration of the motion generation in seconds."""


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsTEXTUREGENERATIONObjectTypedDict(
    TypedDict
):
    r"""Parameters for TEXTURE_GENERATION service"""

    preview: NotRequired[bool]


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsTEXTUREGENERATIONObject(
    BaseModel
):
    r"""Parameters for TEXTURE_GENERATION service"""

    preview: Optional[bool] = None


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERObjectTypedDict(
    TypedDict
):
    r"""Parameters for UNIVERSAL_UPSCALER service"""

    megapixel: NotRequired[int]
    r"""The maximum upscaled image size is 20 megapixels."""


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERObject(
    BaseModel
):
    r"""Parameters for UNIVERSAL_UPSCALER service"""

    megapixel: Optional[int] = None
    r"""The maximum upscaled image size is 20 megapixels."""


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERULTRAObjectTypedDict(
    TypedDict
):
    r"""Parameters for UNIVERSAL_UPSCALER_ULTRA service"""

    input_height: NotRequired[int]
    r"""The input height of the image."""
    input_width: NotRequired[int]
    r"""The input width of the image."""
    upscale_multiplier: NotRequired[float]
    r"""The upscale multiplier of the universal upscaler. Must be between 1.00 and 2.00."""


class PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERULTRAObject(
    BaseModel
):
    r"""Parameters for UNIVERSAL_UPSCALER_ULTRA service"""

    input_height: Annotated[Optional[int], pydantic.Field(alias="inputHeight")] = None
    r"""The input height of the image."""

    input_width: Annotated[Optional[int], pydantic.Field(alias="inputWidth")] = None
    r"""The input width of the image."""

    upscale_multiplier: Annotated[
        Optional[float], pydantic.Field(alias="upscaleMultiplier")
    ] = 1.5
    r"""The upscale multiplier of the universal upscaler. Must be between 1.00 and 2.00."""


class ObjectTypedDict(TypedDict):
    r"""Parameters for the service"""

    fantasy_avatar_generation: NotRequired[Nullable[PricingCalculatorObjectTypedDict]]
    r"""Parameters for FANTASY_AVATAR_GENERATION service"""
    image_generation: NotRequired[
        Nullable[PricingCalculatorPricingCalculatorObjectTypedDict]
    ]
    r"""Parameters for IMAGE_GENERATION service"""
    lcm_generation: NotRequired[
        Nullable[PricingCalculatorPricingCalculatorRequestObjectTypedDict]
    ]
    r"""Parameters for LCM_GENERATION service"""
    model_training: NotRequired[
        Nullable[PricingCalculatorPricingCalculatorRequestRequestBodyObjectTypedDict]
    ]
    r"""Parameters for MODEL_TRAINING service"""
    motion_generation: NotRequired[
        Nullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsObjectTypedDict
        ]
    ]
    r"""Parameters for MOTION_GENERATION service"""
    texture_generation: NotRequired[
        Nullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsTEXTUREGENERATIONObjectTypedDict
        ]
    ]
    r"""Parameters for TEXTURE_GENERATION service"""
    universal_upscaler: NotRequired[
        Nullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERObjectTypedDict
        ]
    ]
    r"""Parameters for UNIVERSAL_UPSCALER service"""
    universal_upscaler_ultra: NotRequired[
        Nullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERULTRAObjectTypedDict
        ]
    ]
    r"""Parameters for UNIVERSAL_UPSCALER_ULTRA service"""


class Object(BaseModel):
    r"""Parameters for the service"""

    fantasy_avatar_generation: Annotated[
        OptionalNullable[PricingCalculatorObject],
        pydantic.Field(alias="FANTASY_AVATAR_GENERATION"),
    ] = UNSET
    r"""Parameters for FANTASY_AVATAR_GENERATION service"""

    image_generation: Annotated[
        OptionalNullable[PricingCalculatorPricingCalculatorObject],
        pydantic.Field(alias="IMAGE_GENERATION"),
    ] = UNSET
    r"""Parameters for IMAGE_GENERATION service"""

    lcm_generation: Annotated[
        OptionalNullable[PricingCalculatorPricingCalculatorRequestObject],
        pydantic.Field(alias="LCM_GENERATION"),
    ] = UNSET
    r"""Parameters for LCM_GENERATION service"""

    model_training: Annotated[
        OptionalNullable[PricingCalculatorPricingCalculatorRequestRequestBodyObject],
        pydantic.Field(alias="MODEL_TRAINING"),
    ] = UNSET
    r"""Parameters for MODEL_TRAINING service"""

    motion_generation: Annotated[
        OptionalNullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsObject
        ],
        pydantic.Field(alias="MOTION_GENERATION"),
    ] = UNSET
    r"""Parameters for MOTION_GENERATION service"""

    texture_generation: Annotated[
        OptionalNullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsTEXTUREGENERATIONObject
        ],
        pydantic.Field(alias="TEXTURE_GENERATION"),
    ] = UNSET
    r"""Parameters for TEXTURE_GENERATION service"""

    universal_upscaler: Annotated[
        OptionalNullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERObject
        ],
        pydantic.Field(alias="UNIVERSAL_UPSCALER"),
    ] = UNSET
    r"""Parameters for UNIVERSAL_UPSCALER service"""

    universal_upscaler_ultra: Annotated[
        OptionalNullable[
            PricingCalculatorPricingCalculatorRequestRequestBodyServiceParamsUNIVERSALUPSCALERULTRAObject
        ],
        pydantic.Field(alias="UNIVERSAL_UPSCALER_ULTRA"),
    ] = UNSET
    r"""Parameters for UNIVERSAL_UPSCALER_ULTRA service"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "FANTASY_AVATAR_GENERATION",
            "IMAGE_GENERATION",
            "LCM_GENERATION",
            "MODEL_TRAINING",
            "MOTION_GENERATION",
            "TEXTURE_GENERATION",
            "UNIVERSAL_UPSCALER",
            "UNIVERSAL_UPSCALER_ULTRA",
        ]
        nullable_fields = [
            "FANTASY_AVATAR_GENERATION",
            "IMAGE_GENERATION",
            "LCM_GENERATION",
            "MODEL_TRAINING",
            "MOTION_GENERATION",
            "TEXTURE_GENERATION",
            "UNIVERSAL_UPSCALER",
            "UNIVERSAL_UPSCALER_ULTRA",
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


class PricingCalculatorRequestBodyTypedDict(TypedDict):
    service: NotRequired[shared_pricingcalculatorservices.PricingCalculatorServices]
    r"""The services to be chosen for calculating the API credit cost."""
    service_params: NotRequired[ObjectTypedDict]
    r"""Parameters for the service"""


class PricingCalculatorRequestBody(BaseModel):
    service: Optional[shared_pricingcalculatorservices.PricingCalculatorServices] = None
    r"""The services to be chosen for calculating the API credit cost."""

    service_params: Annotated[
        Optional[Object], pydantic.Field(alias="serviceParams")
    ] = None
    r"""Parameters for the service"""


class CalculateProductionAPIServiceCostTypedDict(TypedDict):
    cost: NotRequired[int]
    r"""API service cost to generate the image."""


class CalculateProductionAPIServiceCost(BaseModel):
    cost: Optional[int] = None
    r"""API service cost to generate the image."""


class PricingCalculatorResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /pricing-calculator"""

    calculate_production_api_service_cost: NotRequired[
        Nullable[CalculateProductionAPIServiceCostTypedDict]
    ]


class PricingCalculatorResponseBody(BaseModel):
    r"""Responses for POST /pricing-calculator"""

    calculate_production_api_service_cost: Annotated[
        OptionalNullable[CalculateProductionAPIServiceCost],
        pydantic.Field(alias="calculateProductionApiServiceCost"),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["calculateProductionApiServiceCost"]
        nullable_fields = ["calculateProductionApiServiceCost"]
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


class PricingCalculatorResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[PricingCalculatorResponseBodyTypedDict]
    r"""Responses for POST /pricing-calculator"""


class PricingCalculatorResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[PricingCalculatorResponseBody] = None
    r"""Responses for POST /pricing-calculator"""
