# User
(*user*)

### Available Operations

* [get_user_self](#get_user_self) - Get user information

## get_user_self

This endpoint will return your user information such as your user id, username, token renewal date and current amounts of the following: subscription tokens, gpt (prompt generation) tokens, and model training tokens

### Example Usage

```python
import leonardoaisdk

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.user.get_user_self()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetUserSelfResponse](../../models/operations/getuserselfresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
