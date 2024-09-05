# Motion
(*motion*)

## Overview

### Available Operations

* [create_svd_motion_generation](#create_svd_motion_generation) - Create SVD Motion Generation

## create_svd_motion_generation

This endpoint will generate a SVD motion generation.

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
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

### Response

**[operations.CreateSVDMotionGenerationResponse](../../models/operations/createsvdmotiongenerationresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
