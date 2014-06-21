#!/usr/bin/python


## ------------ Imports ----------- ##
try:
    import json
except:
    import simplejson as json

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
## ------------ Imports ----------- ##

## ------------ Relative Imports ----------- ##
from product import engine
## ------------ Relative Imports ----------- ##


def rpc_target():
    """."""
    engine = engine.Engine()


class XmlRpc(object):
    """."""
    def server(self, **kwargs):
        """."""
        hostname = kwargs.get('hostname')
        port = kwargs.get('port')

        if not hostname:
            raise Exception("Expecting value for keyword argument hostname")
        if not port:
            raise Exception("Expecting value for keyword argument port")

        server = SimpleXMLRPCServer((hostname, port))
        print "Listening on port {0}...".format(port)
        server.register_function(rpc_target, "rpc_target")
        server.serve_forever()

    def client(self, remote_args, **kwargs):
        """."""
        hostname = kwargs.get('hostname')
        port = kwargs.get('port')

        if not hostname:
            raise Exception("Expecting value for keyword argument hostname")
        if not port:
            raise Exception("Expecting value for keyword argument port")

        _server = xmlrpclib.ServerProxy("http://{0}:{1}/".format(hostname, port))
        return _server.rpc_target(json.dumps(remote_args))


if __name__ == '__main__':
    """This Bolck is used for Unit Test.
    """
    pass
