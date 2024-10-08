"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class SdGenerationSchedulers(str, Enum):
    r"""The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified."""

    KLMS = "KLMS"
    EULER_ANCESTRAL_DISCRETE = "EULER_ANCESTRAL_DISCRETE"
    EULER_DISCRETE = "EULER_DISCRETE"
    DDIM = "DDIM"
    DPM_SOLVER = "DPM_SOLVER"
    PNDM = "PNDM"
    LEONARDO = "LEONARDO"
