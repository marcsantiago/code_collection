package org.cadenhead.ecommerce;
import java.util.*;

public class Storefront {
    
    private LinkedList catalog = new LinkedList();
    
    /**
     *
     * @param id
     * @param name
     * @param price
     * @param quant
     */
    public void addItem(String id, String name, String price, String quant, String discountIn, String discount) {
        
        Item it = new Item (id, name, price, quant, discount);
        catalog.add(it);
    }
    
    public Item getItem(int i) {
        return (Item)catalog.get(i); 
    }
    
    public int getSize() {
        return catalog.size();
    }
    public void sort() {
    Collections.sort(catalog);
    }

    void addItem(String c01, String muG, String 99, String 50, String false) {
        throw new UnsupportedOperationException("Not yet implemented");
    }
    
}
