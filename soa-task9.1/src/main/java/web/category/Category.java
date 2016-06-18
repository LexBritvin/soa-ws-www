package web.category;

import web.common.RestURIConstants;

public class Category {
    public int category_id;
    public String name;
    public Integer parent_id = 0;

    public int getCategory_id() {
        return category_id;
    }

    public String getName() {
        return name;
    }

    public int getParent_id() {
        return parent_id;
    }

    public String getUrl() {
        return RestURIConstants.GET_CATEGORY_CHILDREN.replace("{parent_id}", Integer.toString(category_id));
    }

}
