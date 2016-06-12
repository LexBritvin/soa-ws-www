<?php

$config = [
  'url' => 'http://localhost:8080/drupal7/soap',
  'username' => 'superuser',
  'password' => '123',
];

$client = new SoapClient($config['url'] . '?wsdl', [
  'login' => "superuser",
  'password' => "123",
]);

print_r($client->__getFunctions());

// This doesn't work in Drupal 7 SOAP Server.
// Create node.
//$response = $client->node_soap_create(new ArrayObject([
//  'type' => 'article',
//  'status' => 1,
//  'title' => 'Remote Test ' . time(),
//  'body' => 'This is a test created from a remote app',
//]));
//print_r($response);

// List nodes.
$response = $client->node_soap_index(1, 'nid', [], 5);
print_r($response);

$nodes = $response ? reset($response) : FALSE;
$nodes = $nodes && !is_array($nodes) ? [$nodes] : $nodes;
if ($nodes) {
  // Delete the first node.
  $nid = reset($nodes)->nid;
  $response = $client->node_soap_delete(intval($nid));
  var_dump($response);
  print $nid;
}
