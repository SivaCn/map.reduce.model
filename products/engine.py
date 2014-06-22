
import time
import bottle

from products.xmlrpc import XmlRpc


def base_initialize(func):
    """."""
    def wrapper():
        """."""
        XmlRpc().server()
        func()
    return wrapper


#@base_initialize
def while_start(**kwargs):
    """."""
    XmlRpc().server(**kwargs)
