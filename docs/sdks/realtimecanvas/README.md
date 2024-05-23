# RealtimeCanvas
(*realtime_canvas*)

### Available Operations

* [create_lcm_generation](#create_lcm_generation) - Create LCM Generation
* [perform_alchemy_upscale_lcm](#perform_alchemy_upscale_lcm) - Perform Alchemy Upscale on a LCM image
* [perform_inpainting_lcm](#perform_inpainting_lcm) - Perform inpainting on a LCM image
* [perform_instant_refine](#perform_instant_refine) - Perform instant refine on a LCM image

## create_lcm_generation

This endpoint will generate a LCM image generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.realtime_canvas.create_lcm_generation(request=operations.CreateLCMGenerationRequestBody(
    image_data_url='<value>',
    prompt='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateLCMGenerationRequestBody](../../models/operations/createlcmgenerationrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateLCMGenerationResponse](../../models/operations/createlcmgenerationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## perform_alchemy_upscale_lcm

This endpoint will perform Alchemy Upscale on a LCM image

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.realtime_canvas.perform_alchemy_upscale_lcm(request=operations.PerformAlchemyUpscaleLCMRequestBody(
    image_data_url='<value>',
    prompt='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PerformAlchemyUpscaleLCMRequestBody](../../models/operations/performalchemyupscalelcmrequestbody.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PerformAlchemyUpscaleLCMResponse](../../models/operations/performalchemyupscalelcmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## perform_inpainting_lcm

This endpoint will perform a inpainting on a LCM image

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.realtime_canvas.perform_inpainting_lcm(request=operations.PerformInpaintingLCMRequestBody(
    image_data_url='<value>',
    mask_data_url='<value>',
    prompt='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PerformInpaintingLCMRequestBody](../../models/operations/performinpaintinglcmrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PerformInpaintingLCMResponse](../../models/operations/performinpaintinglcmresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## perform_instant_refine

This endpoint will perform instant refine on a LCM image

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.realtime_canvas.perform_instant_refine(request=operations.PerformInstantRefineRequestBody(
    image_data_url='<value>',
    prompt='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PerformInstantRefineRequestBody](../../models/operations/performinstantrefinerequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PerformInstantRefineResponse](../../models/operations/performinstantrefineresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
