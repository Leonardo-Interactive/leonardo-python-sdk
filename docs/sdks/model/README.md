# model

### Available Operations

* [create_model](#create_model) - Train a Custom Model
* [delete_model_by_id](#delete_model_by_id) - Delete a Single Custom Model by ID
* [get_model_by_id](#get_model_by_id) - Get a Single Custom Model by ID

## create_model

This endpoint will train a new custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateModelRequestBody(
    dataset_id='in',
    description='illum',
    instance_prompt='maiores',
    model_type=shared.CustomModelType.PIXEL_ART,
    name='Valerie Runolfsson',
    nsfw=False,
    resolution=396506,
    sd_version=shared.SdVersions.V2,
    strength=shared.Strength.HIGH,
)

res = s.model.create_model(req)

if res.create_model_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreateModelRequestBody](../../models/operations/createmodelrequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**


## delete_model_by_id

This endpoint will delete a specific custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteModelByIDRequest(
    id='395efb9b-a88f-43a6-a997-074ba4469b6e',
)

res = s.model.delete_model_by_id(req)

if res.delete_model_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteModelByIDRequest](../../models/operations/deletemodelbyidrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.DeleteModelByIDResponse](../../models/operations/deletemodelbyidresponse.md)**


## get_model_by_id

This endpoint gets the specific custom model

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetModelByIDRequest(
    id='21419598-90af-4a56-be25-16fe4c8b711e',
)

res = s.model.get_model_by_id(req)

if res.get_model_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetModelByIDRequest](../../models/operations/getmodelbyidrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetModelByIDResponse](../../models/operations/getmodelbyidresponse.md)**

