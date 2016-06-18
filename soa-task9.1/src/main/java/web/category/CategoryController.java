package web.category;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import web.common.RestURIConstants;

import java.util.ArrayList;
import java.util.List;

@Controller
public class CategoryController {

    @RequestMapping(value = RestURIConstants.GET_CATEGORY_CHILDREN, method = RequestMethod.GET)
    public
    @ResponseBody
    List<Category> getCategoryChildren(@PathVariable("parent_id") Integer parentId) {
        List<Category> categories = new ArrayList<Category>();
        for (Integer i : CategoriesStorage.items.keySet()) {
            Category category = CategoriesStorage.items.get(i);
            if (category.parent_id.equals(parentId)) {
                categories.add(category);
            }
        }
        return categories;
    }

    @RequestMapping(value = RestURIConstants.GET_CATEGORIES, method = RequestMethod.GET)
    public
    @ResponseBody
    List<Category> getCategories() {
        return this.getCategoryChildren(0);
    }

}