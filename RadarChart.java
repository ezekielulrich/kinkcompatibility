import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.HashMap;

public class RadarChart extends JPanel {

    private final ArrayList<HashMap<String, Double>> playmates;
    private final HashMap<String, String> pairs;

    public RadarChart(ArrayList<HashMap<String, Double>> playmates, HashMap<String, String> pairs) {
        this.playmates = playmates;
        this.pairs = pairs;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        int centerX = getWidth() / 2;
        int centerY = getHeight() / 2;

        int numplaymates = playmates.size();
        int angleStep = 360 / numplaymates;

        int maxValue = 26; // Assuming a maximum value

        for (HashMap<String, Double> playmate : playmates) {
            int i = 0;
            for (String pair : pairs.keySet()) {
                double value = playmate.get(pair);
                System.out.println(value);
                int radius = (int) ((value / maxValue) * 100); // Scale the value to fit within the chart
                int x = (int) (centerX + radius * Math.cos(Math.toRadians(i * angleStep)));
                int y = (int) (centerY + radius * Math.sin(Math.toRadians(i * angleStep)));
                g.drawLine(centerX, centerY, x, y);
                i++;
            }
        }
    }

    public static void main(String[] args) {
        ArrayList<HashMap<String, Double>> playmates = new ArrayList<>();
        playmates.add(new HashMap<String, Double>() {{
            put("Sub", 1.0);
            put("Pet", 1.0);
            put("Masochist", 1.0);
            put("You know who you are", 1.0);
            put("Slave", 1.0);

        }});

        final HashMap<String, String> pairs = new HashMap<>();
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

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(new RadarChart(playmates, pairs));
        frame.setVisible(true);
    }
}
