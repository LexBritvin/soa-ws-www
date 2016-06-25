## Inventory system

Track inventory and provide reports to Data Warhouse System.

This is project for university subject.

## Предоставляемые ресурсы

### Общее описание

Веб-сервис представляет собой прокси к API МойСклад.

### Список ресурсов

**POST** */store* - Запрос на списание или добавление товара на склад.<br>

Запрос на списание производится операцией decrease, а добавление с помощью increase.
Артикул товара должен соответствовать uuid товара на складе.

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

Ответ:
```
{
  "order_id": "123",
  "store_status": "decreased"
  "message": "Successfully decreased."
}
```
Пример ошибки списания:
```
{
  "order_id": "123",
  "store_status": "error",
  "message": "Item is out of stock."
}
```
