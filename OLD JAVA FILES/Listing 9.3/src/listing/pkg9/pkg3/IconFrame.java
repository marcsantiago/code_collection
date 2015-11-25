import javax.swing.*;

public class IconFrame extends JFrame {
    
    JButton load, save, subscribe, unsubscribe;
    
    public IconFrame() {
        super("Icon Frame");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel = new JPanel();
        //create icons
        
        ImageIcon loadIcon = new ImageIcon("load.gif");
        ImageIcon saveIcon = new ImageIcon("save.gif");
        ImageIcon subscribeIcon = new ImageIcon("subscribe.gif");
        ImageIcon unsubscribeIcon = new ImageIcon("unsubscribe.gif");
        
       // create buttons
        load = new JButton("Load", loadIcon);
        save = new JButton("save", saveIcon);
        subscribe = new JButton("subscribe", subscribeIcon);
        unsubscribe = new JButton("unsubscribe", unsubscribeIcon);
        
        // add buttons to panel
        panel.add(load);
        panel.add(save);
        panel.add(subscribe);
        panel.add(unsubscribe);
        // add panel to frame
        add(panel);
        pack();
        setVisible(true);
    }
    public static void main(String[] args) {
        IconFrame ike = new IconFrame();
    }
}