<!-- Start SDK Example Usage [usage] -->
```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.dataset.create_dataset(request=operations.CreateDatasetRequestBody(
    name='<value>',
))

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->