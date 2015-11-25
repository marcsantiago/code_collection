public class Weather {
    public static void main(String[] arguments) {
        float fah = 86;
        System.out.println(fah + " degrees Fahrenheit is ...");
        //To convert Fahrenhiet to Celsius
        //begin by substracting 32
        fah = fah - 32;
        //Divide that by 9
        fah = fah / 9;
        //Multiply by 5
        fah = fah * 5;
        System.out.println(fah + " degress Celsius\n");
        
        float cel = 33;
        System.out.println(cel + " degrees Celsius is ...");
        //To convert Celsius to Fahrenheit
        //Multiply by 9
        cel = cel * 9;
        //Divide by 5
        cel = cel / 5;
        //add 32
        cel = cel + 32;
        System.out.println( cel + " degrees Fahrenheit");
              
    }
}