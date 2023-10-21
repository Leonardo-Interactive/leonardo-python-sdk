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
    bearer_auth="",
)

req = operations.CreateGenerationRequestBody(
    elements=[
        shared.ElementInput(),
    ],
    image_prompts=[
        'string',
    ],
)

res = s.generation.create_generation(req)

if res.create_generation_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.generation.delete_generation_by_id(id='string')

if res.delete_generation_by_id_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.generation.delete_generations_texture_id_(id='string', request_body=operations.DeleteGenerationsTextureIDRequestBody())

if res.delete_generations_texture_id_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.generation.get_generation_by_id(id='string')

if res.get_generation_by_id_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.generation.get_generations_by_user_id(user_id='string', limit=270501, offset=770121)

if res.get_generations_by_user_id_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.generation.get_generations_texture_model_model_id_(model_id='string', request_body=operations.GetGenerationsTextureModelModelIDRequestBody(), limit=216504, offset=808783)

if res.get_generations_texture_model_model_id_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)


res = s.generation.get_generations_texture_id_(id='string', request_body=operations.GetGenerationsTextureIDRequestBody(), limit=608876, offset=119347)

if res.get_generations_texture_id_200_application_json_object is not None:
    # handle response
    pass
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
    bearer_auth="",
)

req = operations.PostGenerationsTextureRequestBody()

res = s.generation.post_generations_texture(req)

if res.post_generations_texture_200_application_json_object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostGenerationsTextureRequestBody](../../models/operations/postgenerationstexturerequestbody.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostGenerationsTextureResponse](../../models/operations/postgenerationstextureresponse.md)**

