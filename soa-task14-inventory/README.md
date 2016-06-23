# Описание структур данных

## Статусы заказов
1. pending (Тымчук)
2. payed (Андрейчук)
3. assigned (Коробков)
4. processing (Баранова)
5. compiled (Баранова)
6. completed (Глебов)
7. shipped (Бутусов)
8. canceled (Коробков, Тымчук)

## Очереди

1. Orders - содержит информацию о созданном заказе. Появляется только при начале заказа.
2. Users - содержит информацию о новом пользователе. Появляется только при регистрации пользователя.
3. OrderStatus - содержит информацию об изменении статуса заказа. Сообщение появляется и рассылается всем при изменении
статуса заказа. Может быть расширен информацией специфичной для каждого узла.
4. ReportDataWarehouse - используется для отправки отчётов на DataWarehouse. Появляется при совершении действия какой-либо системой
5. RequestStock - используется, когда какой-либо системе необходимо снять товар со склада
6. ResponseStock - ответ склада о списанном товаре. (Не используется)

## Примеры структуры данных для очередей

### Orders

```
{

    "order_number":"17",
    "revision_uid":"1",
    "mail":"timchuck.andrey2011@yandex.ru",
    "status":"pending",
    "log":"Order state updated via Rules.",
    "revision_timestamp":1466699378,
    "revision_hostname":"127.0.0.1",
    "data":{
        "last_cart_refresh":1466699377,
        "products":[
            {
                "product_id":"7",
                "sku":"6b3e5534-3616-11e6-7a69-971100217953",
                "title":"Чехол для телефона",
                "price":{
                    "amount":"100000",
                    "currency_code":"USD"
                },
                "quantity":"7.00",
            },
            {
                "product_id":"5",
                "sku":"1fd686aa-3616-11e6-7a69-93a70015e25f",
                "title":"Болт",
                "price":{
                    "amount":"500",
                    "currency_code":"USD"
                },
                "quantity":"1.00",
            }
        ],
        "delivery":{
            "country":"RU",
            "address":"Adres",
            "city":"City",
            "postcode":"123789"
        }
    },
    "order_id":"17",
    "type":"commerce_order",
    "uid":"1",
    "created":1466699378,
    "changed":1466699378,
    "hostname":"127.0.0.1",
    "commerce_line_items":{
        "und":[
            {
                "line_item_id":"20"
            },
            {
                "line_item_id":"21"
            }
        ]
    },
    "commerce_order_total":{
        "und":[
            {
                "amount":100500,
                "currency_code":"USD",
                "data":{
                    "components":[
                        {
                            "name":"base_price",
                            "price":{
                                "amount":100500,
                                "currency_code":"USD",
                                "data":[
                                ]
                            },
                            "included":true
                        }
                    ]
                }
            }
        ]
    },
    "commerce_customer_billing":{
        "und":[
            {
                "profile_id":"17"
            }
        ]
    },
    "rdf_mapping":[
    ],
    "old_revision_id":"133",
    "revision_id":"134"
}
```

### Users

```
{
    "uid":"118",
    "name":"eryery",
    "pass":"$S$DB58VyFrd1w/p.6FwDGQzsS8aeSOzF7gW3Ngm5cm/lr6UkfelTc5",
    "mail":"andrey@test.ru",
    "theme":"",
    "signature":"",
    "signature_format":"filtered_html",
    "created":"1466456962",
    "access":"0",
    "login":"0",
    "status":"1",
    "timezone":"Europe/Moscow",
    "language":"ru",
    "picture":null,
    "init":"andrey@test.ru",
    "data":false,
    "roles":{
        "2":"authenticated user"
    },
    "bus_tickets_field":[
    ],
    "rdf_mapping":{
        "rdftype":[
            "sioc:UserAccount"
        ],
        "name":{
            "predicates":[
                "foaf:name"
            ]
        },
        "homepage":{
            "predicates":[
                "foaf:page"
            ],
            "type":"rel"
        }
    }
}
```

### OrderStatus

```
{
    "order_id": "123",
    "status": "pending"
}
```

### RequestStock

```
{
  "order_id": "1",
  "operation": "decrease",
  "department": "erp",
  "items": [
    {
      "product_id": "1",
      "sku": "17f369b8-3616-11e6-7a69-93a70015e207",
      "qty": 10
    },
    {
      "product_id": "2",
      "sku": "1fd686aa-3616-11e6-7a69-93a70015e25f",
      "qty": 15
    },
    {
      "product_id": "3",
      "sku": "45e94931-3616-11e6-7a69-93a70015e3af",
      "qty": 20
    },
    {
      "product_id": "4",
      "sku": "6b3e5534-3616-11e6-7a69-971100217953",
      "qty": 25
    }
  ]
}
```

### ReportDataWarehouse

Департамент - машинное имя департамента каждой системы, отправляющей отчёт.

1. website - Corporate Web Site (Тымчук)
2. accounting - Accounting System (Андрейчук)
3. oms - Order Management System (Коробков)
4. erp - ERP System (Глебов)
5. intranet - Intranet Web Portal (Баранова)
6. inventory - Inventory System (Бритвин)
7. shipping - Shipping System (Бутусов)
8. crm - Customer Resource Management System (Бушков)
9. marketing - Marketing system (Литвинов)

```
{
	"order_id": "123",
	"department": "department",
	"message": "message"
}
```
