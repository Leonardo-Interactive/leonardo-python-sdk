# SettingName

The type of setting to replace:
- `text`: Direct text replacement (value is a string)
- `imageUrl`: Image URL input (value is a URL string)
- `textVariables`: Text with placeholder variables (value is an array of TextVariable)

## Example Usage

```python
from leonardo_ai_sdk.models.shared import SettingName

value = SettingName.TEXT
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `TEXT`           | text             |
| `IMAGE_URL`      | imageUrl         |
| `TEXT_VARIABLES` | textVariables    |