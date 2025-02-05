# PricingCalculator
(*pricing_calculator*)

## Overview

### Available Operations

* [pricing_calculator](#pricing_calculator) - Calculating API Cost

## pricing_calculator

This endpoint returns the cost used for generating images using a particular service type.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.pricing_calculator.pricing_calculator()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PricingCalculatorRequestBody](../../models/operations/pricingcalculatorrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.PricingCalculatorResponse](../../models/operations/pricingcalculatorresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |