package web.category;

import java.util.HashMap;
import java.util.Map;

public class CategoriesStorage {
    public static Map<Integer, Category> items = new HashMap<Integer, Category>();

    public static void init() {
        for (int i = 10; i <= 50; i += 10) {
            Category category = new Category();
            category.category_id = i;
            category.name = "Category " + category.category_id;
            items.put(category.category_id, category);
            for (int j = 1; j <= 5; j++) {
                category = new Category();
                category.category_id = i + j;
                category.name = "Category " + category.category_id;
                category.parent_id = i;
                items.put(category.category_id, category);
            }
        }
    }
}
