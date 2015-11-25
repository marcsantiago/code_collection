package enormousinputtest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EnormousInputTest {

    public static void main(String[] args) throws IOException {
        
        Integer n = 0, k = 0, count = 0, number = 0;
        //THIS METHOD BELOW IS FASTER
        InputStreamReader inr = new InputStreamReader(System.in);
        BufferedReader bfr = new BufferedReader(inr);
        
        String line =  bfr.readLine();
        
        n = Integer.parseInt(line.split(" ")[0]);
        k = Integer.parseInt(line.split(" ")[1]);
        
        
        while(n != 0){
            number = Integer.parseInt(bfr.readLine());
            if(number % k == 0){
                count++;
        }
            n--;
    }
        bfr.close();
        System.out.println(count);
    
}
}
