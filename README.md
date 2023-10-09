# Leonardo-Ai-SDK

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install Leonardo-Ai-SDK
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateDatasetRequestBody(
    name='Forward South uselessly',
)

res = s.dataset.create_dataset(req)

if res.create_dataset_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [dataset](docs/sdks/dataset/README.md)

* [create_dataset](docs/sdks/dataset/README.md#create_dataset) - Create a Dataset
* [delete_dataset_by_id](docs/sdks/dataset/README.md#delete_dataset_by_id) - Delete a Single Dataset by ID
* [get_dataset_by_id](docs/sdks/dataset/README.md#get_dataset_by_id) - Get a Single Dataset by ID
* [upload_dataset_image](docs/sdks/dataset/README.md#upload_dataset_image) - Upload dataset image
* [upload_dataset_image_from_gen](docs/sdks/dataset/README.md#upload_dataset_image_from_gen) - Upload a Single Generated Image to a Dataset

### [generation](docs/sdks/generation/README.md)

* [create_generation](docs/sdks/generation/README.md#create_generation) - Create a Generation of Images
* [delete_generation_by_id](docs/sdks/generation/README.md#delete_generation_by_id) - Delete a Single Generation
* [delete_generations_texture_id_](docs/sdks/generation/README.md#delete_generations_texture_id_) - Delete Texture Generation by ID
* [get_generation_by_id](docs/sdks/generation/README.md#get_generation_by_id) - Get a Single Generation
* [get_generations_by_user_id](docs/sdks/generation/README.md#get_generations_by_user_id) - Get generations by user ID
* [get_generations_texture_model_model_id_](docs/sdks/generation/README.md#get_generations_texture_model_model_id_) - Get texture generations by 3D Model ID
* [get_generations_texture_id_](docs/sdks/generation/README.md#get_generations_texture_id_) - Get Texture Generation by ID
* [post_generations_texture](docs/sdks/generation/README.md#post_generations_texture) - Create Texture Generation

### [init_image](docs/sdks/initimage/README.md)

* [delete_init_image_by_id](docs/sdks/initimage/README.md#delete_init_image_by_id) - Delete init image
* [get_init_image_by_id](docs/sdks/initimage/README.md#get_init_image_by_id) - Get single init image
* [upload_init_image](docs/sdks/initimage/README.md#upload_init_image) - Upload init image

### [model](docs/sdks/model/README.md)

* [create_model](docs/sdks/model/README.md#create_model) - Train a Custom Model
* [delete_model_by_id](docs/sdks/model/README.md#delete_model_by_id) - Delete a Single Custom Model by ID
* [delete_models_3d_id_](docs/sdks/model/README.md#delete_models_3d_id_) - Delete 3D Model by ID
* [get_model_by_id](docs/sdks/model/README.md#get_model_by_id) - Get a Single Custom Model by ID
* [get_models_3d_user_user_id_](docs/sdks/model/README.md#get_models_3d_user_user_id_) - Get 3D models by user ID
* [get_models_3d_id_](docs/sdks/model/README.md#get_models_3d_id_) - Get 3D Model by ID
* [get_platform_models](docs/sdks/model/README.md#get_platform_models) - List Platform Models
* [post_models_3d_upload](docs/sdks/model/README.md#post_models_3d_upload) - Upload 3D Model

### [user](docs/sdks/user/README.md)

* [get_user_self](docs/sdks/user/README.md#get_user_self) - Get user information

### [variation](docs/sdks/variation/README.md)

* [create_variation_upscale](docs/sdks/variation/README.md#create_variation_upscale) - Create upscale
* [get_variation_by_id](docs/sdks/variation/README.md#get_variation_by_id) - Get variation by ID
* [post_variations_unzoom](docs/sdks/variation/README.md#post_variations_unzoom) - Create unzoom
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->
# Dev Containers
<div align="left">
    <a href="https://codespaces.new/Leonardo-Interactive/leonardo-python-sdk.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>
    
</div>

Experience our SDK in an enhanced sandbox environment. Try it now in **GitHub Codespaces**!

* [Explore Dev Containers](.devcontainer/README.md)
<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
