class Clay {
 
   
    public static void main(String[] arguments){
    Clay st = new Clay();
    int number = 1;
    
    try {
        
        System.out.println("Enter a number: " + number);
    } catch(Exception e){
        
        if(number == 0) {
            System.out.println("Thank you for entering the right number");
        }
        else {
            System.out.println("Error");
        }
        
        
        }
    }
}
        
  
    