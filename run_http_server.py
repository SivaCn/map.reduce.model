#!/usr/bin/python

#coding: utf-8

import bottle


@bottle.route('/')
@bottle.route('/index.html')
def index():
    return '<h1>Go to Hello World page</h1>'

def main():

    # Start the Bottle webapp
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=80, reloader=True)

if __name__ == "__main__":
    main()
