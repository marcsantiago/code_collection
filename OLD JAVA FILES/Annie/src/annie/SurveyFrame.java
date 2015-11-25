import java.awt.*;
import javax.swing.*;

public class SurveyFrame extends JFrame {
    public SurveyFrame() {
        super("You're A Dirty Girl");
        setSize(700, 290);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLookAndFeel();
        
        Ann ie = new Ann();
        add(ie);
        setVisible(true);
    }
    
    private void setLookAndFeel() {
        try {
            UIManager.setLookAndFeel(
                    "com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");
            SwingUtilities.updateComponentTreeUI(this);
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException exc) {
            System.err.println(exc);
        }
    }
    
    public static void main(String[] args){
        SurveyFrame surv = new SurveyFrame();
    }
}