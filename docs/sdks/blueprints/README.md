# Blueprints

## Overview

### Available Operations

* [execute_blueprint](#execute_blueprint) - Execute a Blueprint
* [get_blueprint_by_id](#get_blueprint_by_id) - Get Blueprint by ID
* [get_blueprint_execution](#get_blueprint_execution) - Get Blueprint Execution by ID
* [get_blueprint_execution_generations](#get_blueprint_execution_generations) - Get Blueprint Execution Generations by Execution ID
* [get_blueprint_versions_by_blueprint_id](#get_blueprint_versions_by_blueprint_id) - Get Blueprint Versions by Blueprint ID
* [list_blueprints](#list_blueprints) - List Blueprints

## execute_blueprint

Execute a Blueprint Version with custom node inputs. This endpoint triggers the execution of the specified Blueprint Version and returns a Blueprint Execution ID to track the job.

### Example Usage

<!-- UsageSnippet language="python" operationID="executeBlueprint" method="post" path="/blueprint-executions" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK
from leonardo_ai_sdk.models import shared


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.execute_blueprint(request={
        "blueprint_version_id": "550e8400-e29b-41d4-a716-446655440000",
        "input": {
            "collection_ids": [],
            "node_inputs": [
                {
                    "node_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                    "setting_name": shared.SettingName.TEXT,
                    "value": "A futuristic cityscape at sunset",
                },
                {
                    "node_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
                    "setting_name": shared.SettingName.TEXT_VARIABLES,
                    "value": [
                        {
                            "name": "characterName",
                            "value": "Luna",
                        },
                        {
                            "name": "outfit",
                            "value": "cyberpunk armor",
                        },
                    ],
                },
                {
                    "node_id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
                    "setting_name": shared.SettingName.IMAGE_URL,
                    "value": "https://cdn.leonardo.ai/users/example/image.png",
                },
            ],
            "public": False,
        },
    })

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ExecuteBlueprintRequestBody](../../models/operations/executeblueprintrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.ExecuteBlueprintResponse](../../models/operations/executeblueprintresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ExecuteBlueprintResponseBody | 400                                 | application/json                    |
| errors.SDKError                     | 4XX, 5XX                            | \*/\*                               |

## get_blueprint_by_id

Returns a single Blueprint by its akUUID

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprintById" method="get" path="/blueprints/{id}" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_by_id(id="151f5c6d-c840-46cd-84ea-f25ac4521a39")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The akUUID of the Blueprint to return                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetBlueprintByIDResponse](../../models/operations/getblueprintbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_blueprint_execution

Retrieves details of a specific Blueprint Execution by its akUUID

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprintExecution" method="get" path="/blueprint-executions/{id}" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_execution(id="<id>")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | The akUUID of the Blueprint Execution to retrieve                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetBlueprintExecutionResponse](../../models/operations/getblueprintexecutionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_blueprint_execution_generations

Retrieves paginated generations for a specific Blueprint Execution, including their statuses and any prompt moderation failure details.

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprintExecutionGenerations" method="get" path="/blueprint-executions/{id}/generations" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_execution_generations(request={
        "id": "<id>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetBlueprintExecutionGenerationsRequest](../../models/operations/getblueprintexecutiongenerationsrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.GetBlueprintExecutionGenerationsResponse](../../models/operations/getblueprintexecutiongenerationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_blueprint_versions_by_blueprint_id

Returns all versions of a Blueprint by its akUUID

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprintVersionsByBlueprintId" method="get" path="/blueprints/{id}/versions" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_versions_by_blueprint_id(id="b18920da-63c6-48a9-8fec-f3b887c8d851")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The akUUID of the Blueprint                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetBlueprintVersionsByBlueprintIDResponse](../../models/operations/getblueprintversionsbyblueprintidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_blueprints

Returns a list of Blueprints. Use either forward pagination (first/after) or backward pagination (last/before), but not both. Note: This endpoint uses a request body to support complex filtering parameters

### Example Usage

<!-- UsageSnippet language="python" operationID="listBlueprints" method="get" path="/blueprints" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK
from leonardo_ai_sdk.models import operations


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.list_blueprints(request={
        "after": "eyJjcmVhdGVkQXQiOiIyMDI1LTEwLTI5VDIxOjMxOjQ3Ljk5OVoiLCJha1VVSUQiOiJjODQ2NDEzZS05MmJhLTQzMDItODRmOC00N2M2NjdkNDc2MWYifQ==",
        "categories": [
            "social-media",
        ],
        "platforms": [
            operations.Platforms.I_OS,
            operations.Platforms.ANDROID,
        ],
    })

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListBlueprintsRequestBody](../../models/operations/listblueprintsrequestbody.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.ListBlueprintsResponse](../../models/operations/listblueprintsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |