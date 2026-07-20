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

### Example Usage: error

<!-- UsageSnippet language="python" operationID="executeBlueprint" method="post" path="/blueprint-executions" example="error" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.execute_blueprint(request={
        "blueprint_version_id": "550e8400-e29b-41d4-a716-446655440000",
        "input": {
            "collection_ids": [],
            "node_inputs": [],
            "public": False,
        },
    })

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="executeBlueprint" method="post" path="/blueprint-executions" example="success" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.execute_blueprint(request={
        "blueprint_version_id": "550e8400-e29b-41d4-a716-446655440000",
        "input": {
            "collection_ids": [],
            "node_inputs": [],
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

### Example Usage: badRequest

<!-- UsageSnippet language="python" operationID="getBlueprintById" method="get" path="/blueprints/{id}" example="badRequest" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_by_id(id="8f161ed5-dc84-4f5b-8ef5-4f3e5821df56")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```
### Example Usage: notFound

<!-- UsageSnippet language="python" operationID="getBlueprintById" method="get" path="/blueprints/{id}" example="notFound" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_by_id(id="d5f01775-fb53-4c5c-8d08-df840b5a6c71")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getBlueprintById" method="get" path="/blueprints/{id}" example="success" -->
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

### Example Usage: badRequest

<!-- UsageSnippet language="python" operationID="getBlueprintExecution" method="get" path="/blueprint-executions/{id}" example="badRequest" -->
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
### Example Usage: notFound

<!-- UsageSnippet language="python" operationID="getBlueprintExecution" method="get" path="/blueprint-executions/{id}" example="notFound" -->
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
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getBlueprintExecution" method="get" path="/blueprint-executions/{id}" example="success" -->
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

### Example Usage: notAccessible

<!-- UsageSnippet language="python" operationID="getBlueprintExecutionGenerations" method="get" path="/blueprint-executions/{id}/generations" example="notAccessible" -->
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
### Example Usage: promptModerationFailure

<!-- UsageSnippet language="python" operationID="getBlueprintExecutionGenerations" method="get" path="/blueprint-executions/{id}/generations" example="promptModerationFailure" -->
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
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getBlueprintExecutionGenerations" method="get" path="/blueprint-executions/{id}/generations" example="success" -->
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

### Example Usage: badRequest

<!-- UsageSnippet language="python" operationID="getBlueprintVersionsByBlueprintId" method="get" path="/blueprints/{id}/versions" example="badRequest" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_versions_by_blueprint_id(id="a6daa51b-6406-4e13-93f8-b7c8344fad6c")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```
### Example Usage: notFound

<!-- UsageSnippet language="python" operationID="getBlueprintVersionsByBlueprintId" method="get" path="/blueprints/{id}/versions" example="notFound" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.get_blueprint_versions_by_blueprint_id(id="7b44812d-6ac6-40b5-ad08-7c47a3f9807c")

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="getBlueprintVersionsByBlueprintId" method="get" path="/blueprints/{id}/versions" example="success" -->
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

### Example Usage: error

<!-- UsageSnippet language="python" operationID="listBlueprints" method="get" path="/blueprints" example="error" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK
from leonardo_ai_sdk.models import operations


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.list_blueprints(request={
        "categories": [
            "social-media",
        ],
        "platforms": [
            operations.Platforms.API,
            operations.Platforms.WEB,
        ],
    })

    assert res.one_of is not None

    # Handle response
    print(res.one_of)

```
### Example Usage: success

<!-- UsageSnippet language="python" operationID="listBlueprints" method="get" path="/blueprints" example="success" -->
```python
from leonardo_ai_sdk import LeonardoAiSDK
from leonardo_ai_sdk.models import operations


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.list_blueprints(request={
        "categories": [
            "social-media",
        ],
        "platforms": [
            operations.Platforms.API,
            operations.Platforms.WEB,
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