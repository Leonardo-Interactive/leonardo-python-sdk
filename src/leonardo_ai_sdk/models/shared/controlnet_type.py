"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing_extensions import deprecated


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class ControlnetType(str, Enum):
    r"""This parameter will be deprecated in September 2024. Please use the controlnets array instead."""

    POSE = "POSE"
    CANNY = "CANNY"
    DEPTH = "DEPTH"
