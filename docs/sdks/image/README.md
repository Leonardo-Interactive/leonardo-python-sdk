# Image
(*image*)

## Overview

### Available Operations

* [create_generation](#create_generation) - Create a Generation of Images
* [delete_generation_by_id](#delete_generation_by_id) - Delete a Single Generation
* [get_generation_by_id](#get_generation_by_id) - Get a Single Generation
* [get_generations_by_user_id](#get_generations_by_user_id) - Get generations by user ID

## create_generation

This endpoint will generate images

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.image.create_generation(request={})

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateGenerationRequestBody](../../models/operations/creategenerationrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateGenerationResponse](../../models/operations/creategenerationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_generation_by_id

This endpoint deletes a specific generation

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.image.delete_generation_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the generation to delete.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteGenerationByIDResponse](../../models/operations/deletegenerationbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_generation_by_id

This endpoint will provide information about a specific generation

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.image.get_generation_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the generation to return.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetGenerationByIDResponse](../../models/operations/getgenerationbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_generations_by_user_id

This endpoint returns all generations by a specific user

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.image.get_generations_by_user_id(user_id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetGenerationsByUserIDResponse](../../models/operations/getgenerationsbyuseridresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |