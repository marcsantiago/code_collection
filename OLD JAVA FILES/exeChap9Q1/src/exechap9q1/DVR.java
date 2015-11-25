import javax.swing.*;


public class DVR extends JFrame {  
    public DVR() {
        
        
        
        super("DVR Control Frame");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //what to do on close
        setSize(450, 300);
        setLookAndFeel();
      
        JButton play = new JButton("play");
        JButton stop = new JButton("Stop");
        JButton eject = new JButton("eject");
        JButton rewind =  new JButton("rewind");
        JButton fastforward = new JButton("Fast-Forward");
        JButton pause = new JButton("pause");
        JPanel pane = new JPanel();
        
        
        pane.add(play);
        pane.add(stop);
        pane.add(eject);
        pane.add(rewind);
        pane.add(fastforward);
        pane.add(pause);
        
        add(pane);
        setVisible(true);
        
    }
private static void setLookAndFeel() {
    try {
        UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");
    
    } catch (Exception exc) {
        //ignore error
        }  
    }
    
    public static void main(String[] args) {
        setLookAndFeel();
        DVR dvr = new DVR();
    }
    
}