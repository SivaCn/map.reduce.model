#!/usr/bin/python

#coding: utf-8

import bottle
from products import engine


@bottle.route('/')
@bottle.route('/index.html')
def index():
    import pdb; pdb.set_trace()
    return '<h1>Go to Hello World page</h1>'

@bottle.route('/service')
def webservice():
    """."""
    return {'response': True}

def main():

    ## configs.
    hostname = "0.0.0.0"

    # Enabble Debugging for bottle Framework.
    bottle.debug(True)

    ## ## Start the XML-RPC Server and serve it forever.
    ## engine.while_start(hostname=hostname, port=8585)

    ## Start the WSGi web server and start listen to the
    ## on comming http requests.
    bottle.run(host=hostname, port=80, reloader=True)

if __name__ == "__main__":
    main()
