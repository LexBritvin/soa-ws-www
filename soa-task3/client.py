import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8080/soa-task3/server.php")
print str(proxy.say_hello('Britvin'))
