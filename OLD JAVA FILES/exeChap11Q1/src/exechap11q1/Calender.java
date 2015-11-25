import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class Calender extends JFrame {
    JLabel[] days = new JLabel[31];
    JLabel[] dayTitles = new JLabel[7];
    JLabel monthTitle = new JLabel("October 2000");

    Calender() {
        super("October 2000");
        setSize(260, 260);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container pane = getContentPane();
        FlowLayout flow = new FlowLayout();
        pane.setLayout(flow);
        JPanel titlePane = new JPanel();
        titlePane.setLayout(flow);
        titlePane.add(monthTitle);
        pane.add(titlePane);
        JPanel monthPane = new JPanel();
        GridLayout calLayout = new GridLayout(6, 7);
        monthPane.setLayout(calLayout);
        String[] dayNames = { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
        for (int i = 0; i < 7; i++) {
            dayTitles[i] = new JLabel(dayNames[i]);
            monthPane.add(dayTitles[i]);
        }
        for (int i = 0; i < days.length; i++) {
            days[i] = new JLabel("" + (i+1));
            monthPane.add(days[i]);
        }
        pane.add(monthPane);
        setContentPane(pane);
    }

    public static void main(String[] arguments) {
        Calender cal = new Calender();
        cal.show();
    }
}