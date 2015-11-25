/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package move;

/**
 *
 * @author marcsantago
 */
import javax.swing.*;
import java.awt.*;

public class Move extends JFrame{
     public Move(){
          setSize(400,400);
          setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
          setLocationRelativeTo(null);
          setVisible(true);
     }

     public static void main(String a[]){
         new Move();
     }

     public void paint(Graphics g){
          g.setColor(Color.BLUE);
          g.drawOval(40, 40, 60, 60); //FOR CIRCLE
          g.setColor(Color.RED);
          g.drawRect(80, 30, 200, 200); // FOR SQUARE
          g.setColor(Color.MAGENTA);
          g.drawRect(200, 100, 100, 200); // FOR RECT
     }
}
