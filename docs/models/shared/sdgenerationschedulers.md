# SdGenerationSchedulers

The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified.

## Example Usage

```python
from leonardo_ai_sdk.models.shared import SdGenerationSchedulers

value = SdGenerationSchedulers.KLMS
```


## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `KLMS`                     | KLMS                       |
| `EULER_ANCESTRAL_DISCRETE` | EULER_ANCESTRAL_DISCRETE   |
| `EULER_DISCRETE`           | EULER_DISCRETE             |
| `DDIM`                     | DDIM                       |
| `DPM_SOLVER`               | DPM_SOLVER                 |
| `PNDM`                     | PNDM                       |
| `LEONARDO`                 | LEONARDO                   |