<!-- Start SDK Example Usage -->


```python
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateDatasetRequestBody(
    description='Synchronised multi-tasking projection',
    name='Quetzal South',
)

res = s.dataset.create_dataset(req)

if res.create_dataset_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->