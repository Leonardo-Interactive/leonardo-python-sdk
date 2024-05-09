# Prompt
(*prompt*)

### Available Operations

* [prompt_improve](#prompt_improve) - Improve a Prompt
* [prompt_random](#prompt_random) - Generate a Random prompt

## prompt_improve

This endpoint returns a improved prompt

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.prompt.prompt_improve(request=operations.PromptImproveRequestBody(
    prompt='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PromptImproveRequestBody](../../models/operations/promptimproverequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PromptImproveResponse](../../models/operations/promptimproveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## prompt_random

This endpoint returns a random prompt

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.prompt.prompt_random()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.PromptRandomResponse](../../models/operations/promptrandomresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
