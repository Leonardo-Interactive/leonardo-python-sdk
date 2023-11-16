"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ControlnetType(str, Enum):
    r"""The type of ControlNet to use."""
    POSE = 'POSE'
    CANNY = 'CANNY'
    DEPTH = 'DEPTH'
