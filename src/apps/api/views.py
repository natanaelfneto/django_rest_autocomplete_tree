# -*- coding: utf-8 -*-
# python imports
import csv
# django imports
from django.conf import settings
from django.shortcuts import render
# third party imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pytrie import SortedStringTrie as Trie


# Patinets class instance for csv values
class Patients:

    # initalize Patient instance
    def __init__(self, csv_file):
        """
        """

        # create a sorted string trie object instance
        trie=Trie()

        # open csv file
        with open(csv_file, 'r') as f:

            # read csv file
            reader = csv.reader(f)

            # loop for each row in csv file
            for index, row in enumerate(reader):

                # add row with patient name to trie object
                trie[''.join(row)] = index

        # 
        self.trie = trie
    
    # create a suggestion object filter for patients, parsing the query argument
    def suggestions(self, query):
        """
        """

        # 
        return { 'patients': self.trie.keys(prefix=query) }
        

# 
@api_view(['GET'])
def patient_suggestios(request, query):
    """
    
    """

    # check for GET method request
    if request.method == 'GET':

        # get csv file path
        csv_file = settings.PATIENTS

        # create a trie object for csv file
        patients = Patients(csv_file)

        # get suggestions for patients based on query
        suggestions = patients.suggestions(query)

        # return filtered suggesttions
        return Response(suggestions)