"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from leonardo_ai_sdk.models.shared import (
    custom_model_type as shared_custom_model_type,
    sd_versions as shared_sd_versions,
    strength as shared_strength,
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


class CreateModelRequestBodyTypedDict(TypedDict):
    r"""Query parameters to be provided in the request body as a JSON object"""

    dataset_id: str
    r"""The ID of the dataset to train the model on."""
    instance_prompt: str
    r"""The instance prompt to use during training."""
    name: str
    r"""The name of the model."""
    description: NotRequired[Nullable[str]]
    r"""The description of the model."""
    model_type: NotRequired[shared_custom_model_type.CustomModelType]
    r"""The category the most accurately reflects the model."""
    nsfw: NotRequired[Nullable[bool]]
    r"""Whether or not the model is NSFW."""
    resolution: NotRequired[Nullable[int]]
    r"""The resolution for training. Must be 512 or 768."""
    sd_version: NotRequired[shared_sd_versions.SdVersions]
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
    strength: NotRequired[shared_strength.Strength]
    r"""When training using the PIXEL_ART model type, this influences the training strength."""


class CreateModelRequestBody(BaseModel):
    r"""Query parameters to be provided in the request body as a JSON object"""

    dataset_id: Annotated[str, pydantic.Field(alias="datasetId")]
    r"""The ID of the dataset to train the model on."""

    instance_prompt: str
    r"""The instance prompt to use during training."""

    name: str
    r"""The name of the model."""

    description: OptionalNullable[str] = ""
    r"""The description of the model."""

    model_type: Annotated[
        Optional[shared_custom_model_type.CustomModelType],
        pydantic.Field(alias="modelType"),
    ] = shared_custom_model_type.CustomModelType.GENERAL
    r"""The category the most accurately reflects the model."""

    nsfw: OptionalNullable[bool] = False
    r"""Whether or not the model is NSFW."""

    resolution: OptionalNullable[int] = 512
    r"""The resolution for training. Must be 512 or 768."""

    sd_version: Annotated[
        Optional[shared_sd_versions.SdVersions], pydantic.Field(alias="sd_Version")
    ] = None
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""

    strength: Optional[shared_strength.Strength] = shared_strength.Strength.MEDIUM
    r"""When training using the PIXEL_ART model type, this influences the training strength."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "modelType",
            "nsfw",
            "resolution",
            "sd_Version",
            "strength",
        ]
        nullable_fields = ["description", "nsfw", "resolution"]
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


class SDTrainingOutputTypedDict(TypedDict):
    api_credit_cost: NotRequired[Nullable[int]]
    r"""API Credits Cost for Model Training. Available for Production API Users."""
    custom_model_id: NotRequired[str]


class SDTrainingOutput(BaseModel):
    api_credit_cost: Annotated[
        OptionalNullable[int], pydantic.Field(alias="apiCreditCost")
    ] = UNSET
    r"""API Credits Cost for Model Training. Available for Production API Users."""

    custom_model_id: Annotated[Optional[str], pydantic.Field(alias="customModelId")] = (
        None
    )

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["apiCreditCost", "customModelId"]
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


class CreateModelResponseBodyTypedDict(TypedDict):
    r"""Responses for POST /models"""

    sd_training_job: NotRequired[Nullable[SDTrainingOutputTypedDict]]


class CreateModelResponseBody(BaseModel):
    r"""Responses for POST /models"""

    sd_training_job: Annotated[
        OptionalNullable[SDTrainingOutput], pydantic.Field(alias="sdTrainingJob")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["sdTrainingJob"]
        nullable_fields = ["sdTrainingJob"]
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


class CreateModelResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: NotRequired[CreateModelResponseBodyTypedDict]
    r"""Responses for POST /models"""


class CreateModelResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    object: Optional[CreateModelResponseBody] = None
    r"""Responses for POST /models"""
