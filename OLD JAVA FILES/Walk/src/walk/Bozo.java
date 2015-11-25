import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Bozo extends JFrame implements ActionListener {
        ImageIcon wt = new ImageIcon("bozo.gif");
        JButton bad = new JButton("IDK");
        JButton walk = new JButton(wt);
    
   public Bozo(){
        super("Magic Paw");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        FlowLayout flow = new FlowLayout();
        setLayout(flow);
        String time = new String("What time is it?");
        JLabel lab1 = new JLabel(time);

        bad.addActionListener(this);
        walk.addActionListener(this);
        
        add(lab1);
        add(bad);
        add(walk);
        
        pack();
        setVisible(true);
    }
        
    @Override
   public void actionPerformed(ActionEvent evt) {
       Object source = evt.getSource();
       if (source == bad) { System.out.println("Leave me the F... alone");
       }else if (source == walk)
            {
                System.out.println("IT'S WALKIE TIME MOTHERFUCKER");
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        FlowLayout flow = new FlowLayout();
        setLayout(flow);
        String time = new String("What time is it?");
        JLabel lab1 = new JLabel(time);

        bad.addActionListener(this);
        walk.addActionListener(this);
        
        add(lab1);
        add(bad);
        add(walk);
        
        pack();
        setVisible(true);
                
            }
       
   }
    
   public static void main(String[] args){
       Bozo bean = new Bozo();
   }
   
}