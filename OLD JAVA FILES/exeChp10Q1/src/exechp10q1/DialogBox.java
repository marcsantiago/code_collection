import java.awt.event.*;
import javax.swing.*;

public class DialogBox extends JFrame {
    public DialogBox() {
        super("Title Frame");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        String response = JOptionPane.showInputDialog(null,
            "Enter a Title for the Frame:");
        setTitle(response); //method within JOptionPane
    }
    
    public static void main(String[] arguments) {
        JFrame frame = new DialogBox();
    }
}