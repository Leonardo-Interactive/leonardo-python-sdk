<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from leonardo_ai_sdk import LeonardoAiSDK
from leonardo_ai_sdk.models import shared


with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.blueprints.execute_blueprint(request={
        "blueprint_version_id": "550e8400-e29b-41d4-a716-446655440000",
        "input": {
            "collection_ids": [],
            "node_inputs": [
                {
                    "node_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                    "setting_name": shared.SettingName.TEXT,
                    "value": "A futuristic cityscape at sunset",
                },
                {
                    "node_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
                    "setting_name": shared.SettingName.TEXT_VARIABLES,
                    "value": [
                        {
                            "name": "characterName",
                            "value": "Luna",
                        },
                        {
                            "name": "outfit",
                            "value": "cyberpunk armor",
                        },
                    ],
                },
                {
                    "node_id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
                    "setting_name": shared.SettingName.IMAGE_URL,
                    "value": "https://cdn.leonardo.ai/users/example/image.png",
                },
            ],
            "public": False,
        },
    })

    assert res.one_of is not None

    # Handle response
    print(res.one_of)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from leonardo_ai_sdk import LeonardoAiSDK
from leonardo_ai_sdk.models import shared

async def main():

    async with LeonardoAiSDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as las_client:

        res = await las_client.blueprints.execute_blueprint_async(request={
            "blueprint_version_id": "550e8400-e29b-41d4-a716-446655440000",
            "input": {
                "collection_ids": [],
                "node_inputs": [
                    {
                        "node_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                        "setting_name": shared.SettingName.TEXT,
                        "value": "A futuristic cityscape at sunset",
                    },
                    {
                        "node_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
                        "setting_name": shared.SettingName.TEXT_VARIABLES,
                        "value": [
                            {
                                "name": "characterName",
                                "value": "Luna",
                            },
                            {
                                "name": "outfit",
                                "value": "cyberpunk armor",
                            },
                        ],
                    },
                    {
                        "node_id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
                        "setting_name": shared.SettingName.IMAGE_URL,
                        "value": "https://cdn.leonardo.ai/users/example/image.png",
                    },
                ],
                "public": False,
            },
        })

        assert res.one_of is not None

        # Handle response
        print(res.one_of)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->