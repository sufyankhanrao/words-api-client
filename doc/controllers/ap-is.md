# AP Is

```python
ap_is_controller = client.ap_is
```

## Class Name

`APIsController`

## Methods

* [Synonyms](../../doc/controllers/ap-is.md#synonyms)
* [Definitions](../../doc/controllers/ap-is.md#definitions)
* [Pronunciation](../../doc/controllers/ap-is.md#pronunciation)
* [Word](../../doc/controllers/ap-is.md#word)
* [Examples](../../doc/controllers/ap-is.md#examples)
* [Frequency](../../doc/controllers/ap-is.md#frequency)


# Synonyms

Get synonyms of a word.

```python
def synonyms(self,
            word)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Template, Required | The word to search synonyms for. |

## Response Type

[`SynonymsResponse`](../../doc/models/synonyms-response.md)

## Example Usage

```python
word = 'lovely'

result = ap_is_controller.synonyms(word)
```

## Example Response *(as JSON)*

```json
{
  "word": "lovely",
  "synonyms": [
    "adorable",
    "endearing",
    "cover girl",
    "pin-up"
  ]
}
```


# Definitions

Get definitions of a word, including the part of speech.

```python
def definitions(self,
               word)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Template, Required | The word to search the definitions for. |

## Response Type

[`DefinitionsResponse`](../../doc/models/definitions-response.md)

## Example Usage

```python
word = 'lovely'

result = ap_is_controller.definitions(word)
```

## Example Response *(as JSON)*

```json
{
  "word": "lovely",
  "definition": [
    "lovable especially in a childlike or naive way",
    "a very pretty girl who works as a photographer's model",
    "appealing to the emotions as well as the eye"
  ]
}
```


# Pronunciation

How to pronounce a word, according to the International Phonetic Alphabet. May include multiple results if the word is pronounced differently depending on its part of speech.

```python
def pronunciation(self,
                 word)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Template, Required | The word to search pronunciation for. |

## Response Type

[`PronunciationResponse`](../../doc/models/pronunciation-response.md)

## Example Usage

```python
word = 'wind'

result = ap_is_controller.pronunciation(word)
```

## Example Response *(as JSON)*

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


# Word

Retrieve information about a word. Results can include definitions, part of speech, synonyms, related words, syllables, and pronunciation. This method is useful to see which relationships are attached to which definition and part of speech of a word.

```python
def word(self,
        word)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Template, Required | This is a template parameter that is used to provide the word, about which the information is being fetched. |

## Response Type

[`WordResponse`](../../doc/models/word-response.md)

## Example Usage

```python
word = 'Testing'

result = ap_is_controller.word(word)
```


# Examples

Get examples of how the word is used.

```python
def examples(self,
            word)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Template, Required | The word to search the examples for. |

## Response Type

[`ExamplesResponse`](../../doc/models/examples-response.md)

## Example Usage

```python
word = 'wind'

result = ap_is_controller.examples(word)
```

## Example Response *(as JSON)*

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


# Frequency

Expands upon the frequency score returned by the main /words/{word} endpoint. Returns zipf, a score indicating how common the word is in the English language, with a range of 1 to 7; per Million, the number of times the word is likely to appear in a corpus of one million English words; and diversity, a 0-1 scale the shows the likelihood of the word appearing in an English document that is part of a corpus.

```python
def frequency(self,
             word)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `string` | Template, Required | The word to search frequency for. |

## Response Type

[`FrequencyResponse`](../../doc/models/frequency-response.md)

## Example Usage

```python
word = 'lovely'

result = ap_is_controller.frequency(word)
```

## Example Response *(as JSON)*

```json
{
  "word": "wind",
  "frequency": {
    "zipf": 4.81,
    "perMillion": 64.22,
    "diversity": 0.2
  }
}
```

