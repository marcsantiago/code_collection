package org.cadenhead.ecommerce;

public class Item implements Comparable {
    private String id;      // Private class variables
    private String name;
    private double retail;
    private int quantity;
    private double price;
     private boolean noDiscount;
    
    Item(String idIn, String nameIn, String retailIn, String quanIn, String discountIn) {
        id = idIn;
        name = nameIn;
        retail = Double.parseDouble(retailIn); //parse double was used to convert double into a string
        quantity = Integer.parseInt(quanIn);
        
        if (discountIn.equals("TRUE")) {
            noDiscount = true;
        }
        else {
            noDiscount = false;
        }
        
        if (quantity > 400) {
            price = retail * .5D;
        }
        else if (quantity > 200) {
            price = retail * .6D;
        }
        else {
            price = retail * .7D;
        }
        price = Math.floor(price * 100 + .5) / 100;
        
    }
    
    @Override
    public int compareTo(Object obj) {
        Item temp = (Item)obj;      //object
        if(this.price < temp.price) {       //this refers to item clas
            return 1;
        }
        else if (this.price > temp.price) {
            return -1;
        }
        return 0;
    }
    //Accesors
    public String getId() {
        return id;
    }
    
    public String getName() {
        return name;
    }
    public double getRetail() {
        return retail;
    }
    
    public int getQuantity() {
        return quantity;
    }
    
    public double getPrice() {
        return price;
    }
}

