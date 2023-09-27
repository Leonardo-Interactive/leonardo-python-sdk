# Model
(*model*)

### Available Operations

* [create_model](#create_model) - Train a Custom Model
* [delete_model_by_id](#delete_model_by_id) - Delete a Single Custom Model by ID
* [delete_models_3d_id_](#delete_models_3d_id_) - Delete 3D Model by ID
* [get_model_by_id](#get_model_by_id) - Get a Single Custom Model by ID
* [get_models_3d_user_user_id_](#get_models_3d_user_user_id_) - Get 3D models by user ID
* [get_models_3d_id_](#get_models_3d_id_) - Get 3D Model by ID
* [get_platform_models](#get_platform_models) - List Platform Models
* [post_models_3d_upload](#post_models_3d_upload) - Upload 3D Model

## create_model

This endpoint will train a new custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateModelRequestBody(
    dataset_id='quasi',
    description='error',
    instance_prompt='temporibus',
    model_type=shared.CustomModelType.PIXEL_ART,
    name='Johanna Wolf',
    nsfw=False,
    resolution=509624,
    sd_version=shared.SdVersions.V2,
    strength=shared.Strength.VERY_LOW,
)

res = s.model.create_model(req)

if res.create_model_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateModelRequestBody](../../models/operations/createmodelrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**


## delete_model_by_id

This endpoint will delete a specific custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.model.delete_model_by_id(id='omnis')

if res.delete_model_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `id`                           | *str*                          | :heavy_check_mark:             | The ID of the model to delete. |


### Response

**[operations.DeleteModelByIDResponse](../../models/operations/deletemodelbyidresponse.md)**


## delete_models_3d_id_

This endpoint deletes the specific 3D Model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.model.delete_models_3d_id_(id='voluptate', request_body=operations.DeleteModels3dIDRequestBody(
    id='b0074f15-471b-45e6-a13b-99d488e1e91e',
))

if res.delete_models_3d_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | _"id" is required (enter it either in parameters or request body)_                                         |
| `request_body`                                                                                             | [Optional[operations.DeleteModels3dIDRequestBody]](../../models/operations/deletemodels3didrequestbody.md) | :heavy_minus_sign:                                                                                         | Query parameters can also be provided in the request body as a JSON object                                 |


### Response

**[operations.DeleteModels3dIDResponse](../../models/operations/deletemodels3didresponse.md)**


## get_model_by_id

This endpoint gets the specific custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.model.get_model_by_id(id='incidunt')

if res.get_model_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `id`                                  | *str*                                 | :heavy_check_mark:                    | The ID of the custom model to return. |


### Response

**[operations.GetModelByIDResponse](../../models/operations/getmodelbyidresponse.md)**


## get_models_3d_user_user_id_

This endpoint returns all 3D models by a specific user

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.model.get_models_3d_user_user_id_(user_id='enim', request_body=operations.GetModels3dUserUserIDRequestBody(
    user_id='consequatur',
), limit=667411, offset=842342)

if res.get_models_3d_user_user_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                            | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |
| `request_body`                                                                                                       | [Optional[operations.GetModels3dUserUserIDRequestBody]](../../models/operations/getmodels3duseruseridrequestbody.md) | :heavy_minus_sign:                                                                                                   | Query parameters can also be provided in the request body as a JSON object                                           |
| `limit`                                                                                                              | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `offset`                                                                                                             | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |


### Response

**[operations.GetModels3dUserUserIDResponse](../../models/operations/getmodels3duseruseridresponse.md)**


## get_models_3d_id_

This endpoint gets the specific 3D model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.model.get_models_3d_id_(id='explicabo', request_body=operations.GetModels3dIDRequestBody(
    id='abd44269-802d-4502-a94b-b4f63c969e9a',
), limit=223081, offset=891555)

if res.get_models_3d_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | _"id" is required (enter it either in parameters or request body)_                                   |
| `request_body`                                                                                       | [Optional[operations.GetModels3dIDRequestBody]](../../models/operations/getmodels3didrequestbody.md) | :heavy_minus_sign:                                                                                   | Query parameters can also be provided in the request body as a JSON object                           |
| `limit`                                                                                              | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `offset`                                                                                             | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |


### Response

**[operations.GetModels3dIDResponse](../../models/operations/getmodels3didresponse.md)**


## get_platform_models

Get a list of public Platform Models available for use with generations.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.model.get_platform_models(limit=952749, offset=680056)

if res.get_platform_models_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `offset`           | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetPlatformModelsResponse](../../models/operations/getplatformmodelsresponse.md)**


## post_models_3d_upload

This endpoint returns presigned details to upload a 3D model to S3

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostModels3dUploadRequestBody(
    model_extension='in',
    name='Angel Wolff II',
)

res = s.model.post_models_3d_upload(req)

if res.post_models_3d_upload_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PostModels3dUploadRequestBody](../../models/operations/postmodels3duploadrequestbody.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PostModels3dUploadResponse](../../models/operations/postmodels3duploadresponse.md)**

