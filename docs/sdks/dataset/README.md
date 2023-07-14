# dataset

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
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateDatasetRequestBody(
    description='corrupti',
    name='Ben Mueller',
)

res = s.dataset.create_dataset(req)

if res.create_dataset_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateDatasetRequestBody](../../models/operations/createdatasetrequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateDatasetResponse](../../models/operations/createdatasetresponse.md)**


## delete_dataset_by_id

This endpoint deletes the specific dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteDatasetByIDRequest(
    id='74e0f467-cc87-496e-9151-a05dfc2ddf7c',
)

res = s.dataset.delete_dataset_by_id(req)

if res.delete_dataset_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteDatasetByIDRequest](../../models/operations/deletedatasetbyidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteDatasetByIDResponse](../../models/operations/deletedatasetbyidresponse.md)**


## get_dataset_by_id

This endpoint gets the specific dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDatasetByIDRequest(
    id='c78ca1ba-928f-4c81-a742-cb7392059293',
)

res = s.dataset.get_dataset_by_id(req)

if res.get_dataset_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDatasetByIDRequest](../../models/operations/getdatasetbyidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetDatasetByIDResponse](../../models/operations/getdatasetbyidresponse.md)**


## upload_dataset_image

This endpoint returns presigned details to upload a dataset image to S3

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UploadDatasetImageRequest(
    request_body=operations.UploadDatasetImageRequestBody(
        extension='natus',
    ),
    dataset_id='laboriosam',
)

res = s.dataset.upload_dataset_image(req)

if res.upload_dataset_image_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UploadDatasetImageRequest](../../models/operations/uploaddatasetimagerequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UploadDatasetImageResponse](../../models/operations/uploaddatasetimageresponse.md)**


## upload_dataset_image_from_gen

This endpoint will upload a previously generated image to the dataset

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UploadDatasetImageFromGenRequest(
    request_body=operations.UploadDatasetImageFromGenRequestBody(
        generated_image_id='hic',
    ),
    dataset_id='saepe',
)

res = s.dataset.upload_dataset_image_from_gen(req)

if res.upload_dataset_image_from_gen_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UploadDatasetImageFromGenRequest](../../models/operations/uploaddatasetimagefromgenrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.UploadDatasetImageFromGenResponse](../../models/operations/uploaddatasetimagefromgenresponse.md)**

