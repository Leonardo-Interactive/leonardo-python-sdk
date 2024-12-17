# ThreeDModelAssets
(*three_d_model_assets*)

## Overview

### Available Operations

* [delete3_d_model_by_id](#delete3_d_model_by_id) - Delete 3D Model by ID
* [get3_d_model_by_id](#get3_d_model_by_id) - Get 3D Model by ID
* [get3_d_models_by_user_id](#get3_d_models_by_user_id) - Get 3D models by user ID
* [upload_model_asset](#upload_model_asset) - Upload 3D Model

## delete3_d_model_by_id

This endpoint deletes the specific 3D Model

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.three_d_model_assets.delete3_d_model_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                         | *str*                                                                                                        | :heavy_check_mark:                                                                                           | _"id" is required (enter it either in parameters or request body)_                                           |
| `request_body`                                                                                               | [Optional[operations.Delete3DModelByIDRequestBody]](../../models/operations/delete3dmodelbyidrequestbody.md) | :heavy_minus_sign:                                                                                           | Query parameters can also be provided in the request body as a JSON object                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.Delete3DModelByIDResponse](../../models/operations/delete3dmodelbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get3_d_model_by_id

This endpoint gets the specific 3D model

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.three_d_model_assets.get3_d_model_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                   | *str*                                                                                                  | :heavy_check_mark:                                                                                     | _"id" is required (enter it either in parameters or request body)_                                     |
| `limit`                                                                                                | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `offset`                                                                                               | *Optional[int]*                                                                                        | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |
| `request_body`                                                                                         | [Optional[operations.Get3DModelByIDRequestBody]](../../models/operations/get3dmodelbyidrequestbody.md) | :heavy_minus_sign:                                                                                     | Query parameters can also be provided in the request body as a JSON object                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.Get3DModelByIDResponse](../../models/operations/get3dmodelbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get3_d_models_by_user_id

This endpoint returns all 3D models by a specific user

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.three_d_model_assets.get3_d_models_by_user_id(user_id="<value>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                        | *str*                                                                                                            | :heavy_check_mark:                                                                                               | N/A                                                                                                              |
| `limit`                                                                                                          | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |
| `offset`                                                                                                         | *Optional[int]*                                                                                                  | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |
| `request_body`                                                                                                   | [Optional[operations.Get3DModelsByUserIDRequestBody]](../../models/operations/get3dmodelsbyuseridrequestbody.md) | :heavy_minus_sign:                                                                                               | Query parameters can also be provided in the request body as a JSON object                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.Get3DModelsByUserIDResponse](../../models/operations/get3dmodelsbyuseridresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## upload_model_asset

This endpoint returns presigned details to upload a 3D model to S3

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.three_d_model_assets.upload_model_asset()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.UploadModelAssetRequestBody](../../models/operations/uploadmodelassetrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.UploadModelAssetResponse](../../models/operations/uploadmodelassetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |