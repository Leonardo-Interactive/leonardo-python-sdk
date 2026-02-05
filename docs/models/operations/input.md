# Input


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `collection_ids`                                           | List[*Nullable[int]*]                                      | :heavy_minus_sign:                                         | Optional list of collection IDs to add the generations to  | []                                                         |
| `node_inputs`                                              | List[[shared.NodeInput](../../models/shared/nodeinput.md)] | :heavy_check_mark:                                         | Array of node input objects to customize the Blueprint     |                                                            |
| `public`                                                   | *bool*                                                     | :heavy_check_mark:                                         | Whether the resulting generations should be public         | false                                                      |