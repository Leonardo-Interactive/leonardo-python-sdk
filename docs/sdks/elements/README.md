# Elements
(*elements*)

## Overview

### Available Operations

* [list_elements](#list_elements) - List Elements

## list_elements

Get a list of public Elements available for use with generations.

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.elements.list_elements()

if res.object is not None:
    # handle response
    pass

```

### Response

**[operations.ListElementsResponse](../../models/operations/listelementsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
