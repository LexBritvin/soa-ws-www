package web.order;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import web.common.*;
import web.product.Product;
import web.product.ProductsStorage;

import java.security.Principal;
import java.util.ArrayList;
import java.util.List;

@Controller
public class OrdersController {

    private List<Order> ordersData = new ArrayList<Order>();

    @RequestMapping(value = RestURIConstants.GET_ORDERS, method = RequestMethod.GET)
    public
    @ResponseBody
    List<Order> getOrders(Principal principal) {
        List<Order> orders = new ArrayList<Order>();
        String username = principal.getName();
        for (Order order : ordersData) {
            if (order.user.equals(username)) {
                orders.add(order);
            }
        }
        return orders;
    }

    @RequestMapping(value = RestURIConstants.GET_ORDER, method = RequestMethod.GET)
    public
    @ResponseBody
    Order getOrder(Principal principal, @PathVariable("order_id") int orderId) {
        Order order = this.ordersData.get(orderId);
        if (order == null) {
            throw new ResourceNotFoundException();
        }
        String username = principal.getName();
        if (!order.user.equals(username)) {
            throw new ResourceForbiddenException();
        }
        return order;
    }

    @RequestMapping(value = RestURIConstants.CREATE_ORDER, method = RequestMethod.POST)
    public final String createOrder(Principal principal, @RequestBody Order order) {
        for (LineItem lineItem: order.lineItems) {
            Product product = ProductsStorage.items.get(lineItem.product_id);
            if (product == null) {
                throw new ResourceUnprocessableEntityException();
            }
            lineItem.price = product.price;
        }
        order.created = System.currentTimeMillis() / 1000L;
        order.status = "Pending";
        order.user = principal.getName();
        ordersData.add(order);
        order.order_id = ordersData.size() - 1;
        return "redirect:" + RestURIConstants.GET_ORDER.replace("{order_id}", Integer.toString(order.order_id));
    }

}
