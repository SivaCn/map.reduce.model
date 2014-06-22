#! /usr/bin/python

# -*- coding: utf-8 -*-


## ---------- Import Section ---------- ##
try:
    import json
except ImportError:
    import simplejson as json

import httplib
from urllib2 import urlopen
from urlparse import urlparse
## ---------- Import Section ---------- ##

__all__ = ['Service'] # Exposed classes or methods.


class CodeUrl(object):
    """Static url mapper of reader which reads from the configs
    and returns the mapped url for any given webservice."""

    def map_url(self, key, hostname):
        """Returns the target webservice url by providing the short url.
        """
        return {
                'bottle': r'http://{0}/service',
                }.get(key, None).format(hostname)


class Url(object):
    """An Interface class to URL related inspections.
    """
    def exists(self, _url):
        """Check the existance of any URL with path.
        """
        url_obj = urlopen( _url )
        return url_obj.getcode() == 200

class Service(Url, CodeUrl):
    """Web Services class to make GET or POST calls to the webservice.
    """
    def __init__(self, url_key, hostname):
        """Initialization Block.
        """
        ## Validate the arguments.
        if not url_key:
            raise Exception("Unable to map the url key: {0}, which is not Valid".format(url_key))

        self.url = self.map_url(url_key, hostname)

        self.collected_values = []

    def __fragment_url(self, url):
        """Use this method for investigating the given url.
        """
        return urlparse(url)

    def __construct_url(self, **kwargs):
        """Constructs new url with the query string.
        """
        str_query = '&'.join( ["""{0}={1}""".format( key, value ) for key, value in kwargs.items()] )

        complete_url = """{0}?{1}""".format( self.url, str_query )

        return complete_url

    def __get_values_of_key(self, data, key):
        """Get all the values in the python complex datastructure

        if the @params: target_key is specified
        returns the specific values as a list
        else
        returns the entire python or json data.
        """
        if data:
            if isinstance(data, dict):
                if key in data:
                    self.collected_values.append(data[key])
                else:
                    for eachkey in data:
                        self.__get_values_of_key(data[eachkey], key)
            if isinstance(data, list):
                for ele in data:
                    self.__get_values_of_key(ele, key)

    def get(self, target_key='', **kwargs):
        """An Exposed method to call the webservice
        and get the interested data."""
        complete_url = self.__construct_url(**kwargs)

        print complete_url

        if not self.exists( complete_url ):
            raise Exception("Specified URL: {0} does not exist".format( complete_url ))

        response = urlopen( complete_url ).read()

        python_data = json.loads( response )

        if target_key:
            ## this call populates the collected data to self.collected_values as list.
            self.__get_values_of_key( python_data, target_key )

        return self.collected_values if self.collected_values else python_data

    def post(self, **params):
        """An adapter method for the POST to the webservices.
        """
        pass

if __name__ == '__main__':
    """Used for unit testing.
    """
    params = {}

    hostname = "192.168.0.2"
    obj = Service('site1', hostname)

    from pprint import pprint as pp
    pp( obj.get(target_key='medCondProfessional', **params) )
