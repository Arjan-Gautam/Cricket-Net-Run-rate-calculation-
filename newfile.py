RunScored = int(input("Run scored: "))
OverCompleted = float(input("Over completed: "))
full_over = int(OverCompleted)
extra_balls = round((OverCompleted - full_over) * 10)
if extra_balls > 5:
	print("Invalid Input: One over has just 6 balls (0-5)")
else:	
      total_balls = full_over * 6 + extra_balls
      Runrate = (RunScored / total_balls)*6
      print(f"Net Runrate is {Runrate:.2f} Runs per over")
