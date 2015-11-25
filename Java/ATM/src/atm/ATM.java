package atm;

import java.text.DecimalFormat;
import java.util.*;

public class ATM {

    public static void main(String[] args) {
        
        Double fee = 0.50;
        
        Scanner input = new Scanner(System.in);
        String line = input.nextLine(); 
        
        DecimalFormat df = new DecimalFormat();
        df.setMaximumFractionDigits(2);
        df.setMinimumFractionDigits(2);
        
        Integer widthdrawlAmount = Integer.parseInt(line.split(" ")[0]);
        Double bankAccount = Double.parseDouble(line.split(" ")[1]);
        
        
        if(bankAccount > 0) {
            if(widthdrawlAmount % 5 == 0){
                if((widthdrawlAmount.doubleValue() + fee) > bankAccount){
                    System.out.println(df.format(bankAccount));
                }
                else{
                    System.out.println(df.format(bankAccount - (widthdrawlAmount.doubleValue() + fee)));
                }
            }
            else{
                System.out.println(df.format(bankAccount));
            }
        }
   
    }
    
}
