# ExecuteBlueprintResponseBody

Bad Request - Invalid input type or missing required GraphQL field


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `raw_response`                                                       | [httpx.Response](https://www.python-httpx.org/api/#response)         | :heavy_minus_sign:                                                   | Raw HTTP response; suitable for custom response parsing              |                                                                      |
| `error`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Error message describing the invalid input type or missing field     | Invalid input type: expected 'string' for field 'blueprintVersionId' |