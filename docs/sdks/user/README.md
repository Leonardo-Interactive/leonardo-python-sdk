# User
(*user*)

### Available Operations

* [get_user_self](#get_user_self) - Get user information

## get_user_self

This endpoint will return your user information such as your user id, username, token renewal date and current amounts of the following: subscription tokens, gpt (prompt generation) tokens, and model training tokens

### Example Usage

```python
import leonardoaisdk
from leonardoaisdk.models import shared

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)


res = s.user.get_user_self()

if res.get_user_self_200_application_json_object is not None:
    # handle response
    pass
```


### Response

**[operations.GetUserSelfResponse](../../models/operations/getuserselfresponse.md)**

