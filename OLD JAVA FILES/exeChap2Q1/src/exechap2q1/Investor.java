public class Investor{
    public static void main(String[] arguments) {
        
        float yearOne = 14000;
        System.out.println("Total investment: " + yearOne + "\n");
        
        float increase = (float) .40;
        yearOne = (yearOne * increase) + 14000;
        System.out.println("Investment after a 40% increase: " + yearOne + "\n");
   
        float yearTwo;
        yearTwo = yearOne - 1500;
        System.out.println("After taking a hit the toltal investment at the end"
                + " the second year is: " + yearTwo + "\n");
        
        float total;
        increase = (float) .12;
        
        
        yearTwo =  (yearTwo * increase); 
        total = yearTwo + 18100;
        
        System.out.println("During the third year the investment increase 12%. "
                + "The total was: "
                + total + "\n");
                
    }
    
}