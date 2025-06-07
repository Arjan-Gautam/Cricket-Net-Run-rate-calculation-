# Cricket-Net-Run-rate-calculation-
Simple Python script to calculate Net Run Rate in cricket with overs validation.
🏏 Net Run Rate Calculator

This is a simple Python script to calculate the Net Run Rate (NRR) in cricket based on user input for total runs scored and overs completed.

📌 How It Works

The user inputs:

Total runs scored (as an integer)

Overs completed (as a float, e.g., 10.3 means 10 overs and 3 balls)


The script checks if the input is valid (no more than 5 balls after the decimal).

It calculates the total number of balls bowled.

Then it calculates and displays the Net Run Rate (runs per over), rounded to 2 decimal places.


📄 Example Input/Output

Run scored: 250  
Over completed: 45.3  
Net Runrate is 5.49 runs per over

⚠️ Validation

The decimal part of the overs should be between 0 and 5.

For example, 10.6 is invalid because an over has only 6 balls.


▶️ How to Run

1. Make sure you have Python installed.


2. Run the script:



python
