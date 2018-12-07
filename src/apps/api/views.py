# -*- coding: utf-8 -*-
# python imports
import csv
import sortedcontainers
from collections import MutableMapping
# django imports
from django.conf import settings
from django.shortcuts import render
# third party imports
from rest_framework.decorators import api_view
from rest_framework.response import Response


# helper function for iteration on get_items
def __iter__(dictionary):
    """
    Helper function for self iteration on get_items

    Argument(s):
        dictionary: dictionary containing parts to be iterated
    """

    if hasattr(dictionary, 'get_items'):

        # return self iteration
        return dictionary.__iter__()

    # return value of iterated items
    return dictionary.items()


# pass for ~null~ value on instance functions
class NULL(object):
    """
    Instancieate a NULL object for node values that are valid but not interesting
    """
    pass


# Node object for a Tree
class Node(object):
    """
    Instance of tree node
    """

    # 
    def __init__(self, value=NULL):
        """
        Initialize instance of class

        Argument(s):
            value: An object for value, or ~NULL~
        """
        self.value = value
        self.children = sortedcontainers.SortedDict()


# Tree class instance for mapped dictionary
class Tree(MutableMapping):
    """
    Tree instance class
    """

    # Node object
    _Node = Node

    # initialize Tree instance
    def __init__(self, *args, **kwargs):
        """
        Initialize instance of class
        """
        self._root = self._Node()
        self.update(*args, **kwargs)

    # get items for query
    def get_items(self, query=None):
        """
        Return an iterator over Keys and Values for searched keys, including valid complete values and partial valid values
        If query not None, yield only the values associated with keys

        Argument(s):
            query: A string with one or more letters to be parsed as substring of names. 
        """
        # array for query parts
        parts = []

        # yeald values for node query parts
        def make(node, parts=parts, null=NULL):
            """
            Subfunction to make the iterator

            Argument(s):
                node: An associated node for value check
                parts: The parts to be append/removed 
                null: An object for value ~NULL~
            """

            # generate a value if not NULL
            if node.value is not null:
                yield (tuple(parts), node.value)
            # for each part, generate a value
            for part, child in __iter__(node.children):
                parts.append(part)
                # generate a value for each child
                for subresult in make(child):
                    yield subresult
                # remove last part
                del parts[-1]

        # set root as node object's root
        root = self._root

        # if query not none
        if query is not None:
            # for each part in query inputed
            for part in query:
                # appen this part
                parts.append(part)
                # update root with found children for part
                root = root.children.get(part)
                # check if any were found
                if root is None:
                    # return node
                    root = self._Node()
                    # and break loop
                    break

        # return loop make for node root
        return make(root)

    # get keys for query
    def get_keys(self, query=None):
        """
        Funtion to get all valid interesting results for tree search
        and convert list of parts into string for each key

        Argument(s):
            query: A string with one or more letters to be parsed as substring of names
        """

        # return list of keys
        return list((''.join(key) for key, value in self.get_items(query)))

    # set self value of item
    def __setitem__(self, key, value):
        """
        Called to implement assignment to self[key].
        This should only be implemented for mappings if the objects support changes to the values for keys,
        or if new keys can be added, or for sequences if elements can be replaced.

        Argument(s):
            key: key to self[key] assignment
            value: new value to self[key] = value
        """

        # set node as node object's root
        node = self._root
        # set factory as node object class instance
        factory = self._Node
        # for each part of key
        for part in key:
            # set next node
            next_node = node.children.get(part)
            # set node based on next node value
            node = node.children.setdefault(part, factory()) if next_node is None else next_node
        # update node value
        node.value = value

    # future implemenation
    def __delitem__(self):
        """Obrigatory due to class inheritance"""
        return

    # future implemenation
    def __getitem__(self):
        """Obrigatory due to class inheritance"""
        return

    # future implemenation
    def __iter__(self):
        """Obrigatory due to class inheritance"""
        return
    
    # future implemenation
    def __len__(self):
        """Obrigatory due to class inheritance"""
        return


# Patinets class instance for csv values
class Patients:

    # initalize Patient instance
    def __init__(self, csv_file):
        """
        Initialize instance of class

        Argument(s): 
            csv_file: A string with path to a file
        """

        # create a sorted string trie object instance
        tree=Tree()

        # open csv file
        with open(csv_file, 'r') as f:

            # read csv file
            reader = csv.reader(f)

            # loop for each row in csv file
            for index, row in enumerate(reader):

                # add row with patient name to trie object
                tree[''.join(row)] = index

        # add trie value to self
        self.tree = tree
    
    # create a suggestion object filter for patients, parsing the query argument
    def suggestions(self, query):
        """
        Create and array of sugestions based on query

        Argument(s):
            query: A string with one or more letters to be parsed as substring of names
        """

        # return array of suggestions for patients names
        return { 'patients': self.tree.get_keys(query=query) }
        

# rest framework api view
@api_view(['GET'])
def patient_suggestios(request, query):
    """
    Parses queries to be checked as substrings of patients names within tree structure

    Argument(s):
        request: A string representing the scheme of the request (http or https usually)
        query: A string with one or more letters to be parsed as substring of names
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