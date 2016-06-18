package web.common;

public class RestURIConstants {

    public static final String GET_PRODUCT = "/rest/product/{product_id}";
    public static final String GET_ALL_PRODUCTS_IN_CATEGORY = "/rest/products/{category_id}";

    public static final String GET_CATEGORIES = "/rest/categories";
    public static final String GET_CATEGORY_CHILDREN = "/rest/categories/{parent_id}";

    public static final String GET_ORDERS = "/rest/orders";
    public static final String CREATE_ORDER = "/rest/orders";
    public static final String GET_ORDER = "/rest/order/{order_id}";

}
