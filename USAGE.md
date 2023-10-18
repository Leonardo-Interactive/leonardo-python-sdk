<!-- Start SDK Example Usage -->


```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.CreateDatasetRequestBody(
    name='Van',
)

res = s.dataset.create_dataset(req)

if res.create_dataset_200_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->