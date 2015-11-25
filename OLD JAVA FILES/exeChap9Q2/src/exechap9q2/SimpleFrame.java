import javax.swing.*;

public class SimpleFrame extends JFrame {
    PasswordFrame pass = new PasswordFrame();
    
    public SimpleFrame() {
        super("Ask Password");
        setSize(540, 80);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        pass.setVisible(true);
}

    public static void main(String[] arguments) {
        SimpleFrame ask = new SimpleFrame();
        
    }
}

class PasswordFrame extends JFrame {
    public PasswordFrame() {
        super("Password");
        setSize(210, 130);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        JPanel pane = new JPanel();
        JLabel usernameLabel = new JLabel("Username: ");
        JTextField username = new JTextField(8);
        JLabel passwordLabel = new JLabel("Password: ");
        JPasswordField password = new JPasswordField(8);
        pane.add(usernameLabel);
        pane.add(username);
        pane.add(passwordLabel);
        pane.add(password);
        setContentPane(pane);
        setVisible(false);
    }
}