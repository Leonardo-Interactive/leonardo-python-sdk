# variation

### Available Operations

* [create_variation_upscale](#create_variation_upscale) - Create upscale
* [get_variation_by_id](#get_variation_by_id) - Get variation by ID
* [post_variations_unzoom](#post_variations_unzoom) - Create unzoom

## create_variation_upscale

This endpoint will create an upscale for the provided image ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateVariationUpscaleRequestBody(
    id='77dfb14c-d66a-4e39-9efb-9ba88f3a6699',
)

res = s.variation.create_variation_upscale(req)

if res.create_variation_upscale_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateVariationUpscaleRequestBody](../../models/operations/createvariationupscalerequestbody.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreateVariationUpscaleResponse](../../models/operations/createvariationupscaleresponse.md)**


## get_variation_by_id

This endpoint will get the variation by ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.variation.get_variation_by_id(id='molestiae')

if res.get_variation_by_id_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | "id" is required   |


### Response

**[operations.GetVariationByIDResponse](../../models/operations/getvariationbyidresponse.md)**


## post_variations_unzoom

This endpoint will create an unzoom variation for the provided image ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostVariationsUnzoomRequestBody(
    id='074ba446-9b6e-4214-9959-890afa563e25',
    is_variation=False,
)

res = s.variation.post_variations_unzoom(req)

if res.post_variations_unzoom_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostVariationsUnzoomRequestBody](../../models/operations/postvariationsunzoomrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PostVariationsUnzoomResponse](../../models/operations/postvariationsunzoomresponse.md)**

