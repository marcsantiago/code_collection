class Ball {
    
    int radius;  // Abstract class properties
    int diameter;
    String color;
    String purpose;  
    
    int Haecceities;
    
    Ball(int haec){  //individualizing property
        Haecceities = haec;
    }
            
    public static void main(String[] arguments){
        
        Ball basketBall1 = new Ball(1); //First instatiation of a BasketBall
        
        basketBall1.color = "Orange with parralle black lines";
        basketBall1.purpose = "Object to play basketball with";
        basketBall1.radius = 4;
        basketBall1.diameter = 8;
        
        Ball basketBall2 = new Ball(2); //Second instatiation of a BasketBall
        
        basketBall2.color = "Orange with parralle black lines";
        basketBall2.purpose = "Object to play basketball with";
        basketBall2.radius = 4;
        basketBall2.diameter = 8;
     //*************************************************************//
        /*Notice that all the properties are the same except for Haecceities*/
        
        Ball soccerBall = new Ball(3);
        
        soccerBall.color = "White";
        soccerBall.purpose = "Object to play soccer with";
        soccerBall.radius = 2;
        soccerBall.diameter = 4;
        
        System.out.println("Basket Ball 1 properties:");
        System.out.println("Color: " + basketBall1.color);
        System.out.println("Purpose: " + basketBall1.purpose);
        System.out.println("Radius: " + basketBall1.radius);
        System.out.println("Daimeter: " + basketBall1.diameter);
        
        System.out.println("\n");
        
        System.out.println("Basket Ball 2 properties:");
        System.out.println("Color: " + basketBall2.color);
        System.out.println("Purpose: " + basketBall2.purpose);
        System.out.println("Radius: " + basketBall2.radius);
        System.out.println("Daimeter: " + basketBall2.diameter);
        
        System.out.println("Are Basketball 1 and 2 the same object: " + 
                basketBall1.equals(basketBall2)); 
        //logical comparison to test whether both BasketBalls are the same
        
        System.out.println("\n");
        
        System.out.println("Soccer ball properties:");
        System.out.println("Color: " + soccerBall.color);
        System.out.println("Purpose: " + soccerBall.purpose);
        System.out.println("Radius: " + soccerBall.radius);
        System.out.println("Daimeter: " + soccerBall.diameter);
        
        
        }    
    }  

    
    
