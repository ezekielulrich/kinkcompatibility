/*
 * FEATURES TO ADD:
 * Data visualization:
 * - Plot radar chart
 * - Most compatible kinks
 * Ability to scrape from links
 */

// For the main program
import java.util.ArrayList;
import java.util.HashMap;

// For the GUI
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;

public class KinkCompatibilityCalculator {
    private static final HashMap<String, String> pairs = new HashMap<>();
    private static int num = 0;
    static {
        pairs.put("Rigger", "Rope bunny");
        pairs.put("Sadist", "Masochist");
        pairs.put("Dominant", "Submissive");
        pairs.put("Brat tamer", "Brat");
        pairs.put("Daddy/Mommy", "Boy/Girl");
        pairs.put("Primal (Hunter)", "Primal (Prey)");
        pairs.put("Master/Mistress", "Slave");
        pairs.put("Degrader", "Degradee");
        pairs.put("Owner", "Pet");
        pairs.put("Switch", "Switch");
        pairs.put("Vanilla", "Vanilla");
        pairs.put("Experimentalist", "Experimentalist");
        pairs.put("Exhibitionist", "Exhibitionist");
        pairs.put("Voyeur", "Voyeur");
        pairs.put("Ageplayer", "Ageplayer");
        pairs.put("Non-monogamist", "Non-monogamist");
    }

    private static double calculateCompatibility(ArrayList<HashMap<String, Double>> playmates) {
        double compatibility = 0;
        int n = pairs.size();

        for (String kink : pairs.keySet()) {
            double topValue = 0;
            HashMap<String, Double> top = null;

            for (HashMap<String, Double> playmate : playmates) {
                if (playmate.get(kink) > topValue) {
                    top = playmate;
                    topValue = playmate.get(kink);
                }
            }

            if (top != null) {

                for (HashMap<String, Double> playmate : playmates) {
                    if (!playmate.equals(top)) {
                        topValue *= playmate.get(kink);
                    }
                }
            }

            compatibility += topValue;
        }

        return compatibility / n;
    }

    private static HashMap<String, Double> stripText(String textResults) {
        String[] lines = textResults.split("\n");
        HashMap<String, Double> results = new HashMap<>();

        for (int i = 1; i < 26; i++) {
            String[] parts = lines[i].split(" ", 2);
            String kink = parts[1].trim();
            double percentage = Double.parseDouble(parts[0].replaceAll("%", "")) / 100.0;
            results.put(kink, percentage);
        }

        return results;
    }

    public static void main(String[] args) {

        ArrayList<HashMap<String, Double>> playmates = new ArrayList<>();

        // Main frame and panel
        JFrame frame = new JFrame("Kink Compatibility Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 500);

        // Area for entering results
        JTextArea textArea = new JTextArea();
        textArea.setPreferredSize(new Dimension(150, 50));
        textArea.setMargin(new Insets(10, 20, 10, 20));
        textArea.setOpaque(false);
        textArea.setForeground(Color.WHITE);
        textArea.setText("Enter copied results here."); // Set initial text

        textArea.addFocusListener(new FocusListener() {
            @Override
            public void focusGained(FocusEvent e) {
                // When the field gains focus, set the text color to be fully opaque
                textArea.setForeground(Color.WHITE);
                if (textArea.getText().equals("Enter copied results here.")) {
                    textArea.setText(""); // Clear initial text
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                // When the field loses focus, restore the transparent text color if it's empty
                if (textArea.getText().isEmpty()) {
                    textArea.setForeground(Color.WHITE);
                    textArea.setText("Enter copied results here.");
                }
            }
        });

        // Button for saving results
        JButton submitButton = new JButton("Add Results");
        submitButton.setBackground(Color.BLACK);

        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String response = textArea.getText();
                if (!response.isEmpty()) {
                    HashMap<String, Double> playmate = stripText(response);
                    playmates.add(playmate);
                    num++;
                }
                textArea.setText("");
            }
        });

        // Calculate button
        JButton calculateButton = new JButton("Calculate Compatibility");
        calculateButton.setBackground(Color.BLACK);

        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (num > 1) {
                    double compatibility = calculateCompatibility(playmates);
                    JOptionPane.showMessageDialog(frame, "You are " + (Math.round(100 * compatibility * 100.0) / 100.0) + "% compatible!");
                } else {
                    JOptionPane.showMessageDialog(frame, "You need at least two people to calculate compatibility");
                }
            }
        });

        // Define layout
        Container contentPane = frame.getContentPane();
        contentPane.setBackground(Color.BLACK); // Set background color of the panel

        // Add elements
        contentPane.setLayout(new BorderLayout());
        contentPane.add(textArea, BorderLayout.CENTER);
        contentPane.add(calculateButton, BorderLayout.SOUTH);
        contentPane.add(submitButton, BorderLayout.NORTH);

        frame.setVisible(true);
    }
}