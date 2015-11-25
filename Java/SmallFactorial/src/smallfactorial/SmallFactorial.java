package smallfactorial;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class SmallFactorial {
 
    public static void main(String[] args) throws IOException {
    
       InputStreamReader isr =  new InputStreamReader(System.in);
       BufferedReader input = new BufferedReader(isr);
       Integer inter = Integer.parseInt(input.readLine());
       for (Integer i = 0; i<inter; i++) {
           Long in = Long.parseLong(input.readLine());
           BigInteger fin = BigInteger.valueOf(in.longValue());
           System.out.println(factorial(fin));
       }
    }
    
    
    public static BigInteger factorial(BigInteger baseNumber){
        BigInteger fact = BigInteger.ONE;
        BigInteger sub = BigInteger.ONE;
        while (baseNumber.intValue() !=0) {
            fact = fact.multiply(baseNumber);
            baseNumber = baseNumber.subtract(sub);
        }
        
        return fact;
    }
    
}
