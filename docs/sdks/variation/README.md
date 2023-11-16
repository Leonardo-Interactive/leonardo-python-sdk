# Variation
(*variation*)

### Available Operations

* [create_variation_no_bg](#create_variation_no_bg) - Create no background
* [create_variation_upscale](#create_variation_upscale) - Create upscale
* [get_variation_by_id](#get_variation_by_id) - Get variation by ID
* [post_variations_unzoom](#post_variations_unzoom) - Create unzoom

## create_variation_no_bg

This endpoint will create a no background variation of the provided image ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.CreateVariationNoBGRequestBody(
    id='<ID>',
)

res = s.variation.create_variation_no_bg(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateVariationNoBGRequestBody](../../models/operations/createvariationnobgrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateVariationNoBGResponse](../../models/operations/createvariationnobgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## create_variation_upscale

This endpoint will create an upscale for the provided image ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.CreateVariationUpscaleRequestBody(
    id='<ID>',
)

res = s.variation.create_variation_upscale(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateVariationUpscaleRequestBody](../../models/operations/createvariationupscalerequestbody.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreateVariationUpscaleResponse](../../models/operations/createvariationupscaleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_variation_by_id

This endpoint will get the variation by ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)


res = s.variation.get_variation_by_id(id='string')

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | "id" is required   |


### Response

**[operations.GetVariationByIDResponse](../../models/operations/getvariationbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_variations_unzoom

This endpoint will create an unzoom variation for the provided image ID

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.PostVariationsUnzoomRequestBody()

res = s.variation.post_variations_unzoom(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostVariationsUnzoomRequestBody](../../models/operations/postvariationsunzoomrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PostVariationsUnzoomResponse](../../models/operations/postvariationsunzoomresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
