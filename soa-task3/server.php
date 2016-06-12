<?php

/**
 * @file
 * XMLRPC server.
 */

// The easiest way to read an XMLRPC request is through the input stream.
$request_xml = file_get_contents("php://input");

// Create a basic demo method for the server to use.
function say_hello($method_name, $args) {
  return "Hello " . $args[0];
}

// Create the XMLRPC server.
$xmlrpc_server = xmlrpc_server_create();

// Register the demo method to the XMLRPC server.
xmlrpc_server_register_method($xmlrpc_server, "say_hello", "say_hello");

// Start the server listener.
header('Content-Type: text/xml');
print xmlrpc_server_call_method($xmlrpc_server, $request_xml, array());
