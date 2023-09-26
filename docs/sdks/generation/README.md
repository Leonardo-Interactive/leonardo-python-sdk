# Generation

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
    contrast_ratio=5680.45,
    control_net=False,
    control_net_type=shared.ControlnetType.CANNY,
    expanded_domain=False,
    guidance_scale=925597,
    height=836079,
    high_contrast=False,
    high_resolution=False,
    image_prompt_weight=710.36,
    image_prompts=[
        'quis',
    ],
    init_generation_image_id='veritatis',
    init_image_id='deserunt',
    init_strength=202.18,
    model_id='ipsam',
    negative_prompt='repellendus',
    nsfw=False,
    num_images=957156,
    num_inference_steps=778157,
    photo_real=False,
    preset_style=shared.SdGenerationStyle.LEONARDO,
    prompt='at',
    prompt_magic=False,
    prompt_magic_version='at',
    public=False,
    scheduler=shared.SdGenerationSchedulers.PNDM,
    sd_version=shared.SdVersions.V1_5,
    seed=799159,
    tiling=False,
    unzoom=False,
    unzoom_amount=8009.11,
    upscale_ratio=4614.79,
    weighting=5204.78,
    width=780529,
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


res = s.generation.delete_generation_by_id(id='dolorum')

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


res = s.generation.delete_generations_texture_id_(id='dicta', request_body=operations.DeleteGenerationsTextureIDRequestBody(
    id='ba928fc8-1674-42cb-b392-05929396fea7',
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


res = s.generation.get_generation_by_id(id='corporis')

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


res = s.generation.get_generations_by_user_id(user_id='iste', limit=437032, offset=902349)

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


res = s.generation.get_generations_texture_model_model_id_(model_id='quidem', request_body=operations.GetGenerationsTextureModelModelIDRequestBody(
    limit=99280,
    model_id='ipsa',
    offset=969810,
), limit=666767, offset=653140)

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


res = s.generation.get_generations_texture_id_(id='laborum', request_body=operations.GetGenerationsTextureIDRequestBody(
    id='2352c595-5907-4aff-9a3a-2fa946773925',
), limit=110375, offset=674752)

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
    front_rotation_offset=656330,
    model_asset_id='enim',
    negative_prompt='odit',
    preview=False,
    preview_direction='quo',
    prompt='sequi',
    sd_version='tenetur',
    seed=368725,
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

