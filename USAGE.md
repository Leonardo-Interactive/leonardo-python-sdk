<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as las_client:

    res = las_client.init_images.delete_init_image_by_id(id="<id>")

    assert res.object is not None

    # Handle response
    print(res.object)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from leonardo_ai_sdk import LeonardoAiSDK

async def main():
    async with LeonardoAiSDK(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as las_client:

        res = await las_client.init_images.delete_init_image_by_id_async(id="<id>")

        assert res.object is not None

        # Handle response
        print(res.object)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->