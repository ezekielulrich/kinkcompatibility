# Kink Compatibility Calculator

This is a Java program that calculates compatibility based on BDSM test results. Users can paste their results into a text area, and the program calculates compatibility with other users.

## How to Use

1. **Run the Program**:

   - Compile and run the Java program in an IDE or using the command line.

2. **Enter Results**:

   - Paste BDSM test results into the provided text area. The initial text "Enter copied results here." will disappear when you click on the area.

3. **Save Results**:

   - Click the "Add Results" button to save the entered results.

4. **Calculate Compatibility**:

   - When at least two sets of results are saved, click the "Calculate Compatibility" button to see the compatibility percentage.

## Features

- Allows users to input BDSM test results.
- Calculates compatibility based on saved results.
- Provides compatibility percentage.

## Program Explanation

- The program uses Swing for the GUI (Graphical User Interface).
- It maintains a HashMap of BDSM roles and their corresponding pairs.
- It calculates compatibility by finding the highest percentage match for each role.
- It allows users to enter multiple sets of results for comparison.
- The program provides visual feedback on user interactions with the text area.

*Note: Please ensure you have Java and a compatible IDE installed to run this program.*