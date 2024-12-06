<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from leonardo_ai_sdk import LeonardoAiSDK

with LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.init_images.delete_init_image_by_id(id="<id>")

    if res.object is not None:
        # handle response
        pass
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
    ) as s:
        res = await s.init_images.delete_init_image_by_id_async(id="<id>")

        if res.object is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->