# Как запустить

Это обычное Java приложение.
Чтобы запустить, нужно собрать проект с главным классом Application, он и содержить функцию main.
После запуска развернётся сервер Jetty на localhost:8080.

Для проверки сервиса я использую расширение для хрома Postman.

## POST /login
Чтобы залогиниться, нужно отправить POST запрос на http://localhost:8080/login.
Запрос должен содержать x-www-form-urlencoded поля:
```
username=user&password=user
```
Тело запроса пустое.

ПРи успешном логине выдаётся кука со значением сессии.

## POST /logout
POST запрос с пустым телом.

## GET /rest/categories

Возвращает все категории без родителей.

Я генерирую 10, 20, 30 итд

## GET /rest/categories/10

Возвращает всех детей категории с id 10.

Дети 11-15, 21-25 и т.д.

## GET /rest/products/10

Возращает все товары в категории 10.

## GET /rest/product/5

Возращает описание товара.

## GET /rest/orders

Возвращает все заказы текущего пользователя.

## GET /rest/order/2

Вернёт описание заказа 2

## POST /rest/orders

Создаёт новый заказ.
После создание редиректит на /rest/order/{order_id}

Header:
```
Content-Type: application/json
```
Body:
```
{
    "firstName": "first",
    "lastName": "last",
    "email": "test@example.com",
    "lineItems": [{
        "product_id": 45,
        "qty": 14
    },
    {
        "product_id": 84,
        "qty": 7
    },
    {
        "product_id": 12,
        "qty": 1
    },
    {
        "product_id": 15,
        "qty": 4
    }]
}

```