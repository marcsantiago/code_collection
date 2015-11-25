package trailingzeros;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.*;

public class TrailingZeros {
    public static void main(String[] args) throws IOException {
        Integer sieve [] = {5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625};
        
        InputStreamReader inr = new InputStreamReader(System.in);
        BufferedReader bfr = new BufferedReader(inr);
       
        Integer input = Integer.parseInt(bfr.readLine());
        
        for(int i = 0; i<input; i++) {
            Integer zeros = 0;
            Integer holder = Integer.parseInt(bfr.readLine());
            for(int j = 0; j<12; j++) {
                if (sieve[j] > holder) {
                break;
            }
            else {
                zeros += (int) (holder / sieve[j]);
            }
 
            }
            System.out.println(zeros);
        } 
        bfr.close();
    }
    
}
