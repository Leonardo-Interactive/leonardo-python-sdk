# Leonardo-Ai-SDK

<a href="https://codespaces.new/Leonardo-Interactive/leonardo-python-sdk.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>

<!-- Start Summary [summary] -->
## Summary

Rest Endpoints: Leonardo.Ai API OpenAPI specification.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install LeonardoAiSDK
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add LeonardoAiSDK
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from leonardoaisdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.init_images.delete_init_image_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from leonardoaisdk import LeonardoAiSDK

async def main():
    s = LeonardoAiSDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.init_images.delete_init_image_by_id_async(id="<id>")
    if res.object is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [dataset](docs/sdks/dataset/README.md)

* [create_dataset](docs/sdks/dataset/README.md#create_dataset) - Create a Dataset
* [delete_dataset_by_id](docs/sdks/dataset/README.md#delete_dataset_by_id) - Delete a Single Dataset by ID
* [get_dataset_by_id](docs/sdks/dataset/README.md#get_dataset_by_id) - Get a Single Dataset by ID
* [upload_dataset_image](docs/sdks/dataset/README.md#upload_dataset_image) - Upload dataset image
* [upload_dataset_image_from_gen](docs/sdks/dataset/README.md#upload_dataset_image_from_gen) - Upload a Single Generated Image to a Dataset

### [elements](docs/sdks/elements/README.md)

* [list_elements](docs/sdks/elements/README.md#list_elements) - List Elements

### [image](docs/sdks/image/README.md)

* [create_generation](docs/sdks/image/README.md#create_generation) - Create a Generation of Images
* [delete_generation_by_id](docs/sdks/image/README.md#delete_generation_by_id) - Delete a Single Generation
* [get_generation_by_id](docs/sdks/image/README.md#get_generation_by_id) - Get a Single Generation
* [get_generations_by_user_id](docs/sdks/image/README.md#get_generations_by_user_id) - Get generations by user ID

### [init_images](docs/sdks/initimages/README.md)

* [delete_init_image_by_id](docs/sdks/initimages/README.md#delete_init_image_by_id) - Delete init image
* [get_init_image_by_id](docs/sdks/initimages/README.md#get_init_image_by_id) - Get single init image
* [upload_canvas_init_image](docs/sdks/initimages/README.md#upload_canvas_init_image) - Upload Canvas Editor init and mask image
* [upload_init_image](docs/sdks/initimages/README.md#upload_init_image) - Upload init image


### [models](docs/sdks/models/README.md)

* [create_model](docs/sdks/models/README.md#create_model) - Train a Custom Model
* [delete_model_by_id](docs/sdks/models/README.md#delete_model_by_id) - Delete a Single Custom Model by ID
* [get_model_by_id](docs/sdks/models/README.md#get_model_by_id) - Get a Single Custom Model by ID
* [list_platform_models](docs/sdks/models/README.md#list_platform_models) - List Platform Models

### [motion](docs/sdks/motion/README.md)

* [create_svd_motion_generation](docs/sdks/motion/README.md#create_svd_motion_generation) - Create SVD Motion Generation

### [pricing_calculator](docs/sdks/pricingcalculator/README.md)

* [pricing_calculator](docs/sdks/pricingcalculator/README.md#pricing_calculator) - Calculating API Cost

### [prompt](docs/sdks/prompt/README.md)

* [prompt_improve](docs/sdks/prompt/README.md#prompt_improve) - Improve a Prompt
* [prompt_random](docs/sdks/prompt/README.md#prompt_random) - Generate a Random prompt

### [realtime_canvas](docs/sdks/realtimecanvas/README.md)

* [create_lcm_generation](docs/sdks/realtimecanvas/README.md#create_lcm_generation) - Create LCM Generation
* [perform_alchemy_upscale_lcm](docs/sdks/realtimecanvas/README.md#perform_alchemy_upscale_lcm) - Perform Alchemy Upscale on a LCM image
* [perform_inpainting_lcm](docs/sdks/realtimecanvas/README.md#perform_inpainting_lcm) - Perform inpainting on a LCM image
* [perform_instant_refine](docs/sdks/realtimecanvas/README.md#perform_instant_refine) - Perform instant refine on a LCM image

### [texture](docs/sdks/texture/README.md)

* [create_texture_generation](docs/sdks/texture/README.md#create_texture_generation) - Create Texture Generation
* [delete_texture_generation_by_id](docs/sdks/texture/README.md#delete_texture_generation_by_id) - Delete Texture Generation by ID
* [get_texture_generation_by_id](docs/sdks/texture/README.md#get_texture_generation_by_id) - Get Texture Generation by ID
* [get_texture_generations_by_model_id](docs/sdks/texture/README.md#get_texture_generations_by_model_id) - Get texture generations by 3D Model ID

### [three_d_model_assets](docs/sdks/threedmodelassets/README.md)

* [delete3_d_model_by_id](docs/sdks/threedmodelassets/README.md#delete3_d_model_by_id) - Delete 3D Model by ID
* [get3_d_model_by_id](docs/sdks/threedmodelassets/README.md#get3_d_model_by_id) - Get 3D Model by ID
* [get3_d_models_by_user_id](docs/sdks/threedmodelassets/README.md#get3_d_models_by_user_id) - Get 3D models by user ID
* [upload_model_asset](docs/sdks/threedmodelassets/README.md#upload_model_asset) - Upload 3D Model

### [user](docs/sdks/user/README.md)

* [get_user_self](docs/sdks/user/README.md#get_user_self) - Get user information

### [variation](docs/sdks/variation/README.md)

* [create_universal_upscaler_job](docs/sdks/variation/README.md#create_universal_upscaler_job) - Create using Universal Upscaler
* [create_variation_no_bg](docs/sdks/variation/README.md#create_variation_no_bg) - Create no background
* [create_variation_unzoom](docs/sdks/variation/README.md#create_variation_unzoom) - Create unzoom
* [create_variation_upscale](docs/sdks/variation/README.md#create_variation_upscale) - Create upscale
* [get_variation_by_id](docs/sdks/variation/README.md#get_variation_by_id) - Get variation by ID

</details>
<!-- End Available Resources and Operations [operations] -->







<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from leonardoaisdk import LeonardoAiSDK
from leonardoaisdk.utils import BackoffStrategy, RetryConfig

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.init_images.delete_init_image_by_id(id="<id>",
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res.object is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from leonardoaisdk import LeonardoAiSDK
from leonardoaisdk.utils import BackoffStrategy, RetryConfig

s = LeonardoAiSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.init_images.delete_init_image_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
from leonardoaisdk import LeonardoAiSDK
from leonardoaisdk.models import errors

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.init_images.delete_init_image_by_id(id="<id>")

    if res.object is not None:
        # handle response
        pass

except errors.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from leonardoaisdk import LeonardoAiSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = LeonardoAiSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from leonardoaisdk import LeonardoAiSDK
from leonardoaisdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = LeonardoAiSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://cloud.leonardo.ai/api/rest/v1` | None |

#### Example

```python
from leonardoaisdk import LeonardoAiSDK

s = LeonardoAiSDK(
    server_idx=0,
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.init_images.delete_init_image_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from leonardoaisdk import LeonardoAiSDK

s = LeonardoAiSDK(
    server_url="https://cloud.leonardo.ai/api/rest/v1",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.init_images.delete_init_image_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from leonardoaisdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.init_images.delete_init_image_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from leonardoaisdk import LeonardoAiSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = LeonardoAiSDK(debug_logger=logging.getLogger("leonardoaisdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
