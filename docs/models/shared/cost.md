# Cost

The cost of the operation.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `amount`                                                                                     | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | The amount of the cost.                                                                      |
| `unit`                                                                                       | [Optional[shared.Unit]](../../models/shared/unit.md)                                         | :heavy_minus_sign:                                                                           | The unit of the cost. Can be CREDITS or DOLLARS. Note: DOLLARS unit only supports PAYG plan. |