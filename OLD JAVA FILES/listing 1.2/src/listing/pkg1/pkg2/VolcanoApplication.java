class VolcanoApplication {
    
    String status;
        int speed;
        int power;
        
    
VolcanoApplication(String in1, int in2, int in3) {
        
        status = in1;
        speed = in2;
        power = in3;
        
        
}
    
       
    
        void showAttributes() {
        System.out.println("Status: " + status);
        System.out.println("Speed: " + speed);
        System.out.println("Power: " + power);
        
    }


public static void main(String[] arguments) {

VolcanoApplication walle = new VolcanoApplication("HEllO, All Systems are good", 5, 10);
walle.showAttributes();
        
        
    System.out.println(77%8);
    
    }
}
