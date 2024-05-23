# PricingCalculator
(*pricing_calculator*)

### Available Operations

* [pricing_calculator](#pricing_calculator) - Calculating API Cost

## pricing_calculator

This endpoint returns the cost used for generating images using a particular service type.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.pricing_calculator.pricing_calculator(request=operations.PricingCalculatorRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PricingCalculatorRequestBody](../../models/operations/pricingcalculatorrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PricingCalculatorResponse](../../models/operations/pricingcalculatorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
