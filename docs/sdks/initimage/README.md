# InitImage
(*.init_image*)

### Available Operations

* [delete_init_image_by_id](#delete_init_image_by_id) - Delete init image
* [get_init_image_by_id](#get_init_image_by_id) - Get single init image
* [upload_init_image](#upload_init_image) - Upload init image

## delete_init_image_by_id

This endpoint deletes an init image

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)


res = s.init_image.delete_init_image_by_id(id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | _"id" is required_ |


### Response

**[operations.DeleteInitImageByIDResponse](../../models/operations/deleteinitimagebyidresponse.md)**


## get_init_image_by_id

This endpoint will return a single init image

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)


res = s.init_image.get_init_image_by_id(id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | _"id" is required_ |


### Response

**[operations.GetInitImageByIDResponse](../../models/operations/getinitimagebyidresponse.md)**


## upload_init_image

This endpoint returns presigned details to upload an init image to S3

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.UploadInitImageRequestBody(
    extension='png',
)

res = s.init_image.upload_init_image(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UploadInitImageRequestBody](../../models/operations/uploadinitimagerequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.UploadInitImageResponse](../../models/operations/uploadinitimageresponse.md)**

