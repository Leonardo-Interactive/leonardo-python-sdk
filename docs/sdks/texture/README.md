# Texture
(*texture*)

## Overview

### Available Operations

* [create_texture_generation](#create_texture_generation) - Create Texture Generation
* [delete_texture_generation_by_id](#delete_texture_generation_by_id) - Delete Texture Generation by ID
* [get_texture_generation_by_id](#get_texture_generation_by_id) - Get Texture Generation by ID
* [get_texture_generations_by_model_id](#get_texture_generations_by_model_id) - Get texture generations by 3D Model ID

## create_texture_generation

This endpoint will generate a texture generation.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.texture.create_texture_generation()

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateTextureGenerationRequestBody](../../models/operations/createtexturegenerationrequestbody.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.CreateTextureGenerationResponse](../../models/operations/createtexturegenerationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_texture_generation_by_id

This endpoint deletes the specific texture generation.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.texture.delete_texture_generation_by_id(id="<id>")

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                             | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | _"id" is required (enter it either in parameters or request body)_                                                               |
| `request_body`                                                                                                                   | [Optional[operations.DeleteTextureGenerationByIDRequestBody]](../../models/operations/deletetexturegenerationbyidrequestbody.md) | :heavy_minus_sign:                                                                                                               | Query parameters can also be provided in the request body as a JSON object                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.DeleteTextureGenerationByIDResponse](../../models/operations/deletetexturegenerationbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_texture_generation_by_id

This endpoint gets the specific texture generation.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.texture.get_texture_generation_by_id(id="<id>")

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                       | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | _"id" is required (enter it either in parameters or request body)_                                                         |
| `limit`                                                                                                                    | *Optional[int]*                                                                                                            | :heavy_minus_sign:                                                                                                         | N/A                                                                                                                        |
| `offset`                                                                                                                   | *Optional[int]*                                                                                                            | :heavy_minus_sign:                                                                                                         | N/A                                                                                                                        |
| `request_body`                                                                                                             | [Optional[operations.GetTextureGenerationByIDRequestBody]](../../models/operations/gettexturegenerationbyidrequestbody.md) | :heavy_minus_sign:                                                                                                         | Query parameters can also be provided in the request body as a JSON object                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.GetTextureGenerationByIDResponse](../../models/operations/gettexturegenerationbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_texture_generations_by_model_id

This endpoint gets the specific texture generations by the 3d model id.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.texture.get_texture_generations_by_model_id(model_id="<value>")

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `model_id`                                                                                                                             | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | _"modelId" is required (enter it either in parameters or request body)_                                                                |
| `limit`                                                                                                                                | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `offset`                                                                                                                               | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `request_body`                                                                                                                         | [Optional[operations.GetTextureGenerationsByModelIDRequestBody]](../../models/operations/gettexturegenerationsbymodelidrequestbody.md) | :heavy_minus_sign:                                                                                                                     | Query parameters can also be provided in the request body as a JSON object                                                             |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[operations.GetTextureGenerationsByModelIDResponse](../../models/operations/gettexturegenerationsbymodelidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |