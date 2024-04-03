# Model
(*model*)

### Available Operations

* [create_model](#create_model) - Train a Custom Model
* [delete3_d_model_by_id](#delete3_d_model_by_id) - Delete 3D Model by ID
* [delete_model_by_id](#delete_model_by_id) - Delete a Single Custom Model by ID
* [get3_d_model_by_id](#get3_d_model_by_id) - Get 3D Model by ID
* [get3_d_models_by_user_id](#get3_d_models_by_user_id) - Get 3D models by user ID
* [get_model_by_id](#get_model_by_id) - Get a Single Custom Model by ID
* [list_platform_models](#list_platform_models) - List Platform Models
* [upload_model_asset](#upload_model_asset) - Upload 3D Model

## create_model

This endpoint will train a new custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.CreateModelRequestBody(
    dataset_id='<value>',
    instance_prompt='<value>',
    name='<value>',
)

res = s.model.create_model(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateModelRequestBody](../../models/operations/createmodelrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete3_d_model_by_id

This endpoint deletes the specific 3D Model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model.delete3_d_model_by_id(id='<value>', request_body=operations.Delete3DModelByIDRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                         | *str*                                                                                                        | :heavy_check_mark:                                                                                           | _"id" is required (enter it either in parameters or request body)_                                           |
| `request_body`                                                                                               | [Optional[operations.Delete3DModelByIDRequestBody]](../../models/operations/delete3dmodelbyidrequestbody.md) | :heavy_minus_sign:                                                                                           | Query parameters can also be provided in the request body as a JSON object                                   |


### Response

**[operations.Delete3DModelByIDResponse](../../models/operations/delete3dmodelbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_model_by_id

This endpoint will delete a specific custom model

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model.delete_model_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `id`                           | *str*                          | :heavy_check_mark:             | The ID of the model to delete. |


### Response

**[operations.DeleteModelByIDResponse](../../models/operations/deletemodelbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get3_d_model_by_id

This endpoint gets the specific 3D model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model.get3_d_model_by_id(id='<value>', request_body=operations.Get3DModelByIDRequestBody(), limit=10, offset=0)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | _"id" is required (enter it either in parameters or request body)_                                     |
| `request_body`                                                                                         | [Optional[operations.Get3DModelByIDRequestBody]](../../models/operations/get3dmodelbyidrequestbody.md) | :heavy_minus_sign:                                                                                     | Query parameters can also be provided in the request body as a JSON object                             |
| `limit`                                                                                                | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `offset`                                                                                               | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |


### Response

**[operations.Get3DModelByIDResponse](../../models/operations/get3dmodelbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get3_d_models_by_user_id

This endpoint returns all 3D models by a specific user

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model.get3_d_models_by_user_id(user_id='<value>', request_body=operations.Get3DModelsByUserIDRequestBody(), limit=10, offset=0)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                        | *str*                                                                                                            | :heavy_check_mark:                                                                                               | N/A                                                                                                              |
| `request_body`                                                                                                   | [Optional[operations.Get3DModelsByUserIDRequestBody]](../../models/operations/get3dmodelsbyuseridrequestbody.md) | :heavy_minus_sign:                                                                                               | Query parameters can also be provided in the request body as a JSON object                                       |
| `limit`                                                                                                          | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |
| `offset`                                                                                                         | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |


### Response

**[operations.Get3DModelsByUserIDResponse](../../models/operations/get3dmodelsbyuseridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_model_by_id

This endpoint gets the specific custom model

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model.get_model_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                             | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `id`                                  | *str*                                 | :heavy_check_mark:                    | The ID of the custom model to return. |


### Response

**[operations.GetModelByIDResponse](../../models/operations/getmodelbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_platform_models

Get a list of public Platform Models available for use with generations.

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.model.list_platform_models()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.ListPlatformModelsResponse](../../models/operations/listplatformmodelsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## upload_model_asset

This endpoint returns presigned details to upload a 3D model to S3

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.UploadModelAssetRequestBody()

res = s.model.upload_model_asset(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UploadModelAssetRequestBody](../../models/operations/uploadmodelassetrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.UploadModelAssetResponse](../../models/operations/uploadmodelassetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
