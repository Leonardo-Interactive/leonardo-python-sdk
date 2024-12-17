# RealtimeCanvas
(*realtime_canvas*)

## Overview

### Available Operations

* [create_lcm_generation](#create_lcm_generation) - Create LCM Generation
* [perform_alchemy_upscale_lcm](#perform_alchemy_upscale_lcm) - Perform Alchemy Upscale on a LCM image
* [perform_inpainting_lcm](#perform_inpainting_lcm) - Perform inpainting on a LCM image
* [perform_instant_refine](#perform_instant_refine) - Perform instant refine on a LCM image

## create_lcm_generation

This endpoint will generate a LCM image generation.

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.realtime_canvas.create_lcm_generation()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateLCMGenerationRequestBody](../../models/operations/createlcmgenerationrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.CreateLCMGenerationResponse](../../models/operations/createlcmgenerationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## perform_alchemy_upscale_lcm

This endpoint will perform Alchemy Upscale on a LCM image

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.realtime_canvas.perform_alchemy_upscale_lcm()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PerformAlchemyUpscaleLCMRequestBody](../../models/operations/performalchemyupscalelcmrequestbody.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.PerformAlchemyUpscaleLCMResponse](../../models/operations/performalchemyupscalelcmresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## perform_inpainting_lcm

This endpoint will perform a inpainting on a LCM image

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.realtime_canvas.perform_inpainting_lcm()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PerformInpaintingLCMRequestBody](../../models/operations/performinpaintinglcmrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PerformInpaintingLCMResponse](../../models/operations/performinpaintinglcmresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## perform_instant_refine

This endpoint will perform instant refine on a LCM image

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as leonardo_ai_sdk:

    res = leonardo_ai_sdk.realtime_canvas.perform_instant_refine()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PerformInstantRefineRequestBody](../../models/operations/performinstantrefinerequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.PerformInstantRefineResponse](../../models/operations/performinstantrefineresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |