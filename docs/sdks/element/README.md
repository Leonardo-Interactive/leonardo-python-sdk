# Element
(*.element*)

### Available Operations

* [get_elements](#get_elements) - List Elements

## get_elements

Get a list of public Elements available for use with generations.

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)


res = s.element.get_elements()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.GetElementsResponse](../../models/operations/getelementsresponse.md)**

