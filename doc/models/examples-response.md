
# Examples Response

This custom type contains response for examples endpoint.

## Structure

`ExamplesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Optional | The word that is searched. |
| `examples` | `List of string` | Optional | The usage examples of the searched word. |

## Example (as JSON)

```json
{
  "word": "testing",
  "examples": [
    "there are laboratories for commercial testing",
    "it involved testing thousands of children for smallpox",
    "they agreed to end the testing of atomic weapons"
  ]
}
```

