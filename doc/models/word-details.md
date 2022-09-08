
# Word Details

This custom type stores word information.

## Structure

`WordDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `definition` | `string` | Optional | Explains the definition of the word. |
| `part_of_speech` | `string` | Optional | Explains what part of speech the word is. |
| `synonyms` | `List of string` | Optional | The list of synonyms. |
| `type_of` | `List of string` | Optional | List of words that are more general than the searched word. |
| `has_types` | `List of string` | Optional | More specific examples of types of searched word. |
| `derivation` | `List of string` | Optional | The derivation if any. |
| `examples` | `List of string` | Optional | The usage examples of word if any. |
| `antonyms` | `List of string` | Optional | List of antonyms for the searched word. |
| `verb_group` | `List of string` | Optional | The verb group of the searched word. |
| `has_parts` | `List of string` | Optional | Words that are parts of the searched word. |
| `has_substances` | `List of string` | Optional | Words that are substances of the searched word. |
| `entails` | `List of string` | Optional | Words that are implied by the searched word. Usually used for verbs. |

## Example (as JSON)

```json
{
  "definition": "coil the spring of (some mechanical device) by turning a stem",
  "partOfSpeech": "verb",
  "synonyms": [
    "wind up"
  ],
  "entails": [
    "turn"
  ],
  "typeOf": [
    "fasten",
    "tighten"
  ],
  "hasTypes": [
    "rewind"
  ],
  "derivation": [
    "winder"
  ],
  "examples": [
    "wind your watch"
  ]
}
```

