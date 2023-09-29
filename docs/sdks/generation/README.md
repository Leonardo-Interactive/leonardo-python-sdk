# Generation
(*generation*)

### Available Operations

* [create_generation](#create_generation) - Create a Generation of Images
* [delete_generation_by_id](#delete_generation_by_id) - Delete a Single Generation
* [delete_generations_texture_id_](#delete_generations_texture_id_) - Delete Texture Generation by ID
* [get_generation_by_id](#get_generation_by_id) - Get a Single Generation
* [get_generations_by_user_id](#get_generations_by_user_id) - Get generations by user ID
* [get_generations_texture_model_model_id_](#get_generations_texture_model_model_id_) - Get texture generations by 3D Model ID
* [get_generations_texture_id_](#get_generations_texture_id_) - Get Texture Generation by ID
* [post_generations_texture](#post_generations_texture) - Create Texture Generation

## create_generation

This endpoint will generate images

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateGenerationRequestBody(
    alchemy=False,
    contrast_ratio=4444.14,
    control_net=False,
    control_net_type=shared.ControlnetType.CANNY,
    expanded_domain=False,
    guidance_scale=784343,
    height=244808,
    high_contrast=False,
    high_resolution=False,
    image_prompt_weight=2793,
    image_prompts=[
        'Product',
    ],
    init_generation_image_id='actuating DNS',
    init_image_id='salmon wireless rarely',
    init_strength=1502.38,
    model_id='emulation Country',
    negative_prompt='Kentucky MTF',
    nsfw=False,
    num_images=649224,
    num_inference_steps=895539,
    photo_real=False,
    preset_style=shared.SdGenerationStyle.LEONARDO,
    prompt='aggregate',
    prompt_magic=False,
    prompt_magic_version='visionary which',
    public=False,
    scheduler=shared.SdGenerationSchedulers.DDIM,
    sd_version=shared.SdVersions.V2,
    seed=262328,
    tiling=False,
    unzoom=False,
    unzoom_amount=371.25,
    upscale_ratio=485.82,
    weighting=9968.92,
    width=152007,
)

res = s.generation.create_generation(req)

if res.create_generation_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateGenerationRequestBody](../../models/operations/creategenerationrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateGenerationResponse](../../models/operations/creategenerationresponse.md)**


## delete_generation_by_id

This endpoint deletes a specific generation

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.generation.delete_generation_by_id(id='Sports')

if res.delete_generation_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `id`                                | *str*                               | :heavy_check_mark:                  | The ID of the generation to delete. |


### Response

**[operations.DeleteGenerationByIDResponse](../../models/operations/deletegenerationbyidresponse.md)**


## delete_generations_texture_id_

This endpoint deletes the specific texture generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.generation.delete_generations_texture_id_(id='Lodge', request_body=operations.DeleteGenerationsTextureIDRequestBody(
    id='<ID>',
))

if res.delete_generations_texture_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                           | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | _"id" is required (enter it either in parameters or request body)_                                                             |
| `request_body`                                                                                                                 | [Optional[operations.DeleteGenerationsTextureIDRequestBody]](../../models/operations/deletegenerationstextureidrequestbody.md) | :heavy_minus_sign:                                                                                                             | Query parameters can also be provided in the request body as a JSON object                                                     |


### Response

**[operations.DeleteGenerationsTextureIDResponse](../../models/operations/deletegenerationstextureidresponse.md)**


## get_generation_by_id

This endpoint will provide information about a specific generation

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.generation.get_generation_by_id(id='male')

if res.get_generation_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `id`                                | *str*                               | :heavy_check_mark:                  | The ID of the generation to return. |


### Response

**[operations.GetGenerationByIDResponse](../../models/operations/getgenerationbyidresponse.md)**


## get_generations_by_user_id

This endpoint returns all generations by a specific user

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.generation.get_generations_by_user_id(user_id='Oriental', limit=135536, offset=934375)

if res.get_generations_by_user_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `offset`           | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetGenerationsByUserIDResponse](../../models/operations/getgenerationsbyuseridresponse.md)**


## get_generations_texture_model_model_id_

This endpoint gets the specific texture generations by the 3d model id.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.generation.get_generations_texture_model_model_id_(model_id='Bacon', request_body=operations.GetGenerationsTextureModelModelIDRequestBody(
    limit=556694,
    model_id='Diesel',
    offset=607383,
), limit=964860, offset=205602)

if res.get_generations_texture_model_model_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `model_id`                                                                                                                                   | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | _"modelId" is required (enter it either in parameters or request body)_                                                                      |
| `request_body`                                                                                                                               | [Optional[operations.GetGenerationsTextureModelModelIDRequestBody]](../../models/operations/getgenerationstexturemodelmodelidrequestbody.md) | :heavy_minus_sign:                                                                                                                           | Query parameters can also be provided in the request body as a JSON object                                                                   |
| `limit`                                                                                                                                      | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | N/A                                                                                                                                          |
| `offset`                                                                                                                                     | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | N/A                                                                                                                                          |


### Response

**[operations.GetGenerationsTextureModelModelIDResponse](../../models/operations/getgenerationstexturemodelmodelidresponse.md)**


## get_generations_texture_id_

This endpoint gets the specific texture generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.generation.get_generations_texture_id_(id='Cisgender', request_body=operations.GetGenerationsTextureIDRequestBody(
    id='<ID>',
), limit=783489, offset=654442)

if res.get_generations_texture_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                     | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | _"id" is required (enter it either in parameters or request body)_                                                       |
| `request_body`                                                                                                           | [Optional[operations.GetGenerationsTextureIDRequestBody]](../../models/operations/getgenerationstextureidrequestbody.md) | :heavy_minus_sign:                                                                                                       | Query parameters can also be provided in the request body as a JSON object                                               |
| `limit`                                                                                                                  | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |
| `offset`                                                                                                                 | *Optional[int]*                                                                                                          | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |


### Response

**[operations.GetGenerationsTextureIDResponse](../../models/operations/getgenerationstextureidresponse.md)**


## post_generations_texture

This endpoint will generate a texture generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostGenerationsTextureRequestBody(
    front_rotation_offset=854632,
    model_asset_id='West',
    negative_prompt='quantifying pink ah',
    preview=False,
    preview_direction='Auto',
    prompt='Coupe North Steel',
    sd_version='Market parsing inasmuch',
    seed=895868,
)

res = s.generation.post_generations_texture(req)

if res.post_generations_texture_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostGenerationsTextureRequestBody](../../models/operations/postgenerationstexturerequestbody.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostGenerationsTextureResponse](../../models/operations/postgenerationstextureresponse.md)**

