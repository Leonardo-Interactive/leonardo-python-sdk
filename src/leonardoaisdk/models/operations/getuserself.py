"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Users:
    r"""columns and relationships of \\"users\\" """
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is Users.UNSET }})
    username: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is Users.UNSET }})
    r"""Username of the user."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserDetails:
    r"""columns and relationships of \\"user_details\\" """
    UNSET='__SPEAKEASY_UNSET__'
    api_concurrency_slots: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiConcurrencySlots'), 'exclude': lambda f: f is None }})
    r"""API Concurrency Slots."""
    api_paid_tokens: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiPaidTokens'), 'exclude': lambda f: f is UserDetails.UNSET }})
    r"""Current balance of API paid tokens the user has."""
    api_plan_token_renewal_date: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiPlanTokenRenewalDate'), 'exclude': lambda f: f is UserDetails.UNSET }})
    r"""API Plan Token Renewal Date."""
    api_subscription_tokens: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiSubscriptionTokens'), 'exclude': lambda f: f is None }})
    r"""Current balance of Enterprise API subscriptions tokens the user has."""
    paid_tokens: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidTokens'), 'exclude': lambda f: f is UserDetails.UNSET }})
    r"""Current balance of paid tokens the user has."""
    subscription_gpt_tokens: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptionGptTokens'), 'exclude': lambda f: f is None }})
    r"""Current balance of user plan GPT tokens the user has."""
    subscription_model_tokens: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptionModelTokens'), 'exclude': lambda f: f is None }})
    r"""Current balance of model training tokens the user has."""
    subscription_tokens: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptionTokens'), 'exclude': lambda f: f is None }})
    r"""Current balance of user plan subscription tokens the user has."""
    token_renewal_date: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tokenRenewalDate'), 'exclude': lambda f: f is UserDetails.UNSET }})
    r"""User Plan Token Renewal Date."""
    user: Optional[Users] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is UserDetails.UNSET }})
    r"""columns and relationships of \\"users\\" """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserSelfResponseBody:
    r"""Responses for GET /me"""
    user_details: Optional[List[UserDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_details'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetUserSelfResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetUserSelfResponseBody] = dataclasses.field(default=None)
    r"""Responses for GET /me"""
    

