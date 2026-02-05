# APIError

API error response structure


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `extensions`                                                     | [Optional[shared.Extensions]](../../models/shared/extensions.md) | :heavy_minus_sign:                                               | Additional error details and context                             |
| `locations`                                                      | List[[shared.Locations](../../models/shared/locations.md)]       | :heavy_minus_sign:                                               | Location information for the error                               |
| `message`                                                        | *str*                                                            | :heavy_check_mark:                                               | Error message                                                    |
| `path`                                                           | List[*str*]                                                      | :heavy_minus_sign:                                               | Path to the field that caused the error                          |