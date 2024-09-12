# Models
(*models*)

## Overview

### Available Operations

* [create_model](#create_model) - Train a Custom Model
* [delete_model_by_id](#delete_model_by_id) - Delete a Single Custom Model by ID
* [get_model_by_id](#get_model_by_id) - Get a Single Custom Model by ID
* [list_platform_models](#list_platform_models) - List Platform Models

## create_model

This endpoint will train a new custom model

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.models.create_model(request={
    "dataset_id": "<value>",
    "instance_prompt": "<value>",
    "name": "<value>",
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateModelRequestBody](../../models/operations/createmodelrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## delete_model_by_id

This endpoint will delete a specific custom model

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.models.delete_model_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to delete.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteModelByIDResponse](../../models/operations/deletemodelbyidresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## get_model_by_id

This endpoint gets the specific custom model

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.models.get_model_by_id(id="<id>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the custom model to return.                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
from leonardo_ai_sdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.models.list_platform_models()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListPlatformModelsResponse](../../models/operations/listplatformmodelsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
