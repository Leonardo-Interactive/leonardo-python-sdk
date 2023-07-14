# user

### Available Operations

* [get_user_self](#get_user_self) - Get user information

## get_user_self

This endpoint will return your user such as your user id, username, token renewal date and current amounts of the following: subscription tokens, gpt (prompt generation) tokens, model training tokens and api credit (which is used via a production api key). Please note that the api credit unit is the millicent, ie. 100,000 credits = $1

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import shared

s = leonardoaisdk.LeonardoAiSDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.user.get_user_self()

if res.get_user_self_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.GetUserSelfResponse](../../models/operations/getuserselfresponse.md)**

