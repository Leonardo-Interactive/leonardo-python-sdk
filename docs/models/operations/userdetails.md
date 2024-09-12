# UserDetails

columns and relationships of "user_details"


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `api_concurrency_slots`                                                | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | API Concurrency Slots.                                                 |
| `api_paid_tokens`                                                      | *OptionalNullable[int]*                                                | :heavy_minus_sign:                                                     | Current balance of API paid tokens the user has.                       |
| `api_plan_token_renewal_date`                                          | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | API Plan Token Renewal Date.                                           |
| `api_subscription_tokens`                                              | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Current balance of Enterprise API subscriptions tokens the user has.   |
| `paid_tokens`                                                          | *OptionalNullable[int]*                                                | :heavy_minus_sign:                                                     | Current balance of paid tokens the user has.                           |
| `subscription_gpt_tokens`                                              | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Current balance of user plan GPT tokens the user has.                  |
| `subscription_model_tokens`                                            | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Current balance of model training tokens the user has.                 |
| `subscription_tokens`                                                  | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Current balance of user plan subscription tokens the user has.         |
| `token_renewal_date`                                                   | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | User Plan Token Renewal Date.                                          |
| `user`                                                                 | [OptionalNullable[operations.Users]](../../models/operations/users.md) | :heavy_minus_sign:                                                     | columns and relationships of "users"                                   |