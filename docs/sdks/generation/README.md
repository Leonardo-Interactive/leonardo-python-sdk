# generation

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
    contrast_ratio=3834.41,
    control_net=False,
    control_net_type=shared.ControlnetType.CANNY,
    expanded_domain=False,
    guidance_scale=791725,
    height=812169,
    high_contrast=False,
    high_resolution=False,
    image_prompt_weight=5288.95,
    image_prompts=[
        'excepturi',
        'nisi',
    ],
    init_generation_image_id='recusandae',
    init_image_id='temporibus',
    init_strength=710.36,
    model_id='quis',
    negative_prompt='veritatis',
    nsfw=False,
    num_images=648172,
    num_inference_steps=20218,
    preset_style=shared.SdGenerationStyle.LEONARDO,
    prompt='repellendus',
    prompt_magic=False,
    prompt_magic_version='sapiente',
    public=False,
    scheduler=shared.SdGenerationSchedulers.DPM_SOLVER,
    sd_version=shared.SdVersions.V1_5,
    seed=870013,
    tiling=False,
    unzoom=False,
    unzoom_amount=8700.88,
    upscale_ratio=9786.19,
    weighting=4736.08,
    width=799159,
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


res = s.generation.delete_generation_by_id(id='quod')

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


res = s.generation.delete_generations_texture_id_(id='esse', request_body=operations.DeleteGenerationsTextureIDRequestBody(
    id='8ca1ba92-8fc8-4167-82cb-739205929396',
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


res = s.generation.get_generation_by_id(id='hic')

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


res = s.generation.get_generations_by_user_id(user_id='saepe', limit=681820, offset=449950)

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


res = s.generation.get_generations_texture_model_model_id_(model_id='corporis', request_body=operations.GetGenerationsTextureModelModelIDRequestBody(
    limit=613064,
    model_id='iure',
    offset=902349,
), limit=697631, offset=99280)

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


res = s.generation.get_generations_texture_id_(id='ipsa', request_body=operations.GetGenerationsTextureIDRequestBody(
    id='faaa2352-c595-4590-baff-1a3a2fa94677',
), limit=244425, offset=623510)

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
    front_rotation_offset=158969,
    model_asset_id='quis',
    negative_prompt='vitae',
    preview=False,
    preview_direction='laborum',
    prompt='animi',
    sd_version='enim',
    seed=138183,
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

