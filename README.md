# Leonardo-Ai-SDK

<a href="https://codespaces.new/Leonardo-Interactive/leonardo-python-sdk.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install Leonardo-Ai-SDK
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.init_images.delete_init_image_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [init_images](docs/sdks/initimages/README.md)

* [delete_init_image_by_id](docs/sdks/initimages/README.md#delete_init_image_by_id) - Delete init image
* [get_init_image_by_id](docs/sdks/initimages/README.md#get_init_image_by_id) - Get single init image
* [upload_canvas_init_image](docs/sdks/initimages/README.md#upload_canvas_init_image) - Upload Canvas Editor init and mask image
* [upload_init_image](docs/sdks/initimages/README.md#upload_init_image) - Upload init image

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

### [realtime_canvas](docs/sdks/realtimecanvas/README.md)

* [create_lcm_generation](docs/sdks/realtimecanvas/README.md#create_lcm_generation) - Create LCM Generation
* [perform_alchemy_upscale_lcm](docs/sdks/realtimecanvas/README.md#perform_alchemy_upscale_lcm) - Perform Alchemy Upscale on a LCM image
* [perform_inpainting_lcm](docs/sdks/realtimecanvas/README.md#perform_inpainting_lcm) - Perform inpainting on a LCM image
* [perform_instant_refine](docs/sdks/realtimecanvas/README.md#perform_instant_refine) - Perform instant refine on a LCM image

### [motion](docs/sdks/motion/README.md)

* [create_svd_motion_generation](docs/sdks/motion/README.md#create_svd_motion_generation) - Create SVD Motion Generation

### [texture](docs/sdks/texture/README.md)

* [create_texture_generation](docs/sdks/texture/README.md#create_texture_generation) - Create Texture Generation
* [delete_texture_generation_by_id](docs/sdks/texture/README.md#delete_texture_generation_by_id) - Delete Texture Generation by ID
* [get_texture_generation_by_id](docs/sdks/texture/README.md#get_texture_generation_by_id) - Get Texture Generation by ID
* [get_texture_generations_by_model_id](docs/sdks/texture/README.md#get_texture_generations_by_model_id) - Get texture generations by 3D Model ID

### [user](docs/sdks/user/README.md)

* [get_user_self](docs/sdks/user/README.md#get_user_self) - Get user information

### [models](docs/sdks/models/README.md)

* [create_model](docs/sdks/models/README.md#create_model) - Train a Custom Model
* [delete_model_by_id](docs/sdks/models/README.md#delete_model_by_id) - Delete a Single Custom Model by ID
* [get_model_by_id](docs/sdks/models/README.md#get_model_by_id) - Get a Single Custom Model by ID
* [list_platform_models](docs/sdks/models/README.md#list_platform_models) - List Platform Models

### [three_d_model_assets](docs/sdks/threedmodelassets/README.md)

* [delete3_d_model_by_id](docs/sdks/threedmodelassets/README.md#delete3_d_model_by_id) - Delete 3D Model by ID
* [get3_d_model_by_id](docs/sdks/threedmodelassets/README.md#get3_d_model_by_id) - Get 3D Model by ID
* [get3_d_models_by_user_id](docs/sdks/threedmodelassets/README.md#get3_d_models_by_user_id) - Get 3D models by user ID
* [upload_model_asset](docs/sdks/threedmodelassets/README.md#upload_model_asset) - Upload 3D Model

### [pricing_calculator](docs/sdks/pricingcalculator/README.md)

* [pricing_calculator](docs/sdks/pricingcalculator/README.md#pricing_calculator) - Calculating API Cost

### [prompt](docs/sdks/prompt/README.md)

* [prompt_improve](docs/sdks/prompt/README.md#prompt_improve) - Improve a Prompt
* [prompt_random](docs/sdks/prompt/README.md#prompt_random) - Generate a Random prompt

### [variation](docs/sdks/variation/README.md)

* [create_universal_upscaler_job](docs/sdks/variation/README.md#create_universal_upscaler_job) - Create using Universal Upscaler
* [create_variation_no_bg](docs/sdks/variation/README.md#create_variation_no_bg) - Create no background
* [create_variation_unzoom](docs/sdks/variation/README.md#create_variation_unzoom) - Create unzoom
* [create_variation_upscale](docs/sdks/variation/README.md#create_variation_upscale) - Create upscale
* [get_variation_by_id](docs/sdks/variation/README.md#get_variation_by_id) - Get variation by ID
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import leonardoaisdk
from leonardoaisdk.models import errors

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.init_images.delete_init_image_by_id(id='<value>')

except errors.SDKError as e:
    # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import leonardoaisdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = leonardoaisdk.LeonardoAiSDK(client=http_client)
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
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    server_idx=0,
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.init_images.delete_init_image_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    server_url="https://cloud.leonardo.ai/api/rest/v1",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.init_images.delete_init_image_by_id(id='<value>')

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
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.init_images.delete_init_image_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
