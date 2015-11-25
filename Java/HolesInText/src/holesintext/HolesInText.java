package holesintext;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HolesInText {

    public static void main(String[] args) throws IOException {
        
        InputStreamReader isr =  new InputStreamReader(System.in);
        BufferedReader input = new BufferedReader(isr);
        
        String a = "A";
        String d = "D";
        String o = "O";
        String p = "P";
        String r = "R";
        String q = "Q";
        String b = "B";
        
        
        Integer number = Integer.parseInt(input.readLine());
        for (Integer i =0; i<number; i++) {
            Integer count = 0;
            String line = input.readLine();
            for (Integer j = 0; j<line.length(); j++) {
                
                if (line.toCharArray()[j] ==  a.toCharArray()[0]) {
                    count++;
                }
                else if (line.toCharArray()[j] ==  d.toCharArray()[0]) {
                    count++;
                }
                else if (line.toCharArray()[j] ==  o.toCharArray()[0]) {
                    count++;
                }
                else if (line.toCharArray()[j] ==  p.toCharArray()[0]) {
                    count++;
                }
                else if (line.toCharArray()[j] ==  r.toCharArray()[0]) {
                    count++;
                }
                else if (line.toCharArray()[j] ==  q.toCharArray()[0]) {
                    count++;
                }
                else if (line.toCharArray()[j] ==  b.toCharArray()[0]) {
                    count += 2;
                }
            }
            System.out.println(count);
            
        }
    }
    
}
