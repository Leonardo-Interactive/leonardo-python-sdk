# Element
(*element*)

### Available Operations

* [get_elements](#get_elements) - List Elements

## get_elements

Get a list of public Elements available for use with generations.

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import shared

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)


res = s.element.get_elements()

if res.get_elements_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.GetElementsResponse](../../models/operations/getelementsresponse.md)**

