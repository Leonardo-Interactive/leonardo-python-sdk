# Prompt
(*prompt*)

## Overview

### Available Operations

* [prompt_improve](#prompt_improve) - Improve a Prompt
* [prompt_random](#prompt_random) - Generate a Random prompt

## prompt_improve

This endpoint returns a improved prompt

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.prompt.prompt_improve(request={
        "prompt": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PromptImproveRequestBody](../../models/operations/promptimproverequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.PromptImproveResponse](../../models/operations/promptimproveresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## prompt_random

This endpoint returns a random prompt

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.prompt.prompt_random()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.PromptRandomResponse](../../models/operations/promptrandomresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |