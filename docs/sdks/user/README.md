# User
(*user*)

## Overview

### Available Operations

* [get_user_self](#get_user_self) - Get user information

## get_user_self

This endpoint will return your user information such as your user id, username, token renewal date and current amounts of the following: subscription tokens, gpt (prompt generation) tokens, and model training tokens

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

s = LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.user.get_user_self()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetUserSelfResponse](../../models/operations/getuserselfresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
