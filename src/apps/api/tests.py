# -*- coding: utf-8 -*-
# python imports
import csv
import random
import string
# django imports
from django.urls import reverse
# third party imports
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
# self imports
from .views import *


# Patient autocomplete api query test class
class PatientAPITest(APITestCase):

    def response(self, url_name, query):
        """
        DRY procedure for api request and response
        """

        # set example query value
        kwargs = { 'query': query }

        # set example query url 
        url = reverse(url_name, kwargs=kwargs)

        # get response from a client request
        return self.client.get(url, format='json')

    
    # query response value is 200?
    def test_request_status_value(self):
        """
        Ensure url get request return OK for an example valid request
        using single value for all alphabet possible entries.
        """

        # array with status code for all possible alphabet query entries with single char
        print('generating status code array')
        status_code_seq = [
            self.response('autocomplete', char).status_code for char in string.ascii_letters
        ]
    
        # assert response status
        assert all(status_code == status.HTTP_200_OK for status_code in status_code_seq)


    # query response data is a valid patient object?
    def test_expected_response(self):
        """
        Ensure query response data matches expected.
        """

        # get example response data
        data = self.response('autocomplete', 'lee').data
        
        # set expected data object
        expected_value = {
            "patients": [
                "lee chambers",
                "lee chavez",
                "lee clark",
                "lee hanson",
                "lee price",
                "leevi anttila",
                "leevi takala"
            ]
        }

        # assert response data
        self.assertEqual(data, expected_value)