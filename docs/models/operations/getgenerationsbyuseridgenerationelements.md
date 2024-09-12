# GetGenerationsByUserIDGenerationElements

This table captures the elements that are applied to a Generations, also the order and weightings used when applied.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *OptionalNullable[int]*                                                      | :heavy_minus_sign:                                                           | N/A                                                                          |
| `lora`                                                                       | [OptionalNullable[operations.Elements]](../../models/operations/elements.md) | :heavy_minus_sign:                                                           | Element used for the generation.                                             |
| `weight_applied`                                                             | *OptionalNullable[float]*                                                    | :heavy_minus_sign:                                                           | N/A                                                                          |