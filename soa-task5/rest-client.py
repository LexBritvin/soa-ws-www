import json
import requests

base_url = "http://localhost:8080/drupal8"
auth = ('superuser', '123')
params = {'_format': 'hal_json'}


def get_value(drupal_field):
    return drupal_field[0][u'value']


def get_node(nid):
    headers = {'accept': 'application/hal+json'}
    response = requests.get(base_url + "/node/" + str(nid), auth=auth, params=params, headers=headers)
    return response


def create_node(data):
    headers = {'content-type': 'application/hal+json'}
    response = requests.post(base_url + "/entity/node", auth=auth, params=params, headers=headers,
                             data=json.dumps(data))
    return response


def delete_node(nid):
    headers = {'content-type': 'application/hal+json'}
    response = requests.delete(base_url + "/node/" + str(nid), auth=auth, params=params, headers=headers)
    return response


response = get_node(1)
print "Get node: \n"
if response.status_code == 200:
    node = json.loads(response.text)
    print "nid: ", get_value(node[u'nid'])
    print "Title: ", get_value(node[u'title'])
elif response.status_code == '404':
    print "No such node"
print "\n"

print "Create node: \n"
data = {
    "_links": {
        "type": {
            "href": base_url + "/rest/type/node/article"
        }
    },
    "title": [{
        "value": "My first page"
    }]
}
response = create_node(data)
created_nid = None
if response.status_code == 201:
    node = json.loads(response.text)
    created_nid = get_value(node[u'nid'])
    print "nid: ", get_value(node[u'nid'])
    print "Title: ", get_value(node[u'title'])

if created_nid:
    response = delete_node(created_nid)
    if response.status_code == 204:
        print 'Deleted nid', + created_nid
