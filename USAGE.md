<!-- Start SDK Example Usage -->
```python
import leonardoaisdk
from leonardoaisdk.models import operations

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.CreateDatasetRequestBody(
    name='string',
)

res = s.dataset.create_dataset(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->