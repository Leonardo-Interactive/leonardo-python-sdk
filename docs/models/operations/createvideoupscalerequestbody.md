# CreateVideoUpscaleRequestBody

Query parameters can also be provided in the request body as a JSON object


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `resolution`                                                                               | [operations.CreateVideoUpscaleString](../../models/operations/createvideoupscalestring.md) | :heavy_check_mark:                                                                         | The resolution of the upscaled video. RESOLUTION_720 is the only option for now.           |
| `source_generation_id`                                                                     | *str*                                                                                      | :heavy_check_mark:                                                                         | The ID of the source video generation to upscale.                                          |