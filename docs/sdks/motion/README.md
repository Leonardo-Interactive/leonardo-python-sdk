# Motion
(*motion*)

## Overview

### Available Operations

* [create_image_to_video_generation](#create_image_to_video_generation) - Create a video generation from an image
* [create_svd_motion_generation](#create_svd_motion_generation) - Create SVD Motion Generation
* [create_text_to_video_generation](#create_text_to_video_generation) - Create a video generation from a text prompt
* [create_video_upscale](#create_video_upscale) - Upscale a generated video

## create_image_to_video_generation

This endpoint will generate a video using an uploaded or generated image.

### Example Usage

<!-- UsageSnippet language="python" operationID="createImageToVideoGeneration" method="post" path="/generations-image-to-video" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.motion.create_image_to_video_generation()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.CreateImageToVideoGenerationRequestBody](../../models/operations/createimagetovideogenerationrequestbody.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.CreateImageToVideoGenerationResponse](../../models/operations/createimagetovideogenerationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_svd_motion_generation

This endpoint will generate a SVD motion generation.

### Example Usage

<!-- UsageSnippet language="python" operationID="createSVDMotionGeneration" method="post" path="/generations-motion-svd" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.motion.create_svd_motion_generation()

    assert res.object is not None

    # Handle response
    print(res.object)

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

## create_text_to_video_generation

This endpoint will generate a video using a text prompt

### Example Usage

<!-- UsageSnippet language="python" operationID="createTextToVideoGeneration" method="post" path="/generations-text-to-video" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.motion.create_text_to_video_generation()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.CreateTextToVideoGenerationRequestBody](../../models/operations/createtexttovideogenerationrequestbody.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.CreateTextToVideoGenerationResponse](../../models/operations/createtexttovideogenerationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_video_upscale

This endpoint will upscale a generated video to a higher resolution.

### Example Usage

<!-- UsageSnippet language="python" operationID="createVideoUpscale" method="post" path="/generations-video-upscale" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.motion.create_video_upscale()

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateVideoUpscaleRequestBody](../../models/operations/createvideoupscalerequestbody.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.CreateVideoUpscaleResponse](../../models/operations/createvideoupscaleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |