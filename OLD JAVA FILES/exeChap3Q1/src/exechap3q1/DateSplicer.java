import java.util.StringTokenizer;

class DateSplicer {
    public static void main(String[] arguments) {
        
        StringTokenizer st1;        
        String quote1 = "01/15/1991";        
        
        
        st1 = new StringTokenizer(quote1, "/");
        
        System.out.println("Month: " + st1.nextToken());
        System.out.println("Day: " + st1.nextToken());
        System.out.println("Year: " + st1.nextToken());
      
    }
}