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

// This doesn't work in Drupal 7.
//$response = $client->node_soap_create(new ArrayObject([
//  'type' => 'article',
//  'status' => 1,
//  'title' => 'Remote Test ' . time(),
//  'body' => 'This is a test created from a remote app',
//]));
//print_r($response);

$response = $client->node_soap_index(1, 'nid', []);
print_r($response);

$nodes = $response ? reset($response) : FALSE;
$nodes = $nodes && !is_array($nodes) ? [$nodes] : $nodes;
if ($nodes) {
  $nid = reset($nodes)->nid;
  $response = $client->node_soap_delete(intval($nid));
  var_dump($response);
  print $nid;
}
