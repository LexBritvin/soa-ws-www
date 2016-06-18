package web.order;

import web.common.RestURIConstants;

import java.util.List;

public class Order {
    public int order_id;
    public String firstName;
    public String lastName;
    public String email;
    public long created;
    public String status;
    public List<LineItem> lineItems;
    public String user;

    public int getOrder_id() {
        return order_id;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getEmail() {
        return email;
    }

    public long getCreated() {
        return created;
    }

    public String getStatus() {
        return status;
    }

    public double getTotal() {
        double total = 0;
        for (LineItem lineItem : this.lineItems) {
            total += lineItem.price * lineItem.qty;
        }
        return total;
    }

    public List<LineItem> getLineItems() {
        return lineItems;
    }

    public String getUrl() {
        return RestURIConstants.GET_ORDER.replace("{order_id}", Integer.toString(this.order_id));
    }
}
