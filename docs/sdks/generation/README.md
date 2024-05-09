# Generation
(*generation*)

### Available Operations

* [create_generation](#create_generation) - Create a Generation of Images
* [create_lcm_generation](#create_lcm_generation) - Create LCM Generation
* [create_svd_motion_generation](#create_svd_motion_generation) - Create SVD Motion Generation
* [create_texture_generation](#create_texture_generation) - Create Texture Generation
* [delete_generation_by_id](#delete_generation_by_id) - Delete a Single Generation
* [delete_texture_generation_by_id](#delete_texture_generation_by_id) - Delete Texture Generation by ID
* [get_generation_by_id](#get_generation_by_id) - Get a Single Generation
* [get_generations_by_user_id](#get_generations_by_user_id) - Get generations by user ID
* [get_texture_generation_by_id](#get_texture_generation_by_id) - Get Texture Generation by ID
* [get_texture_generations_by_model_id](#get_texture_generations_by_model_id) - Get texture generations by 3D Model ID
* [perform_alchemy_upscale_lcm](#perform_alchemy_upscale_lcm) - Perform Alchemy Upscale on a LCM image
* [perform_inpainting_lcm](#perform_inpainting_lcm) - Perform inpainting on a LCM image
* [perform_instant_refine](#perform_instant_refine) - Perform instant refine on a LCM image

## create_generation

This endpoint will generate images

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.create_generation(request=operations.CreateGenerationRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateGenerationRequestBody](../../models/operations/creategenerationrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateGenerationResponse](../../models/operations/creategenerationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_lcm_generation

This endpoint will generate a LCM image generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.create_lcm_generation(request=operations.CreateLCMGenerationRequestBody(
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

## create_svd_motion_generation

This endpoint will generate a SVD motion generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.create_svd_motion_generation(request=operations.CreateSVDMotionGenerationRequestBody(
    image_id='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateSVDMotionGenerationRequestBody](../../models/operations/createsvdmotiongenerationrequestbody.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.CreateSVDMotionGenerationResponse](../../models/operations/createsvdmotiongenerationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_texture_generation

This endpoint will generate a texture generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.create_texture_generation(request=operations.CreateTextureGenerationRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.CreateTextureGenerationRequestBody](../../models/operations/createtexturegenerationrequestbody.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.CreateTextureGenerationResponse](../../models/operations/createtexturegenerationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_generation_by_id

This endpoint deletes a specific generation

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.delete_generation_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `id`                                | *str*                               | :heavy_check_mark:                  | The ID of the generation to delete. |


### Response

**[operations.DeleteGenerationByIDResponse](../../models/operations/deletegenerationbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_texture_generation_by_id

This endpoint deletes the specific texture generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.delete_texture_generation_by_id(id='<value>', request_body=operations.DeleteTextureGenerationByIDRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                             | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | _"id" is required (enter it either in parameters or request body)_                                                               |
| `request_body`                                                                                                                   | [Optional[operations.DeleteTextureGenerationByIDRequestBody]](../../models/operations/deletetexturegenerationbyidrequestbody.md) | :heavy_minus_sign:                                                                                                               | Query parameters can also be provided in the request body as a JSON object                                                       |


### Response

**[operations.DeleteTextureGenerationByIDResponse](../../models/operations/deletetexturegenerationbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_generation_by_id

This endpoint will provide information about a specific generation

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.get_generation_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `id`                                | *str*                               | :heavy_check_mark:                  | The ID of the generation to return. |


### Response

**[operations.GetGenerationByIDResponse](../../models/operations/getgenerationbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_generations_by_user_id

This endpoint returns all generations by a specific user

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.get_generations_by_user_id(user_id='<value>', limit=10, offset=0)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `user_id`          | *str*              | :heavy_check_mark: | N/A                |
| `limit`            | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `offset`           | *Optional[int]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetGenerationsByUserIDResponse](../../models/operations/getgenerationsbyuseridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_texture_generation_by_id

This endpoint gets the specific texture generation.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.get_texture_generation_by_id(id='<value>', request_body=operations.GetTextureGenerationByIDRequestBody(), limit=10, offset=0)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                       | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | _"id" is required (enter it either in parameters or request body)_                                                         |
| `request_body`                                                                                                             | [Optional[operations.GetTextureGenerationByIDRequestBody]](../../models/operations/gettexturegenerationbyidrequestbody.md) | :heavy_minus_sign:                                                                                                         | Query parameters can also be provided in the request body as a JSON object                                                 |
| `limit`                                                                                                                    | *Optional[int]*                                                                                                            | :heavy_minus_sign:                                                                                                         | N/A                                                                                                                        |
| `offset`                                                                                                                   | *Optional[int]*                                                                                                            | :heavy_minus_sign:                                                                                                         | N/A                                                                                                                        |


### Response

**[operations.GetTextureGenerationByIDResponse](../../models/operations/gettexturegenerationbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_texture_generations_by_model_id

This endpoint gets the specific texture generations by the 3d model id.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.generation.get_texture_generations_by_model_id(model_id='<value>', request_body=operations.GetTextureGenerationsByModelIDRequestBody(), limit=10, offset=0)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `model_id`                                                                                                                             | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | _"modelId" is required (enter it either in parameters or request body)_                                                                |
| `request_body`                                                                                                                         | [Optional[operations.GetTextureGenerationsByModelIDRequestBody]](../../models/operations/gettexturegenerationsbymodelidrequestbody.md) | :heavy_minus_sign:                                                                                                                     | Query parameters can also be provided in the request body as a JSON object                                                             |
| `limit`                                                                                                                                | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `offset`                                                                                                                               | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |


### Response

**[operations.GetTextureGenerationsByModelIDResponse](../../models/operations/gettexturegenerationsbymodelidresponse.md)**
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

res = s.generation.perform_alchemy_upscale_lcm(request=operations.PerformAlchemyUpscaleLCMRequestBody(
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

res = s.generation.perform_inpainting_lcm(request=operations.PerformInpaintingLCMRequestBody(
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

res = s.generation.perform_instant_refine(request=operations.PerformInstantRefineRequestBody(
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
