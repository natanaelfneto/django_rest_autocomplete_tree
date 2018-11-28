# -*- coding: utf-8 -*-
# python imports
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

    # basic response for api request
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


    # query response value is 200 for random query value?
    def test_single_request_status_value(self):
        """
        Ensure url get request return OK for an example valid request
        using single value for a single random alphabet possible entries.
        """

        # status code for random alphabet query entries with single char
        status_code = self.response('autocomplete', random.choice(string.ascii_letters)).status_code
        
        # assert response status
        self.assertEqual(status_code, status.HTTP_200_OK)


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