public class InstanceCounter {
    private static int numInstances = 0; //private class variable
    
    protected static int getCount() { //read method to access private class variable
        return numInstances;
    }
    
    private static void addInstance() { // modifies numInstance via return from
                                    // getCount method
        numInstances++;
    }
    
    
    InstanceCounter(){                  //constructor which is public and set with the addInstance method
        InstanceCounter.addInstance();
    }
    
    
    public static void main(String[] arguments) {       //main program
        
        System.out.println("Starting with " + InstanceCounter.getCount() + " objects"); // 0 objects right now
        
        for (int i = 0; i < 500; i++){
            new InstanceCounter(); //new object is created
        }
        System.out.println("Created " + InstanceCounter.getCount() + " objects");
        
    } 
}