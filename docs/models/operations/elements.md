# Elements

Element used for the generation.


## Fields

| Field                                                                                                                                      | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `ak_uuid`                                                                                                                                  | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Unique identifier for the element. Elements can be found from the List Elements endpoint.                                                  |
| `base_model`                                                                                                                               | [Optional[shared.SdVersions]](../../models/shared/sdversions.md)                                                                           | :heavy_minus_sign:                                                                                                                         | The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. |
| `description`                                                                                                                              | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Description for the element                                                                                                                |
| `name`                                                                                                                                     | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Name of the element                                                                                                                        |
| `url_image`                                                                                                                                | *Optional[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | URL of the element image                                                                                                                   |
| `weight_default`                                                                                                                           | *Optional[int]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Default weight for the element                                                                                                             |
| `weight_max`                                                                                                                               | *Optional[int]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Maximum weight for the element                                                                                                             |
| `weight_min`                                                                                                                               | *Optional[int]*                                                                                                                            | :heavy_minus_sign:                                                                                                                         | Minimum weight for the element                                                                                                             |