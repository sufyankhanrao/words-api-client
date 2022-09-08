# -*- coding: utf-8 -*-

"""
wordsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from wordsapi.api_helper import APIHelper
from wordsapi.configuration import Server
from wordsapi.controllers.base_controller import BaseController
from wordsapi.models.synonyms_response import SynonymsResponse
from wordsapi.models.definitions_response import DefinitionsResponse
from wordsapi.models.pronunciation_response import PronunciationResponse
from wordsapi.models.word_response import WordResponse
from wordsapi.models.examples_response import ExamplesResponse
from wordsapi.models.frequency_response import FrequencyResponse


class APIsController(BaseController):

    """A Controller to access Endpoints in the wordsapi API."""
    def __init__(self, config, auth_managers):
        super(APIsController, self).__init__(config, auth_managers)

    def synonyms(self,
                 word):
        """Does a GET request to /words/{word}/synonyms.

        Get synonyms of a word.

        Args:
            word (string): The word to search synonyms for.

        Returns:
            SynonymsResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/words/{word}/synonyms'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'word': {'value': word, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, SynonymsResponse.from_dictionary)

        return decoded

    def definitions(self,
                    word):
        """Does a GET request to /words/{word}/definitions.

        Get definitions of a word, including the part of speech.

        Args:
            word (string): The word to search the definitions for.

        Returns:
            DefinitionsResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/words/{word}/definitions'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'word': {'value': word, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, DefinitionsResponse.from_dictionary)

        return decoded

    def pronunciation(self,
                      word):
        """Does a GET request to /words/{word}/pronunciation.

        How to pronounce a word, according to the International Phonetic
        Alphabet. May include multiple results if the word is pronounced
        differently depending on its part of speech.

        Args:
            word (string): The word to search pronunciation for.

        Returns:
            PronunciationResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/words/{word}/pronunciation'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'word': {'value': word, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, PronunciationResponse.from_dictionary)

        return decoded

    def word(self,
             word):
        """Does a GET request to /words/{word}.

        Retrieve information about a word. Results can include definitions,
        part of speech, synonyms, related words, syllables, and pronunciation.
        This method is useful to see which relationships are attached to which
        definition and part of speech of a word.

        Args:
            word (string): This is a template parameter that is used to
                provide the word, about which the information is being
                fetched.

        Returns:
            WordResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/words/{word}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'word': {'value': word, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, WordResponse.from_dictionary)

        return decoded

    def examples(self,
                 word):
        """Does a GET request to /words/{word}/examples.

        Get examples of how the word is used.

        Args:
            word (string): The word to search the examples for.

        Returns:
            ExamplesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/words/{word}/examples'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'word': {'value': word, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ExamplesResponse.from_dictionary)

        return decoded

    def frequency(self,
                  word):
        """Does a GET request to /words/{word}/frequency.

        Expands upon the frequency score returned by the main /words/{word}
        endpoint. Returns zipf, a score indicating how common the word is in
        the English language, with a range of 1 to 7; per Million, the number
        of times the word is likely to appear in a corpus of one million
        English words; and diversity, a 0-1 scale the shows the likelihood of
        the word appearing in an English document that is part of a corpus.

        Args:
            word (string): The word to search frequency for.

        Returns:
            FrequencyResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/words/{word}/frequency'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'word': {'value': word, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, FrequencyResponse.from_dictionary)

        return decoded