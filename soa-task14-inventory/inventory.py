import json
import requests
import time
import xml.etree.ElementTree as ET
import pprint

def main(json_data):
    """
    Entry point.
    """
    backend = MoySkladJSONAPI()
    op = json_data['operation']
    data = {
        'order_id': json_data['order_id'],
        'department': json_data['department'],
        'report_department': 'inventory',
        'message': op + 'd for order ' + json_data['order_id']
    }

    if op == 'increase':
        backend.enter_items(json_data['items'])
        print 'increased'
    elif op == 'decrease':
        current_stock = {}
        # Check stock.
        for item in json_data['items']:
            stock_item = backend.get_stock_for_product(item['sku'])
            if stock_item:
                current_stock[item['sku']] = stock_item['stock']
            else:
                data['store_status'] = 'error'
                data['error'] = 'Item is out of stock'
                data['error_item'] = item['sku']
                data['message'] = 'Order ' + json_data['order_id'] + ' One or more items are out of stock.'
                return json.dumps(data)

        backend.decrease_items(json_data['order_id'], json_data['items'])
        print 'decreased'
    data['store_status'] = op + 'd'
    data['message'] = op + 'd for order ' + json_data['order_id']
    return json.dumps(data)


class MoySkladJSONAPI:
    base_url = 'https://online.moysklad.ru/api/remap/1.1'
    base_url_old = 'https://online.moysklad.ru/exchange/rest/ms/xml/'
    auth = ('admin@soakubsu', 'aa176f2c70')

    def __init__(self):
        # Get data to create stock decrease with right document.
        params = {'limit': 1}
        response = {
            'organization': requests.get(self.base_url + '/entity/organization', auth=self.auth, params=params),
            'counterparty': requests.get(self.base_url + '/entity/counterparty', auth=self.auth, params=params),
            'store': requests.get(self.base_url + '/entity/store', auth=self.auth, params=params)
        }
        data = {}
        for key, entity in response.iteritems():
            entity = json.loads(entity.text)
            data[key] = entity['rows'][0]['meta']
            data[key]['id'] = entity['rows'][0]['id']

        # Cache metadata.
        self.organization_meta = data['organization']
        self.counterparty_meta = data['counterparty']
        self.store_meta = data['store']

    def get_stock_for_product(self, uuid):
        params = {'product.id': uuid}
        response = requests.get(self.base_url + '/report/stock/all', auth=self.auth, params=params)
        data = json.loads(response.text)
        if len(data['rows']):
            return {
                'name': data['rows'][0]['name'],
                'stock': data['rows'][0]['stock'],
            }
        return False

    def decrease_items(self, order_id, items):
        headers = {'content-type': 'application/json'}
        data = {
            'name': 'Order demand ' + order_id + ' time ' + str(time.time()),
            'organization': {'meta': self.organization_meta},
            'agent': {'meta': self.counterparty_meta},
            'store': {'meta': self.store_meta},
        }
        response = requests.post(self.base_url + '/entity/demand', auth=self.auth, headers=headers,
                                 data=json.dumps(data))
        demand = json.loads(response.text)
        demand_id = demand['id']
        data = []
        for item in items:
            data.append({
                'quantity': item['qty'],
                'assortment': {
                    'meta': {
                        'href': self.base_url + '/entity/product/' + item['sku'],
                        'type': 'product',
                        'mediaType': 'application/json',
                    }
                }
            })
        response = requests.post(self.base_url + '/entity/demand/' + demand_id + '/positions', auth=self.auth,
                                 headers=headers, data=json.dumps(data))
        return True

    def enter_items(self, items):
        headers = {'content-type': 'application/xml'}
        good_ids_map = {}
        # Map ids to old api.
        for item in items:
            response = requests.get(self.base_url_old + '/Consignment/' + item['sku'], auth=self.auth)
            root = ET.fromstring(response.text.encode('utf-8'))
            good_ids_map[item['sku']] = root.attrib['goodUuid']

        # Create xml to increase stock.
        root = ET.Element('collection')
        enter = ET.SubElement(root, 'enter')
        enter.set('targetAgentUuid', self.counterparty_meta['id'])
        enter.set('targetStoreUuid', self.store_meta['id'])
        enter.set('applicable', 'true')
        for item in items:
            enter_position = ET.SubElement(enter, 'enterPosition')
            enter_position.set('quantity', str(item['qty']))
            enter_position.set('consignmentUuid', item['sku'])
            enter_position.set('goodUuid', good_ids_map[item['sku']])

        # Get xml string and send to MoySklad.
        xml = ET.tostring(root)
        response = requests.put(self.base_url_old + '/Enter/list/update', auth=self.auth, headers=headers, data=xml)
        return True


# Entry point.
# Check payload for development purposes.
try:
    # JSON is expected.
    payload = payload
except NameError:
    # The script is not running in Mule env.
    # Use test json file.
    with open('test.json') as data_file:
        payload = json.load(data_file)
else:
    # Parse incoming data.
    payload = json.loads(payload)

# Mule Studio expects "result" variable.
result = main(payload)
