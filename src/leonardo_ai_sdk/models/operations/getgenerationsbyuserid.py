"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import (
    job_status as shared_job_status,
    sd_generation_schedulers as shared_sd_generation_schedulers,
    sd_generation_style as shared_sd_generation_style,
    sd_versions as shared_sd_versions,
    variation_type as shared_variation_type,
)
from leonardo_ai_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from leonardo_ai_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetGenerationsByUserIDRequestTypedDict(TypedDict):
    user_id: str
    limit: NotRequired[int]
    offset: NotRequired[int]


class GetGenerationsByUserIDRequest(BaseModel):
    user_id: Annotated[
        str,
        pydantic.Field(alias="userId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0


class GetGenerationsByUserIDGeneratedImageVariationGenericTypedDict(TypedDict):
    r"""columns and relationships of \"generated_image_variation_generic\" """

    id: NotRequired[Nullable[str]]
    status: NotRequired[shared_job_status.JobStatus]
    r"""The status of the current task."""
    transform_type: NotRequired[shared_variation_type.VariationType]
    r"""The type of variation."""
    url: NotRequired[Nullable[str]]


class GetGenerationsByUserIDGeneratedImageVariationGeneric(BaseModel):
    r"""columns and relationships of \"generated_image_variation_generic\" """

    id: OptionalNullable[str] = UNSET

    status: Optional[shared_job_status.JobStatus] = None
    r"""The status of the current task."""

    transform_type: Annotated[
        Optional[shared_variation_type.VariationType],
        pydantic.Field(alias="transformType"),
    ] = None
    r"""The type of variation."""

    url: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "status", "transformType", "url"]
        nullable_fields = ["id", "url"]
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


class GetGenerationsByUserIDGeneratedImagesTypedDict(TypedDict):
    r"""columns and relationships of \"generated_images\" """

    generated_image_variation_generics: NotRequired[
        List[GetGenerationsByUserIDGeneratedImageVariationGenericTypedDict]
    ]
    id: NotRequired[Nullable[str]]
    image_to_video: NotRequired[Nullable[bool]]
    r"""If it is an image to video generation."""
    like_count: NotRequired[int]
    motion: NotRequired[Nullable[bool]]
    r"""If generation is of motion type."""
    motion_mp4_url: NotRequired[Nullable[str]]
    r"""The URL of the motion MP4."""
    motion_model: NotRequired[Nullable[str]]
    r"""The name of the motion model."""
    motion_strength: NotRequired[Nullable[int]]
    r"""The motion strength."""
    nsfw: NotRequired[bool]
    url: NotRequired[str]


class GetGenerationsByUserIDGeneratedImages(BaseModel):
    r"""columns and relationships of \"generated_images\" """

    generated_image_variation_generics: Optional[
        List[GetGenerationsByUserIDGeneratedImageVariationGeneric]
    ] = None

    id: OptionalNullable[str] = UNSET

    image_to_video: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="imageToVideo")
    ] = UNSET
    r"""If it is an image to video generation."""

    like_count: Annotated[Optional[int], pydantic.Field(alias="likeCount")] = None

    motion: OptionalNullable[bool] = UNSET
    r"""If generation is of motion type."""

    motion_mp4_url: Annotated[
        OptionalNullable[str], pydantic.Field(alias="motionMP4URL")
    ] = UNSET
    r"""The URL of the motion MP4."""

    motion_model: Annotated[
        OptionalNullable[str], pydantic.Field(alias="motionModel")
    ] = UNSET
    r"""The name of the motion model."""

    motion_strength: Annotated[
        OptionalNullable[int], pydantic.Field(alias="motionStrength")
    ] = UNSET
    r"""The motion strength."""

    nsfw: Optional[bool] = None

    url: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "generated_image_variation_generics",
            "id",
            "imageToVideo",
            "likeCount",
            "motion",
            "motionMP4URL",
            "motionModel",
            "motionStrength",
            "nsfw",
            "url",
        ]
        nullable_fields = [
            "id",
            "imageToVideo",
            "motion",
            "motionMP4URL",
            "motionModel",
            "motionStrength",
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


class ElementsTypedDict(TypedDict):
    r"""Element used for the generation."""

    ak_uuid: NotRequired[Nullable[str]]
    r"""Unique identifier for the element. Elements can be found from the List Elements endpoint."""
    base_model: NotRequired[shared_sd_versions.SdVersions]
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
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


class Elements(BaseModel):
    r"""Element used for the generation."""

    ak_uuid: Annotated[OptionalNullable[str], pydantic.Field(alias="akUUID")] = UNSET
    r"""Unique identifier for the element. Elements can be found from the List Elements endpoint."""

    base_model: Annotated[
        Optional[shared_sd_versions.SdVersions], pydantic.Field(alias="baseModel")
    ] = None
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""

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
            "description",
            "name",
            "urlImage",
            "weightDefault",
            "weightMax",
            "weightMin",
        ]
        nullable_fields = [
            "akUUID",
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


class GetGenerationsByUserIDGenerationElementsTypedDict(TypedDict):
    r"""This table captures the elements that are applied to a Generations, also the order and weightings used when applied."""

    id: NotRequired[Nullable[int]]
    lora: NotRequired[Nullable[ElementsTypedDict]]
    r"""Element used for the generation."""
    weight_applied: NotRequired[Nullable[float]]


class GetGenerationsByUserIDGenerationElements(BaseModel):
    r"""This table captures the elements that are applied to a Generations, also the order and weightings used when applied."""

    id: OptionalNullable[int] = UNSET

    lora: OptionalNullable[Elements] = UNSET
    r"""Element used for the generation."""

    weight_applied: Annotated[
        OptionalNullable[float], pydantic.Field(alias="weightApplied")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "lora", "weightApplied"]
        nullable_fields = ["id", "lora", "weightApplied"]
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


class GetGenerationsByUserIDGenerationsTypedDict(TypedDict):
    r"""columns and relationships of \"generations\" """

    created_at: NotRequired[str]
    generated_images: NotRequired[List[GetGenerationsByUserIDGeneratedImagesTypedDict]]
    generation_elements: NotRequired[
        List[GetGenerationsByUserIDGenerationElementsTypedDict]
    ]
    guidance_scale: NotRequired[Nullable[float]]
    id: NotRequired[Nullable[str]]
    image_height: NotRequired[int]
    image_width: NotRequired[int]
    inference_steps: NotRequired[Nullable[int]]
    init_strength: NotRequired[Nullable[float]]
    model_id: NotRequired[Nullable[str]]
    negative_prompt: NotRequired[Nullable[str]]
    photo_real: NotRequired[Nullable[bool]]
    r"""If photoReal feature was used."""
    photo_real_strength: NotRequired[Nullable[float]]
    r"""Depth of field of photoReal used. 0.55 is low, 0.5 is medium, and 0.45 is high. Default is 0.55."""
    preset_style: NotRequired[Nullable[shared_sd_generation_style.SdGenerationStyle]]
    r"""The style to generate images with. When photoReal is enabled, refer to the Guide section for a full list. When alchemy is disabled, use LEONARDO or NONE. When alchemy is enabled, use ANIME, CREATIVE, DYNAMIC, ENVIRONMENT, GENERAL, ILLUSTRATION, PHOTOGRAPHY, RAYTRACED, RENDER_3D, SKETCH_BW, SKETCH_COLOR, or NONE."""
    prompt: NotRequired[str]
    prompt_magic: NotRequired[Nullable[bool]]
    r"""If prompt magic was used."""
    prompt_magic_strength: NotRequired[Nullable[float]]
    r"""Strength of prompt magic used."""
    prompt_magic_version: NotRequired[Nullable[str]]
    r"""Version of prompt magic used."""
    public: NotRequired[bool]
    scheduler: NotRequired[shared_sd_generation_schedulers.SdGenerationSchedulers]
    r"""The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified."""
    sd_version: NotRequired[shared_sd_versions.SdVersions]
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
    seed: NotRequired[Nullable[int]]
    status: NotRequired[shared_job_status.JobStatus]
    r"""The status of the current task."""
    ultra: NotRequired[Nullable[bool]]
    r"""If ultra generation mode was used."""


class GetGenerationsByUserIDGenerations(BaseModel):
    r"""columns and relationships of \"generations\" """

    created_at: Annotated[Optional[str], pydantic.Field(alias="createdAt")] = None

    generated_images: Optional[List[GetGenerationsByUserIDGeneratedImages]] = None

    generation_elements: Optional[List[GetGenerationsByUserIDGenerationElements]] = None

    guidance_scale: Annotated[
        OptionalNullable[float], pydantic.Field(alias="guidanceScale")
    ] = UNSET

    id: OptionalNullable[str] = UNSET

    image_height: Annotated[Optional[int], pydantic.Field(alias="imageHeight")] = None

    image_width: Annotated[Optional[int], pydantic.Field(alias="imageWidth")] = None

    inference_steps: Annotated[
        OptionalNullable[int], pydantic.Field(alias="inferenceSteps")
    ] = UNSET

    init_strength: Annotated[
        OptionalNullable[float], pydantic.Field(alias="initStrength")
    ] = UNSET

    model_id: Annotated[OptionalNullable[str], pydantic.Field(alias="modelId")] = UNSET

    negative_prompt: Annotated[
        OptionalNullable[str], pydantic.Field(alias="negativePrompt")
    ] = UNSET

    photo_real: Annotated[OptionalNullable[bool], pydantic.Field(alias="photoReal")] = (
        UNSET
    )
    r"""If photoReal feature was used."""

    photo_real_strength: Annotated[
        OptionalNullable[float], pydantic.Field(alias="photoRealStrength")
    ] = UNSET
    r"""Depth of field of photoReal used. 0.55 is low, 0.5 is medium, and 0.45 is high. Default is 0.55."""

    preset_style: Annotated[
        OptionalNullable[shared_sd_generation_style.SdGenerationStyle],
        pydantic.Field(alias="presetStyle"),
    ] = shared_sd_generation_style.SdGenerationStyle.DYNAMIC
    r"""The style to generate images with. When photoReal is enabled, refer to the Guide section for a full list. When alchemy is disabled, use LEONARDO or NONE. When alchemy is enabled, use ANIME, CREATIVE, DYNAMIC, ENVIRONMENT, GENERAL, ILLUSTRATION, PHOTOGRAPHY, RAYTRACED, RENDER_3D, SKETCH_BW, SKETCH_COLOR, or NONE."""

    prompt: Optional[str] = None

    prompt_magic: Annotated[
        OptionalNullable[bool], pydantic.Field(alias="promptMagic")
    ] = UNSET
    r"""If prompt magic was used."""

    prompt_magic_strength: Annotated[
        OptionalNullable[float], pydantic.Field(alias="promptMagicStrength")
    ] = UNSET
    r"""Strength of prompt magic used."""

    prompt_magic_version: Annotated[
        OptionalNullable[str], pydantic.Field(alias="promptMagicVersion")
    ] = UNSET
    r"""Version of prompt magic used."""

    public: Optional[bool] = None

    scheduler: Optional[shared_sd_generation_schedulers.SdGenerationSchedulers] = None
    r"""The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified."""

    sd_version: Annotated[
        Optional[shared_sd_versions.SdVersions], pydantic.Field(alias="sdVersion")
    ] = None
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""

    seed: OptionalNullable[int] = UNSET

    status: Optional[shared_job_status.JobStatus] = None
    r"""The status of the current task."""

    ultra: OptionalNullable[bool] = UNSET
    r"""If ultra generation mode was used."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "createdAt",
            "generated_images",
            "generation_elements",
            "guidanceScale",
            "id",
            "imageHeight",
            "imageWidth",
            "inferenceSteps",
            "initStrength",
            "modelId",
            "negativePrompt",
            "photoReal",
            "photoRealStrength",
            "presetStyle",
            "prompt",
            "promptMagic",
            "promptMagicStrength",
            "promptMagicVersion",
            "public",
            "scheduler",
            "sdVersion",
            "seed",
            "status",
            "ultra",
        ]
        nullable_fields = [
            "guidanceScale",
            "id",
            "inferenceSteps",
            "initStrength",
            "modelId",
            "negativePrompt",
            "photoReal",
            "photoRealStrength",
            "presetStyle",
            "promptMagic",
            "promptMagicStrength",
            "promptMagicVersion",
            "seed",
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


class GetGenerationsByUserIDResponseBodyTypedDict(TypedDict):
    r"""Responses for GET /generations/user/{userId}"""

    generations: NotRequired[List[GetGenerationsByUserIDGenerationsTypedDict]]


class GetGenerationsByUserIDResponseBody(BaseModel):
    r"""Responses for GET /generations/user/{userId}"""

    generations: Optional[List[GetGenerationsByUserIDGenerations]] = None


class GetGenerationsByUserIDResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[GetGenerationsByUserIDResponseBodyTypedDict]
    r"""Responses for GET /generations/user/{userId}"""


class GetGenerationsByUserIDResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[GetGenerationsByUserIDResponseBody] = None
    r"""Responses for GET /generations/user/{userId}"""
