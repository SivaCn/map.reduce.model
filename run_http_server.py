#!/usr/bin/python

#coding: utf-8

import bottle
from products import engine


@bottle.route('/')
@bottle.route('/index.html')
def index():
    import pdb; pdb.set_trace()
    return '<h1>Go to Hello World page</h1>'

def main():

    ## configs.
    hostname = "0.0.0.0"
    # Start the Bottle webapp
    bottle.debug(True)
    engine.while_start(hostname=hostname, port=8585)
    bottle.run(host=hostname, port=80, reloader=True)

if __name__ == "__main__":
    main()
