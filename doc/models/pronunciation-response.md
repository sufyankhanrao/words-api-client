
# Pronunciation Response

This custom type contains response for pronunciation endpoint.

## Structure

`PronunciationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Optional | The word that is searched. |
| `pronunciation` | [`PronunciationDetails`](../../doc/models/pronunciation-details.md) | Optional | This model contains pronunciation details of a specific word. |

## Example (as JSON)

```json
{
  "word": "wind",
  "pronunciation": {
    "all": "wɪnd",
    "noun": "wɪnd",
    "verb": "waɪnd"
  }
}
```

