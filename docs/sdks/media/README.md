# Media

## Overview

### Available Operations

* [delete_uploaded_media_by_id](#delete_uploaded_media_by_id) - Delete uploaded media
* [get_uploaded_media_by_id](#get_uploaded_media_by_id) - Get uploaded media
* [upload_media](#upload_media) - Upload media

## delete_uploaded_media_by_id

This endpoint deletes an uploaded media record and removes the associated file from S3

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteUploadedMediaById" method="delete" path="/media/{id}" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.media.delete_uploaded_media_by_id(id="<id>")

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

**[operations.DeleteUploadedMediaByIDResponse](../../models/operations/deleteuploadedmediabyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_uploaded_media_by_id

This endpoint returns details of an uploaded media record

### Example Usage

<!-- UsageSnippet language="python" operationID="getUploadedMediaById" method="get" path="/media/{id}" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.media.get_uploaded_media_by_id(id="<id>")

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

**[operations.GetUploadedMediaByIDResponse](../../models/operations/getuploadedmediabyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## upload_media

This endpoint returns presigned POST credentials to upload a video or audio file directly to S3.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadMedia" method="post" path="/media" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.media.upload_media(request={
        "extension": "pdf",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UploadMediaRequestBody](../../models/operations/uploadmediarequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.UploadMediaResponse](../../models/operations/uploadmediaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |