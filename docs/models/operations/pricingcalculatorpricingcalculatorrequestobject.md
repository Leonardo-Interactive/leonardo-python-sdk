# PricingCalculatorPricingCalculatorRequestObject

Parameters for LCM_GENERATION service


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `height`                                                  | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | The output height of the image. Must be 512, 640 or 1024. |
| `instant_refine`                                          | *OptionalNullable[bool]*                                  | :heavy_minus_sign:                                        | Enable for instant upscale                                |
| `refine`                                                  | *OptionalNullable[bool]*                                  | :heavy_minus_sign:                                        | Enable for normal alchemy upscale                         |
| `width`                                                   | *OptionalNullable[int]*                                   | :heavy_minus_sign:                                        | The output width of the image. Must be 512, 640 or 1024.  |