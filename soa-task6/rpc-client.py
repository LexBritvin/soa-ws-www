import pprint
import xmlrpclib

import time

pp = pprint.PrettyPrinter()
config = {
    'url': 'http://localhost:8080/drupal7/xmlrpc',
    'username': 'superuser',
    'password': '123',
}

session_info = (None, None)
token = None

class CookieAwareTransport(xmlrpclib.Transport):
    def send_content(self, connection, request_body):

        if session_info[0]:
            cookie = "%s=%s;" % session_info
            connection.putheader('Cookie', cookie)
            print "Added a cookie header: %s" % (cookie)

        if token:
            connection.putheader('X-Csrf-Token', token)
            print "Added a token header: %s" % token

        xmlrpclib.Transport.send_content(self, connection, request_body)


# Make initial connection to service, then login as developer
server = xmlrpclib.ServerProxy(config['url'], transport=CookieAwareTransport())
connection = server.system.connect()
session = server.user.login(config['username'], config['password'])

session_info = (session['session_name'], session['sessid'])
token = server.user.token()['token']
user = session['user']

# Create the node object and reference the new fid just created
timestamp = str(int(time.time()))

node = {
    'type': 'article',
    'status': 1,
    'title': 'Remote Test ' + timestamp,
    'body': 'This is a test created from a remote app',
}

try:
    nodes = server.node.index()
    n = server.node.create(node)
    deleted = server.node.delete(n['nid'])

except xmlrpclib.Fault, err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString

else:
    pp.pprint(n)
    pp.pprint(nodes)
    pp.pprint(deleted)
