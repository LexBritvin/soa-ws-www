package web.product;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import web.common.ResourceNotFoundException;
import web.common.RestURIConstants;

import java.util.ArrayList;
import java.util.List;

@Controller
public class ProductsController {

    @RequestMapping(value = RestURIConstants.GET_PRODUCT, method = RequestMethod.GET)
    public
    @ResponseBody
    Product getProduct(@PathVariable("product_id") int productId) {
        Product product = ProductsStorage.items.get(productId);
        if (product == null) {
            throw new ResourceNotFoundException();
        }
        return ProductsStorage.items.get(productId);
    }

    @RequestMapping(value = RestURIConstants.GET_ALL_PRODUCTS_IN_CATEGORY, method = RequestMethod.GET)
    public
    @ResponseBody
    List<Product> getProductsInCategory(@PathVariable("category_id") int categoryId) {
        List<Product> products = new ArrayList<Product>();
        for (Integer i : ProductsStorage.items.keySet()) {
            Product product = ProductsStorage.items.get(i);
            if (product.category_id == categoryId) {
                products.add(product);
            }
        }
        return products;
    }

}