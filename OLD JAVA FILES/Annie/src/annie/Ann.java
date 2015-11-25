import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class Ann extends JPanel implements ActionListener {

    int currentCard = 0;
    CardLayout cards = new CardLayout();
    An[] ask = new An[6];
    
    
    
    public Ann(){
        super();
        setSize(300, 700);
        setLayout(cards);
        //survey
        String question1 = "Are you Annie?";
        String[] responses1 = {"Yes", "No"};
        ask[0] = new An(question1, responses1, 1);
        
        String question2 = "Are you a naughty, naughty girl?";
        String[] responses2 = {"Yes", "No"};
        ask[1] = new An(question2, responses2,1);
        
        String question3 = "Do you love Marc Anthony Santiago?";
        String[] responses3 = {"Yes", "No", "Not Sure"};
        ask[2] = new An(question3, responses3, 2);
        
        String question4 = "Will you suck his dick?";
        String[] responses4 = {"Yes, Yes"};
        ask[3] = new An(question4, responses4, 1);
        
        String question5 = "Are you still happy with him?";
        String[] responses5 = {"Yes", "Duh", "No","Not Sure :("};
        ask[4] = new An(question5, responses5, 3);
        
        String question6 = "Will you give him a kiss now :)?";
        String[] responses6 = {"Fuck Yes", "I Don't Think So"};
        ask[5] = new An(question6, responses6, 1);
        
        ask[5].setFinalQuestion(true);
        addListeners();
  }
    
    private void addListeners(){
    for (int i = 0; i < ask.length; i++) {
        ask[i].nextButton.addActionListener(this);
        ask[i].finalButton.addActionListener(this);
        add(ask[i],"Card " + i);
        }
    }
        
    @Override
    public void actionPerformed(ActionEvent evt) {
    currentCard++;
    if(currentCard >= ask.length) {
        System.exit(0);
    }
    cards.show(this, "Card " + currentCard);
    
         }
    }

    
class An extends JPanel {
    
    JLabel question;
    JRadioButton[] response;
    JButton nextButton = new JButton("Next");
    JButton finalButton = new JButton("Final");
    
    
    An (String ques, String[] resp, int def) {
        super();
        setSize(300, 700);
        question = new JLabel(ques);
        response = new JRadioButton[resp.length];
        JPanel sub1 = new JPanel();
        ButtonGroup group = new ButtonGroup();
        JLabel quesLabel = new JLabel(ques);
        sub1.add(quesLabel);
        JPanel sub2 = new JPanel();
            
            for(int i = 0; i < resp.length; i++) {
            if (def == i) {
                response[i] = new JRadioButton(resp[i], true);
            } else {
                response[i] = new JRadioButton(resp[i], false);
            }
            group.add(response[i]);
            sub2.add(response[i]);
            }
       
       JPanel sub3 = new JPanel();
       nextButton.setEnabled(true);
       sub3.add(nextButton);
       
       JPanel sub4 = new JPanel();
       nextButton.setEnabled(true);
       sub4.add(nextButton);
        
       JPanel sub5 = new JPanel();
       nextButton.setEnabled(true);
       sub5.add(nextButton);
       
       finalButton.setEnabled(false);
       sub5.add(finalButton);
       GridLayout grid = new GridLayout(3,1);
       setLayout(grid);
       add(sub1);
       add(sub2);
       add(sub3);
       add(sub4);
       add(sub5);
    }
    
void setFinalQuestion(boolean finalQuestion) {
    if(finalQuestion) {
        nextButton.setEnabled(false);
        finalButton.setEnabled(true);
        }
    }
}
    
