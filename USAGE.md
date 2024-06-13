<!-- Start SDK Example Usage [usage] -->
```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.init_images.delete_init_image_by_id(id='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->