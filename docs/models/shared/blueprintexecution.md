# BlueprintExecution

Represents the Execution of a Blueprint Version


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `ak_uuid`                                                                          | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `created_at`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `inputs`                                                                           | List[[shared.NodeInput](../../models/shared/nodeinput.md)]                         | :heavy_check_mark:                                                                 | Inputs of the Blueprint Execution                                                  |
| `public`                                                                           | *bool*                                                                             | :heavy_check_mark:                                                                 | N/A                                                                                |
| `status`                                                                           | [shared.BlueprintExecutionStatus](../../models/shared/blueprintexecutionstatus.md) | :heavy_check_mark:                                                                 | The status of a Blueprint Execution.                                               |