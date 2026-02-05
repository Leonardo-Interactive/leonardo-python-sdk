# PageInfo

Pagination information following the Relay cursor pagination spec


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `end_cursor`                                | *Optional[str]*                             | :heavy_minus_sign:                          | Cursor for the last item in the result set  |
| `has_next_page`                             | *Optional[bool]*                            | :heavy_minus_sign:                          | Whether there is a next page                |
| `has_previous_page`                         | *Optional[bool]*                            | :heavy_minus_sign:                          | Whether there is a previous page            |
| `start_cursor`                              | *Optional[str]*                             | :heavy_minus_sign:                          | Cursor for the first item in the result set |