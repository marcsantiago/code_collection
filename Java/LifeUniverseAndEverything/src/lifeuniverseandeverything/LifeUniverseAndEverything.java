package lifeuniverseandeverything;

import java.util.*;

/**
 *
 * @author marcsantiago
 */
public class LifeUniverseAndEverything {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        List<Integer> storedNumbers = new ArrayList();
        boolean exit = false;
    
        while(exit == false ){
            int number = input.nextInt();
            if(number == 42){
                exit = true;
            }
            else {
                storedNumbers.add(number);
            }
        }
        
        for(int numbers : storedNumbers){
            System.out.println(numbers);
        }
    }
    
}
