import java.awt.Point;

class FourDPoint extends Point {
    int z;
    int t;
    
    FourDPoint(int x, int y, int inZ, int inT) {
        
        super(x,y); //x and y are primitive data points from the Point super class
        
        this.z = inZ; //could have also written FourDpoint.z = inZ
        this.t = inT;
    }
    
    public static void main(String[] arguments){
        
        FourDPoint np = new FourDPoint(50,100,250,300);
        
        System.out.println("Point 1: " + np.x);
        System.out.println("Point 2: " + np.y);
        System.out.println("Point 3: " + np.z);
        System.out.println("Point 4: " + np.t);
    }
}
        