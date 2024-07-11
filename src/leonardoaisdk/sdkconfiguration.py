"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from leonardoaisdk.models import shared
from typing import Callable, Dict, Optional, Tuple, Union


SERVERS = [
    'https://cloud.leonardo.ai/api/rest/v1',
    # Leonardo.Ai API server
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: Optional[str] = ''
    server_idx: Optional[int] = 0
    language: str = 'python'
    openapi_doc_version: str = 'v1.0.0'
    sdk_version: str = '5.6.1'
    gen_version: str = '2.365.0'
    user_agent: str = 'speakeasy-sdk/python 5.6.1 2.365.0 v1.0.0 Leonardo-Ai-SDK'
    retry_config: Optional[RetryConfig] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url != '':
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}


    def get_hooks(self) -> SDKHooks:
        return self._hooks
