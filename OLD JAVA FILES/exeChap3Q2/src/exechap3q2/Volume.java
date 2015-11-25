class Volume {
    
        int height = 0;
        int width = 0;
        int depth= 0;
        int volume;
        
        void Calculate(){
            
            volume =  (height * width * depth);  
            System.out.println("Volume: " + volume);
        }
        
   public static void main(String[] arguments) {
        
   Volume Cube = new Volume();
   Cube.height = 3;
   Cube.depth = 3;
   Cube.width = 3;
        System.out.println("Height: " + Cube.height);
        System.out.println("depth: " + Cube.depth);
        System.out.println("Width: " + Cube.width);
   
   Cube.Calculate();
   
    }  
}
