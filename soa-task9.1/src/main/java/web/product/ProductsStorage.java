package web.product;

import web.category.CategoriesStorage;

import java.util.*;

public class ProductsStorage {
    public static Map<Integer, Product> items = new HashMap<Integer, Product>();

    public static void init() {
        Set<Integer> categories = CategoriesStorage.items.keySet();
        List<Integer> lstArray = new ArrayList<Integer>();
        lstArray.addAll(categories);

        for (int i = 1; i <= 100; i++) {
            Product product = new Product();
            product.product_id = i;
            product.name = "Product " + product.product_id;
            product.description = "Description for " + product.name;
            Double randomNumber = Math.random();
            product.price = Math.round(randomNumber * 100.0 * i * 100.0) / 100.0;
            Integer arrayLength = lstArray.size();
            Integer randomIndex = (int) (randomNumber * (arrayLength - 1));
            product.stock = (int) (10 / randomNumber) * randomIndex;
            product.category_id = lstArray.get(randomIndex);
            ProductsStorage.items.put(product.product_id, product);
        }
    }
}
