# Motion
(*motion*)

## Overview

### Available Operations

* [create_svd_motion_generation](#create_svd_motion_generation) - Create SVD Motion Generation

## create_svd_motion_generation

This endpoint will generate a SVD motion generation.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.motion.create_svd_motion_generation()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateSVDMotionGenerationRequestBody](../../models/operations/createsvdmotiongenerationrequestbody.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.CreateSVDMotionGenerationResponse](../../models/operations/createsvdmotiongenerationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |