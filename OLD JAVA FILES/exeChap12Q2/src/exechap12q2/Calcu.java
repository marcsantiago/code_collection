import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class Calcu extends JFrame implements ActionListener {
    JTextField one = new JTextField("0", 5);
    JLabel plus = new JLabel("+/-");
    JTextField two = new JTextField("0", 5);
    JButton add = new JButton("+");
    JButton sub = new JButton("-");
    JTextField result = new JTextField("0", 5);
    int value2;
    int value1;

   
    Calcu() {
        super("Add Two Numbers");
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container pane = getContentPane();
        FlowLayout flow = new FlowLayout();
        pane.setLayout(flow);
        add.addActionListener(this);
        sub.addActionListener(this);
        pane.add(one);
        pane.add(plus);
        pane.add(two);
        pane.add(add);
        pane.add(sub);
        
        pane.add(result);
        setContentPane(pane);
        pack();
        setVisible(true);
        
    }
        
     public static void main(String[] arguments) {
        Calcu frame = new Calcu();
    }

    public void actionPerformed(ActionEvent evt) {
        try {
            Object source = evt.getSource();
            if(source == add){
            value1= Integer.parseInt(one.getText());
            value2= Integer.parseInt(two.getText());
            result.setText("" + (value1 + value2));
            }
            else {
             result.setText("" + (value1 - value2));   
            }
        } catch (NumberFormatException exc) {
            one.setText("0");
            two.setText("0");
            result.setText("0");
        }
    }
    
}
