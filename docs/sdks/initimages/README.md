# InitImages
(*init_images*)

## Overview

### Available Operations

* [delete_init_image_by_id](#delete_init_image_by_id) - Delete init image
* [get_init_image_by_id](#get_init_image_by_id) - Get single init image
* [upload_canvas_init_image](#upload_canvas_init_image) - Upload Canvas Editor init and mask image
* [upload_init_image](#upload_init_image) - Upload init image

## delete_init_image_by_id

This endpoint deletes an init image

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.init_images.delete_init_image_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | _"id" is required_                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteInitImageByIDResponse](../../models/operations/deleteinitimagebyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_init_image_by_id

This endpoint will return a single init image

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.init_images.get_init_image_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | _"id" is required_                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetInitImageByIDResponse](../../models/operations/getinitimagebyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## upload_canvas_init_image

This endpoint returns presigned details to upload an init image and a mask image to S3

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.init_images.upload_canvas_init_image(request={
        "init_extension": "<value>",
        "mask_extension": "<value>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UploadCanvasInitImageRequestBody](../../models/operations/uploadcanvasinitimagerequestbody.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.UploadCanvasInitImageResponse](../../models/operations/uploadcanvasinitimageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## upload_init_image

This endpoint returns presigned details to upload an init image to S3

### Example Usage

```python
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.init_images.upload_init_image(request={
        "extension": "png",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UploadInitImageRequestBody](../../models/operations/uploadinitimagerequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.UploadInitImageResponse](../../models/operations/uploadinitimageresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |