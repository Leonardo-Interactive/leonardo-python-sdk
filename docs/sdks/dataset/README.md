# Dataset
(*dataset*)

### Available Operations

* [create_dataset](#create_dataset) - Create a Dataset
* [delete_dataset_by_id](#delete_dataset_by_id) - Delete a Single Dataset by ID
* [get_dataset_by_id](#get_dataset_by_id) - Get a Single Dataset by ID
* [upload_dataset_image](#upload_dataset_image) - Upload dataset image
* [upload_dataset_image_from_gen](#upload_dataset_image_from_gen) - Upload a Single Generated Image to a Dataset

## create_dataset

This endpoint creates a new dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.CreateDatasetRequestBody(
    name='string',
)

res = s.dataset.create_dataset(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateDatasetRequestBody](../../models/operations/createdatasetrequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateDatasetResponse](../../models/operations/createdatasetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_dataset_by_id

This endpoint deletes the specific dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.delete_dataset_by_id(id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `id`                             | *str*                            | :heavy_check_mark:               | The ID of the dataset to delete. |


### Response

**[operations.DeleteDatasetByIDResponse](../../models/operations/deletedatasetbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dataset_by_id

This endpoint gets the specific dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.get_dataset_by_id(id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `id`                             | *str*                            | :heavy_check_mark:               | The ID of the dataset to return. |


### Response

**[operations.GetDatasetByIDResponse](../../models/operations/getdatasetbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upload_dataset_image

This endpoint returns presigned details to upload a dataset image to S3

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.upload_dataset_image(request_body=operations.UploadDatasetImageRequestBody(
    extension='mpg4',
), dataset_id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                       | [operations.UploadDatasetImageRequestBody](../../models/operations/uploaddatasetimagerequestbody.md) | :heavy_check_mark:                                                                                   | Query parameters provided in the request body as a JSON object                                       |
| `dataset_id`                                                                                         | *str*                                                                                                | :heavy_check_mark:                                                                                   | _"datasetId" is required                                                                             |


### Response

**[operations.UploadDatasetImageResponse](../../models/operations/uploaddatasetimageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upload_dataset_image_from_gen

This endpoint will upload a previously generated image to the dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.dataset.upload_dataset_image_from_gen(request_body=operations.UploadDatasetImageFromGenRequestBody(
    generated_image_id='string',
), dataset_id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request_body`                                                                                                     | [operations.UploadDatasetImageFromGenRequestBody](../../models/operations/uploaddatasetimagefromgenrequestbody.md) | :heavy_check_mark:                                                                                                 | Query parameters to be provided in the request body as a JSON object                                               |
| `dataset_id`                                                                                                       | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | The ID of the dataset to upload the image to.                                                                      |


### Response

**[operations.UploadDatasetImageFromGenResponse](../../models/operations/uploaddatasetimagefromgenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
